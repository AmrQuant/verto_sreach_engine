import requests

def get_google_results(keywords, api_key, cse_id):
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': keywords,
            'cx': cse_id,
            'key': api_key,
            'num': 10  # Number of results per page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        search_results = response.json()

        results = []
        for item in search_results.get('items', []):
            results.append({
                'title': item.get('title'),
                'link': item.get('link')
            })
        return results
    except requests.RequestException as e:
        print(f'Error making request to Google API: {e}')
        return []

def aggregate_results(keywords):
    google_api_key = 'AIzaSyB5nPDAlt48IHxI6-iuQUyXirTf6a6g5YE'
    google_cse_id = 'b4e5640e0b13a4ce1'

    results = get_google_results(keywords, google_api_key, google_cse_id)
    return results

if __name__ == "__main__":
    keywords = input("Enter search keywords: ")
    combined_results = aggregate_results(keywords)
    for result in combined_results:
        print(result)
