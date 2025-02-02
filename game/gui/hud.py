import arcade
from arcade import gui

from engine import scripts

HP_WIDTH = 150
HP_HEIGHT = 20
HP_BORDER = 2
HP_X = 10 + HP_WIDTH / 2 + HP_BORDER
HP_Y = 10 + HP_HEIGHT / 2 + HP_BORDER
HP_BORDER_COLOR = (255, 255, 255)
HP_BAR_COLOR = (0, 255, 0)
HP_TEXT_MARGIN = 5


class HUD:
    """A GUI that renders over top of the in-game view."""

    api: scripts.GameAPI

    def __init__(self, api: scripts.GameAPI):
        self.api = api

    def set_api(self, api: scripts.GameAPI) -> None:
        """Sets the API for this GUI."""
        self.api = api

    def set_manager(self, manager: gui.UIManager) -> None:
        """Sets the UI manager for this GUI."""

    def draw(self) -> None:
        """Renders the overlay."""
        state = self.api.player_state

        current_hp = state["hp"]
        max_hp = state["max_hp"]

        hp_width = current_hp / max_hp * (HP_WIDTH - HP_BORDER * 2)

        center_offset = (HP_WIDTH - hp_width - HP_BORDER) / 2 - 1

        arcade.draw_rectangle_outline(
            center_x=HP_X,
            center_y=HP_Y,
            width=HP_WIDTH,
            height=HP_HEIGHT,
            color=HP_BORDER_COLOR,
            border_width=HP_BORDER,
        )
        arcade.draw_rectangle_filled(
            center_x=HP_X - center_offset,
            center_y=HP_Y,
            width=hp_width,
            height=HP_HEIGHT - HP_BORDER * 2,
            color=HP_BAR_COLOR,
        )

        text = f"{round(current_hp)}/{round(max_hp)}"

        arcade.draw_text(
            text=text,
            start_x=HP_X + HP_WIDTH / 2 + HP_TEXT_MARGIN,
            start_y=HP_Y - HP_HEIGHT / 2 + HP_BORDER * 2,
        )
