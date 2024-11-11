import reflex as rx
import matplotlib.pyplot as plt

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
            if i > 3:
                break
            fig = binary_plot(self.users_data[i], xlabel="Time", ylabel="Level", title=f"User {i + 1} Signal")
            self.users_data_figs.append(fig)
        
    def create_combinated_fig(self):
        self.combinated_signal_fig = step_plot(self.combinated_signal, self.sf, xlabel="Time", ylabel="Voltage", title="Combinated Signal")
    
    def create_decoded_figs(self):
        self.users_decoded_figs.clear()
        for i in range(self.num_users):
            if i > 3:
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