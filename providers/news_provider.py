import requests
from dotenv import load_dotenv
import os

load_dotenv()


class NewsProvider:
    API_BASE_URL = "https://newsapi.org/v2/top-headlines"
    API_KEY = os.getenv("NEWS_API_KEY")
    COUNTRY = os.getenv("NEWS_COUNTRY", "us")

    def fetch(self):
        try:
            res = requests.get(self.API_BASE_URL, params=self.params())
            res.raise_for_status()
            return res.json()
        except Exception as e:
            print(f"Error fetching news data: {e}")
            return None

    def params(self):
        return {
            "apiKey": self.API_KEY,
            "country": self.COUNTRY,
            "pageSize": 10,
        }
