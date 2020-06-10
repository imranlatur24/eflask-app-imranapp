from flask import *
import json
import requests

cityname = input("Enter your cityname : ") 

    
api_address='https://api.openweathermap.org/data/2.5/weather?appid=3e90723e72e3e77055f8c10dccb120f8&q='
city = cityname
print("city :",city)
url = api_address + city
print("url :",url)
json_data = requests.get(url).json()
print("json_data :",json_data)
formatted_data = json_data['main']['temp']
print("you city temp is :",formatted_data)
