import requests
from datetime import *
from twilio.rest import Client
# ------------------- Global Variables ----------------------- #
STOCK = "TSLA"
STOCK_API = "ORLPZL1BPRENDFFFSDGGSDCV33KB"
NEWS_API = "f6be540d30c84432b97857dfsdghhcddb64a3afff"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "AC4e2dd445dsdfsdf7e0ea51c388251fsdf4f2b654dgsdfgbece"
auth_token = "76f0a88hfh8182cb0dbb8dadsfdsfaddh615522aa2e29e"
symbol = ""
# ------------------- API Parameters ----------------------- #
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API
}
parameters_news = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API,
    "pageSize": 3,
    "sortBy": "popularity",
    "language": "en"
}

# ------------------- Datetime ----------------------- #
today = date.today()
new_time = timedelta
yesterday = today - new_time(days=1)
day_before = today - new_time(days=2)

# ------------------- Stock API REQUEST ----------------------- #
stock_request = requests.get(url=STOCK_ENDPOINT, params=parameters)
stock_request.raise_for_status()
data = stock_request.json()
yesterday_stock = data['Time Series (Daily)'][f"{yesterday}"]['4. close']
day_before_stock = data['Time Series (Daily)'][f"{day_before}"]['4. close']

# ------------------- Stock Percentages ----------------------- #
the_difference = float(yesterday_stock) - float(day_before_stock)
real_percentage = round((the_difference*100)/float(yesterday_stock), 4)
five_percentage = round((5*float(yesterday_stock))/100, 4)

# ------------------- Stock Up or Down by 5% get News ----------------------- #
list_of_news = []
if real_percentage > five_percentage or real_percentage < five_percentage:
    news_request = requests.get(NEWS_ENDPOINT, params=parameters_news)
    news_request.raise_for_status()
    news_data = news_request.json()
    for news in range(3):
        news_title = news_data['articles'][news]['title']
        list_of_news.append(news_title)
        news_description = news_data['articles'][news]['description']
        list_of_news.append(news_description)

if real_percentage > five_percentage:
    symbol = "☝"
elif real_percentage < five_percentage:
    symbol = "☟"

# ------------------- Send SMS with stock and news ----------------------- #

client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+52 55 5656 5656",
    from_="+155603568445654",
    body=f"TSLA: {symbol}{real_percentage}%\n\nHeadline:{list_of_news[0]}\n\nBrief:{list_of_news[1]}"
)
message_2 = client.messages.create(
    to="+52 55 5656 5656",
    from_="+155603568445654",
    body=f"TSLA: {symbol}{real_percentage}%\n\nHeadline:{list_of_news[2]}\n\nBrief:{list_of_news[3]}"
)
message_3 = client.messages.create(
    to="+52 55 5656 5656",
    from_="+155603568445654",
    body=f"TSLA: {symbol}{real_percentage}%\n\nHeadline:{list_of_news[4]}\n\nBrief:{list_of_news[5]}"
)
