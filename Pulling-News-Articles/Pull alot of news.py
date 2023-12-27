""" This is the code I am using for my sentiment analysis project. This code is going to take a really long time to down load. I estimite about 19*3*52*2 /5 min = 19.76 hours.
We have 19 tickers, 2 years of data (52*2), and we check the news three times each week, but we can make 5 calls a week. So this will take a lot of time. We also add a check
to see if we have exceed our call limit for the minute, i so just wait an additinal minute. Since it has been running i have only seen this happen one time. Im not realy sure why
because if we make 5 back to back calls we wait a total of 60 seconds plus the time to do everything else
"""


from datetime import datetime, timedelta
import pandas as pd
import requests
import time

apikey = ""
limit = 100
stock_tickers = [
    ("aapl", "apple"),
    ("msft", "microsoft"),
    ("googl", "google"),
    ("meta", "meta"),
    ("pfe", "pfizer"),
    ("jnj", "johnson & johnson"),
    ("mrna", "moderna"),
    ("gild", "gilead sciences"),
    ("jpm", "jpmorgan chase"),
    ("gs", "goldman sachs"),
    ("bac", "bank of america"),
    ("c", "citi"),
    ("amzn", "amazon"),
    ("tsla", "tesla"),
    ("hd", "home depot"),
    ("nke", "nike"),
    ("xom", "exxonmobil"),
    ("cvx", "chevron"),
    ("bp", "bp")
]

df = pd.DataFrame(columns=['date', 'ticker', 'description'])
df_indx = 1

def news_download(tick_tup,date):
    global df_indx
    ticker = tick_tup[0]
    company = tick_tup[1]
    url = f"https://api.polygon.io/v2/reference/news?ticker={ticker.upper()}&published_utc={date}&limit={limit}&apiKey={apikey}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        
        for article in results:
            description = str(article.get("description") or "").lower()
            published_utc = str(article.get("published_utc")).split("T")[0]
            if ticker in description or company in description:
                df.loc[df_indx,"date"]        = published_utc
                df.loc[df_indx,"ticker"]      = ticker
                df.loc[df_indx,"description"] = description
                df_indx += 1
                return True
    elif response.status_code==429: time.sleep(60)
    else: print(f"failed on status code: {response.status_code}")
    return False

for i in range(len(stock_tickers)):
    current_date = datetime.now()
    two_years_ago = current_date - timedelta(days=365 * 2)
    current = two_years_ago

    while current <= current_date:
        print(f"{current}, {stock_tickers[i][0]}")
        if current.weekday() in [0, 2, 4] and news_download(stock_tickers[i],current.strftime("%Y-%m-%d")):
            time.sleep(12)
            print("Downloaded")
        current += timedelta(days=1)  # Move to the next day
    df.to_csv("raw_news_data.csv",index=False)
