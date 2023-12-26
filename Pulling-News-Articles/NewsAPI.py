""" I really like this API. I think the titles and descriptions could be really helpful for ML purposes. However, the free version only allows for data to be pulled
up to one month back. And it is very expensive to upgrade.
"""

from datetime import datetime, timedelta
from newsapi import NewsApiClient

# Initialize NewsApiClient with your API key
api_key = ''  # Replace with your actual NewsAPI key
newsapi = NewsApiClient(api_key=api_key)


# Calculate dates for the last year
today = datetime.now()
one_year_ago = today - timedelta(days=365)

# Define the query parameters for Apple within the last year
query = 'Apple Inc. OR AAPL'
from_date = one_year_ago.strftime('%Y-%m-%d')
to_date = today.strftime('%Y-%m-%d')

# Make a request to get articles about Apple within the last year
recent_articles = newsapi.get_everything(q=query, language='en', sort_by='publishedAt', from_param=from_date, to=to_date)

# Access and print the articles related to Apple within the last year
if 'articles' in recent_articles:
    apple_articles = [article for article in recent_articles['articles'] if 'apple' in article['title'].lower()]
    apple_articles = apple_articles[:10]  # Limit to the first ten articles
    for article in apple_articles:
        title = article['title']
        description = article['description']
        published_date = article['publishedAt'][:10]  # Extracting only the date part
        print(f"Published Date: {published_date}\nTitle: {title}\nDescription: {description}\n")
else:
    print("No articles found in the response")
