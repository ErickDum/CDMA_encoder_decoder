import reflex as rx
from app.components import sidebar, main_content
from app.styles.colors import *

@rx.page("/")
def index() -> rx.Component:
    return rx.box(
        sidebar(),
        main_content(),
        height="100%",
        width="100%",
        background_color=Color.BACKGROUND.value,
    )