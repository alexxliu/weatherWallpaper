import requests, json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

base_url = "http://api.openweathermap.org/data/2.5/weather?"

def getWeather(city_name):
        
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        v = x["clouds"]
        current_cloud = v["all"]

        w = x["wind"]
        current_wind = w["speed"]

        y = x["main"]

        current_temperature = y["temp"]

        current_humidity = y["humidity"]

        z = x["weather"]
        weather_description = z[0]["description"]

        return ("Current Windspeed in meters/second: " + str(current_wind) + "\nCurrent Temperature in Kelvins: " + str(current_temperature) + "\nCurrent humidity in percentage: " + str(current_humidity) + "\nCurrent cloudiness in percentage: " + str(current_cloud) + "\nCurrent weather description: " + str(weather_description))
    else:
        return -1
