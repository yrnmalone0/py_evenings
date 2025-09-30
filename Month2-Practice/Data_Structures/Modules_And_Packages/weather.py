# Exploring Python Libraries

#Use the requests library to fetch weather information from an online weather API (e.g., weatherapi.
#Install the requests library using pip if it’s not already installed pip install requests.
#Write a Python script weather.py to use the requests.get method to fetch weather data from the API.
#Print out relevant weather information (e.g., temperature, weather description) from the API response.

import requests

# Define API endpoint
url = "http://api.weatherapi.com/v1"

# Make GET Request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON Data
    data = response.json()
    print("Data fetched successfully:", data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")