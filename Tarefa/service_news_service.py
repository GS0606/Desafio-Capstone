# service_news_service.py
from storage_news_storage import fetch_news

class service_news_service:
    @staticmethod
    def get_news_service(theme, start_time, end_time, page):
        data = fetch_news(theme, start_time, end_time, page)
        return data
