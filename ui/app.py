from textual.app import App
from textual.screen import Screen


class ThisDayApp(App):
    """Root Textual application for This.Day()."""

    def on_mount(self) -> None:
        self.push_screen(DashboardScreen())


class DashboardScreen(Screen):
    def compose(self):
        yield
