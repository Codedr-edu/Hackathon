import requests

api_key = "AIzaSyCDdUi1PAgjFyyl5d6Yh9VrMjrr4sHHyDI"
search_engine_id = "31c4a00fe6b2b457b"


def search_query(query):
    url = "https://www.googleapis.com/customsearch/v1"
    p = {
        'q': query,
        'key': api_key,
        'cx': search_engine_id
    }
    respone = requests.get(url, params=p)
    return respone.json()['items']


def search_image(query):
    url = "https://www.googleapis.com/customsearch/v1"
    p = {
        'q': query,
        'key': api_key,
        'cx': search_engine_id,
        'searchType': 'image'
    }
    respone = requests.get(url, params=p)
    return respone.json()['items']
