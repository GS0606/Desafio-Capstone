# storage_news_storage.py
import requests
import json

def fetch_news(theme, start_time, end_time, page):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

    url = f"https://www.bloomberg.com/markets2/api/search?query={theme}&page={page}&sort=time:desc&resource_subtypes=Article&start_time={start_time}&end_time={end_time}"
    response = session.get(url)

    data = response.json()

    # Exemplo de salvamento dos dados em um arquivo JSON
    with open('response.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return data
