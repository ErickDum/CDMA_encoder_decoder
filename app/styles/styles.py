import reflex as rx
from enum import Enum
from .colors import *

# Constants
SIDEBAR_WIDTH = "25em"

class Spacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "1em"
    LARGE = "2em"

BASE_STYLE = { 
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "margin_bottom": "0.2em",
        "margin_top": "0.5em",
        "color": Color.CONTENT.value
    },
    rx.button: {
        "background_color": Color.PRIMARY.value,
        "variant": "outline",
    }
}