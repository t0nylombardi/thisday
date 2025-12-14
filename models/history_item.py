class HistoryItem:
    def __init__(self, year: str, event: str):
        self.year = year
        self.event = event

    def __repr__(self):
        return f"HistoryItem(year={self.year}, event={self.event})"
