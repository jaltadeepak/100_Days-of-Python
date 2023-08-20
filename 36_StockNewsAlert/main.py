STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alphavantage_api_key = "[Your key]"
INCREASE_SIGN = "🔺"
DECREASE_SIGN = "🔻"

import requests
import datetime as dt
from twilio.rest import Client

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 2% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": alphavantage_api_key
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
yesterday_date = data['Meta Data']['3. Last Refreshed']
close_yesterday = data['Time Series (Daily)'][yesterday_date]['4. close']

day_before_date_dtobject = dt.datetime.strptime(yesterday_date, f"%Y-%m-%d") - dt.timedelta(days=1)
day_before_date = day_before_date_dtobject.strftime(f"%Y-%m-%d")
close_day_before = data['Time Series (Daily)'][day_before_date]['4. close']

change_perc = ((float(close_yesterday) - float(close_day_before))*100)/float(close_day_before)

if  abs(change_perc)>=2:
    percentage_change = round(abs(change_perc))
    if change_perc>=2:
        change_sign = INCREASE_SIGN
    else:
        change_sign = DECREASE_SIGN

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    newsapi_url = "https://newsapi.org/v2/everything"
    newsapi_api_key = "[Your key]"
    parameters = {
        "q": COMPANY_NAME,
        "from": yesterday_date,
        "sortBy": "popularity",
        "apikey": newsapi_api_key
    }
    response = requests.get(url=newsapi_url, params=parameters)
    response.raise_for_status()
    news_data = response.json()
    article_list = news_data['articles'][:3]

    for article in article_list:
        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number. 
        twilio_account_sid = "AC55a62df58eef9ea262650a471556747a"
        twilio_auth_token = "[Your token]"
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            body=f"{STOCK}: {change_sign}{percentage_change}%\nHeadline:{article['title']}\nBrief:{article['description']}",
            from_="+17622475889",
            to="+919166950838",
        )
        print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

