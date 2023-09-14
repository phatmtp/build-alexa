import requests
import json

# Define the API key and base URL for OpenWeatherMap
api_key = 'YOUR_API_KEY'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

# Store user's city
city = 'London'

# Build the complete URL with parameters
complete_url = base_url + 'q=' + city + '&appid=' + api_key

# Send a GET request to the API
response = requests.get(complete_url)

# Check the response status code
if response.status_code == 200:
  # The request was successful, so parse the response
  data = response.json()

  # Print all the data in the JSON object
  for key, value in data.items():
    print(f"{key}: {value}")

else:
  # The request was unsuccessful, so print an error message
  print(f"Error: {response.status_code}.")
