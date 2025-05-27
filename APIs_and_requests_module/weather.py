import requests
# Note: Sign up at https://openweathermap.org to get a free API key
api_key = "9f7fd90d84f299f577bf80dcec5329cb"  # Replace with your actual key
city = "Islamabad"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
if response.ok:
    weather_data = response.json()
    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Conditions: {weather_data['weather'][0]['description']}")
else:
    print("Error fetching weather data")