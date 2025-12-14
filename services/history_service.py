from models.history_item import HistoryItem


class HistoryService:
    def today(self):
        # Fake test data for now
        return [
            HistoryItem(
                "2023",
                "The James Webb telescope discovered its first exoplanet atmosphere.",
            ),
            HistoryItem(
                "2022", "NASA completed the first fully autonomous Moon lander test."
            ),
            HistoryItem(
                "2021", "Major breakthrough achieved in fusion energy research."
            ),
            HistoryItem(
                "2020", "Scientists confirmed the earliest known human drawing."
            ),
        ]
