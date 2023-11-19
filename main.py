import requests

def get_google_results(query, api_key):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx=017576662512468239146:omuauf_lfve&q={query}"
    response = requests.get(url)
    results = response.json()
    search_results = []

    if 'items' in results:
        for item in results['items']:
            title = item['title']
            link = item['link']
            search_results.append({
                'title': title,
                'link': link,
                'search_engine': 'Google'
            })

    return search_results