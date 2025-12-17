from textual.app import App
from textual.widgets import Static


class SmokeTest(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+c", "quit", "Quit"),
    ]

    def compose(self):
        yield Static("Textual is alive 🚀\nPress Q to quit")

    def action_quit(self):
        self.exit()


if __name__ == "__main__":
    SmokeTest().run()
