import reflex as rx
import matplotlib.pyplot as plt
from reflex_pyplot import pyplot
from app.calc import generate_codes, encode_data, decode_data
from app.plots import step_plot, binary_plot

class IndexState(rx.State):
    sf: int = 2
    num_users: int = 0
    users_names: list[str]
    users_data: list[list[int]]
    spreadig_codes: list[list[int]]
    combinated_signal: list[int]
    decoded_data: list[list[int]]
    users_grater_than_sf: bool = False

    # Figs
    users_data_figs: list[plt.Figure]
    combinated_signal_fig: list[plt.Figure]
    users_decoded_figs: list[plt.Figure] = [None]*4

    def set_sf(self, sf: list[int]):
        self.sf = 2**sf[0]

    def set_num_users(self, form_data: dict):
        self.num_users = int(form_data.get("number_of_users"))
        self.users_grater_than_sf = True if self.num_users > self.sf else False
        if self.users_grater_than_sf:
            return
        self.users_names = [f"User{i + 1}" for i in range(self.num_users)]

    def create_users_figs(self):
        self.users_data_figs.clear()
        for i in range(self.num_users):
            if i > 4:
                break
            fig = binary_plot(self.users_data[i], xlabel="Time", ylabel="Level", title=f"User {i + 1} Signal")
            self.users_data_figs.append(fig)
        
    def create_combinated_fig(self):
        self.combinated_signal_fig = step_plot(self.combinated_signal, self.sf, xlabel="Time", ylabel="Voltage", title="Combinated Signal")
    
    def create_decoded_figs(self):
        self.users_decoded_figs.clear()
        for i in range(self.num_users):
            if i > 4:
                break
            fig = binary_plot(self.decoded_data[i], xlabel="Time", ylabel="Level", title=f"User {i + 1} Decoded Signal")
            self.users_decoded_figs.append(fig)
    
    def calculate(self, form_data: dict):
        if self.users_grater_than_sf:
            return
        # Set the data for each user
        self.users_data.clear()
        for user in self.users_names:
            self.users_data.append(list(map(int, form_data.get(user))))
        
        # Generate codes
        self.spreadig_codes = generate_codes(self.sf)

        # Encode data
        self.combinated_signal = encode_data(self.num_users, self.users_data, self.spreadig_codes)

        # Decode data
        self.decoded_data = decode_data(self.num_users, self.combinated_signal, self.spreadig_codes)

        # Generate figures
        self.create_users_figs()
        self.create_combinated_fig()
        self.create_decoded_figs()
        

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.card(
                rx.vstack(
                    rx.heading("Spreading Factor", size="4"),
                    rx.text(IndexState.sf),
                    rx.slider(
                        default_value=1,
                        min=0,
                        max=10,
                        on_change=IndexState.set_sf.throttle(100),
                    ),
                ),

            ),
            rx.card(
                rx.form(
                    rx.vstack(
                        rx.heading("Number of users", size="4"),
                        rx.hstack(
                            rx.input(
                            plahceholder="Number of users",
                            name="number_of_users",
                            ),
                            rx.button("Add", type="submit"),
                        ),
                        rx.cond(
                            IndexState.users_grater_than_sf,
                            rx.callout(
                                "The number of users is greater than the spreading factor",
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",   
                                size = "1",
                            ),
                        ),
                    ),
                    on_submit=IndexState.set_num_users,
                ), 
            ),

            rx.card(
                rx.form(
                    rx.vstack(
                        rx.heading("Users Data", size="4"),
                        rx.foreach(
                            IndexState.users_names,
                            lambda user: rx.hstack(
                                rx.text(f"{user[:4]} {user[4:]}"),
                                rx.input(
                                    plahceholder=user,
                                    name=user,
                                ),
                            ),
                        ),
                        rx.button("Calculate", type="submit"),
                    ),
                    on_submit=IndexState.calculate,
                ),
            ),
            rx.card(
                rx.text(IndexState.decoded_data),
            ),
            width="100%",
            spacing="2",
            direction="column",
        ),

        # Properties for make a sidebar
        width="400px",
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        align_items="left",
        z_index="10",
        backdrop_filter="blur(10px)",
        padding="2em",

        background_color = "gray",
    )

@rx.page("/")
def index() -> rx.Component:
    return rx.box(
        sidebar(),
        rx.box(
            rx.heading("Users data graphs"),
            rx.foreach(
                IndexState.users_data_figs,
                lambda fig: pyplot(fig),
            ),
            rx.heading("Combinated signal graph"),
            pyplot(
                IndexState.combinated_signal_fig,
            ),
            rx.heading("Users decoded graphs"),
            rx.foreach(
                IndexState.users_decoded_figs,
                lambda fig: pyplot(fig),
            ),
            padding_left="400px",
        ),
        background_color = "gray",
    )