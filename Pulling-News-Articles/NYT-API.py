""" This API is also not too great. It is limited to one media source NYT, which means that there are not a whole lot of articles in a small time frame for 
a given stock. Further, there is such little resources available for this. I also couldn't even figure out if there was a subscription required,
so I think it's poor UI/UX with a small community.
"""


import requests

# Replace 'YOUR_API_KEY' with your actual New York Times API key
api_key = 'jGoQc9ZpDv4KJqDJZzylhu46DoMvYLWj'

# Example search query parameters
search_query = 'Apple'  # Example search query for articles related to Apple
begin_date = '20230101'  # Start date for articles in YYYYMMDD format (e.g., January 1, 2023)
end_date = '20231231'    # End date for articles in YYYYMMDD format (e.g., December 31, 2023)

# Example endpoint for article search
url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={search_query}&begin_date={begin_date}&end_date={end_date}&api-key={api_key}"

# Make the API request
response = requests.get(url)


# Make the API request
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    # If the request was successful (status code 200)
    data = response.json()  # Parse the JSON response into a Python dictionary

    # Extract and print the descriptions/snippets of the first few articles
    articles = data.get('response', {}).get('docs', [])
    for article in articles[:5]:
        print(article.get('print_page'))
        print()
else:
    print(f"Request failed with status code {response.status_code}")

