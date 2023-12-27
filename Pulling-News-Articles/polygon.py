""" I really like this API. I can use data up to two years back, the descriptions are good, its easy to use, and i can do everything i want to for free.
Right now I am just pulling description and time only if the descriptoin containts the word "Apple" or "AAPL". I might sent the whole article to lowercase 
for my inclusion. But, I am doing this becasue there are alot of articles the are not driectly realted to apple, just indriectly realted.
"""

import requests

apikey = ""
ticker = "AAPL"
date = "2023-12-26"
limit = 100

url = f"https://api.polygon.io/v2/reference/news?ticker={ticker}&published_utc={date}&limit={limit}&apiKey={apikey}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    results = data.get("results", [])
    
    for article in results:
        description = str(article.get("description"))
        published_utc = str(article.get("published_utc")).split("T")
        if "Apple" in description or "AAPL" in description:
            print(published_utc[0)
            print(description)
            print()

else:
    print(f"Failed to fetch news. Status code: {response.status_code}")
