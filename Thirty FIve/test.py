from urllib import response
import requests
rijin = requests.get("https://console.twilio.com/us1/develop/phone-numbers/manage/verified")
print(rijin.text)