from tkinter import W
import requests
# import os
from twilio.rest import Client
account_sid = "AC5cc44874baed2552e4330daf6712b79b"
auth_token =  "3f507481461f868415a00d7d0debffb7"

api_key = "f401eab24946426296ca68622b6aad87"
url = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat" : 38.937111,
    "lon" : -77.413231,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}
response = requests.get(url=url, params=parameters)
response.status_code
weather_data = response.json()
weather_required =  weather_data["hourly"][:12]
is_raining = False
# print(weather_required)
for hours in weather_required:
    weather_code = hours["weather"][0]["id"]
    # print(weather_code)
    if int(weather_code) < 700:
        is_raining = True
        # print("Bring umbrella")
# print(weather_data["hourly"][0]["weather"][0])

if is_raining :
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="I am awesome",
                     from_='+19854127844',
                     to='+91 95620   02393'
                 )
print(message.status)

