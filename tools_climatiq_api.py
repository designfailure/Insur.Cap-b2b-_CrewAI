import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ClimatiqAPITool:
    def __init__(self):
        self.api_key = os.getenv("CLIMATIQ_API_KEY")

    def estimate_emissions(self, industry, company_size):
        url = "https://beta3.api.climatiq.io/estimate"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "emission_factor": {
                "activity_id": "commercial_and_institutional-type_of_building-office",
                "data_version": "^1"
            },
            "parameters": {
                "area": company_size,
                "area_unit": "ft2"
            }
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"