import requests
from datetime import datetime


MY_LAT = 12.971599
MY_LON = 77.594566
FORMAT= 1
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# data = response.json()["iss_position"]
# print(data)

# lat = response.json()["iss_position"]["latitude"]
# lon = response.json()["iss_position"]["longitude"] 
# location = (lon, lat)
# print(location)
parameters = { "lat" : MY_LAT,
"lng": MY_LON, 
"formatted" : 0

}
response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise= data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)