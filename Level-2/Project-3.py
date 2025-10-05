# Weather App Using API 

import requests

def get_weather(city):
    API_KEY = "52fd660671d9cfb9c620265b398e58cd"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather = data['weather'][0]['description']
        
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather: {weather}")
    else:
        print("❌ City not found or error fetching data!")

city = input("Enter city name: ")
get_weather(city)