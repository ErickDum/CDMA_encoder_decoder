import reflex as rx
from app.states import IndexState
from reflex_pyplot import pyplot
import app.styles.styles as styles

def main_content() -> rx.Component:
    return rx.box(
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
        margin_left=styles.SIDEBAR_WIDTH,
        padding_x=styles.Spacer.MEDIUM.value,
        padding_y=styles.Spacer.SMALL.value,
    )