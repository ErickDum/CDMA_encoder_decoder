import reflex as rx
import numpy as np
import matplotlib.pyplot as plt
from reflex_pyplot import pyplot


#Example data
data = [(0, 1, 0), (1, 1, 0), (0, 0, 0), (1, 1, 1)]
codes = [[1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
combinated = [0, 0, -4, 0, 2, 2, -2, 2, -2, -2, -2, 2]
decoded = [[0, 1, 0], [1, 1, 0], [0, 0, 0], [1, 1, 1]]

class IndexState(rx.State):
    sf: int = 2

    def set_sf(self, sf: list[int]):
        self.sf = 2**sf[0]


def graph(data):
    # Step graph
    x_values = np.arange(len(data) + 1)
    y_values = np.repeat(data, 2)

    x_step = np.repeat(x_values, 2)[1:-1]

    fig, ax = plt.subplots(figsize=(18, 3))
    ax.step(x_step, y_values, where='post', linewidth=2)
    ax.set_xlabel('Sample')
    ax.set_ylabel('Amplitude')
    ax.set_title('Step Plot of Combinated Signal')
    ax.grid(True)

    plt.close(fig)

    return fig


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
                        max=5,
                        on_change=IndexState.set_sf.throttle(100),
                    ),
                ),

            ),
            rx.card(
                rx.heading("Users", size="4"),
                rx.form(
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Number of users", size="1"),
                            rx.input(plahceholder="number", name="number_of_users"),
                        ),
                        rx.hstack(
                            rx.heading("Users data", size="1"),
                            rx.input(plahceholder="data", name="data"),
                        ),
                    ),
                ),
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
            rx.text("Hello, World!"),
            pyplot(
                graph(combinated),
            ),
            padding_left="400px",
        ),
        background_color = "gray",
    )