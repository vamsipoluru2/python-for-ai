
# What is an API?
# An API (Application Programming Interface) is like a waiter at a restaurant. You tell it what you want, and it brings you the data.
# But APIs do more than just fetch information. They’re the bridges that connect your code to other systems. With APIs, you can:
# Pull customer data from your CRM (Salesforce, HubSpot)
# Get order information from Shopify or WooCommerce
# Send messages through Slack or email services

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

# EXTRACT daata from response
data['current']['temperature_2m']

temperature = data['current']['temperature_2m']
print(f"Temperature in Paris: {temperature}°C")
# Output: Temperature in Paris: 20.0°C


import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")

# How it works
# You send a request to the API’s URL with parameters (like coordinates)
# The API processes your request and finds the data
# You receive JSON data back with the information
# You extract the specific parts you need

#changes to oopapi.py