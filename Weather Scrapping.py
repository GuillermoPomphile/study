import json
import urllib.request

# API from Openweather.com
key = "58f2c87f1403e04bd64695326a85f33a"

# Coordinates of Bern, Address:Bolligenstrasse XX
latitude = 46.953819
longitude = 7.465260

language = "de"  # de for German, en for English

response = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}@lang{language}')

j = json.load(response)

print(j["weather"]["description"])
