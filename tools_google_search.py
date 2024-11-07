import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GoogleSearchTool:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    def search(self, query):
        url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.search_engine_id}&q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return f"Error: {response.status_code}"