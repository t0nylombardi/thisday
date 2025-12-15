from models.history_item import HistoryItem


class HistoryService:
    def today(self):
        # Fake test data for now
        return [
            HistoryItem(
                "2023",
                "The JWT ..",
            ),
        ]
