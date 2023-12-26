"""I don't like this for what I want to do. It's a good API to know. But the title and the snippets here are not very descriptive for ML purposes.
Also, there will not be a straightforward way to pull the full articles as each article will lead to a website, where we can web scrap, but
it's not like it will even be remotely close in format each time.
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
