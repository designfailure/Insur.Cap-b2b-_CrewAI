import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAPITool:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")

    def get_weather(self, location):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"