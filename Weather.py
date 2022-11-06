import requests

url = "api.openweathermap.org/data/2.5/weather?q=" + user_location + "&appid=" + weather_api_key
user_location = input(str("Where are you at currently"))
#print("Current temperature is " + data["main"]["temp"])