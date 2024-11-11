import reflex as rx
from app.states import IndexState
import app.styles.styles as styles
from app.styles.colors import *

def spreading_factor_input() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Spreading Factor", size="4", color=Color.BACKGROUND.value),
            rx.text(IndexState.sf),
            rx.slider(
                default_value=1,
                min=0,
                max=10,
                on_change=IndexState.set_sf.throttle(100),
                color_scheme="mint",
            ),
        ),
    )


def number_of_users_input() -> rx.Component:
    return rx.card(
        rx.form(
            rx.vstack(
                rx.heading("Number of users", size="4", color=Color.BACKGROUND.value),
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
    )

def users_data_input() -> rx.Component:
    return  rx.card(
        rx.form(
            rx.vstack(
                rx.heading("Users Data", size="4", color=Color.BACKGROUND.value),
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
    )

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            spreading_factor_input(),
            number_of_users_input(),
            users_data_input(),
            rx.card(
                rx.text(IndexState.decoded_data),
            ),
            width="100%",
            spacing="2",
            direction="column",
        ),

        # Properties for make a sidebar
        width=styles.SIDEBAR_WIDTH,
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        align_items="left",
        z_index="10",
        padding=styles.Spacer.LARGE.value,
        background_color=Color.SECONDARY.value, 
        backdrop_filter="blur(10px)",
    )