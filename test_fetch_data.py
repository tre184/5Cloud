import requests
from datetime import datetime, timedelta

def fetch_data():
    response = requests.get("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/sites-disposant-du-service-paris-wi-fi/records?limit=20")
    with open('paris_wifi.csv', 'w') as file:
        file.write(response.text)

if __name__ == "__main__":
    fetch_data()
    print("Data fetched and saved to paris_wifi.csv")
