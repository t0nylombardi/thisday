from providers.news_provider import NewsProvider
from models.news import News


class NewsService:
    def __init__(self, provider=None):
        self.provider = provider or NewsProvider()

    def get_top_headlines(self):
        data = self.provider.fetch()

        if data is None:
            return []

        if not isinstance(data, dict):
            return []

        if data.get("status") != "ok":
            return []

        articles = data.get("articles", [])
        news_list = []

        for article in articles:
            title = (article.get("title") or "").strip()
            description = (article.get("description") or "").strip()
            url = (article.get("url") or "").strip()
            source = (article.get("source", {}).get("name") or "").strip()

            news_list.append(
                News(
                    title=title,
                    description=description,
                    url=url,
                    source=source,
                )
            )

        return news_list
