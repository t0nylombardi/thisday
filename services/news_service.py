class NewsService:
    def __init__(self):
        pass

    def latest_headlines(self, category=None):
        return [
            NewsItem(title="Breaking News: Something Happened!"),
            NewsItem(title="Latest Updates: More News Here"),
            NewsItem(title="In Case You Missed It: News Recap"),
        ]  # Returns a list of NewsItem models

    def news_item_details(self, item_id):
        return NewsItem(
            title="Detailed News Item",
            content="This is the full content of the news item.",
        )  # Returns a NewsItem model with full details


class NewsItem:
    def __init__(self, title, content=""):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"NewsItem(title={self.title})"
