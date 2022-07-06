import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+19854127844"
VERIFIED_NUMBER = "+91 95620 02393"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "2FTA7179N4IBQ7Y3" 
NEWS_API_KEY = "a9a8c122670d46be99bd1eb8c9f1fe78"
ACCOUNT_SID = "AC5cc44874baed2552e4330daf6712b79b"
AUTH_TOKEN = "3f507481461f868415a00d7d0debffb7"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_URL, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


    
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "searchIn": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_URL, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)


    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )