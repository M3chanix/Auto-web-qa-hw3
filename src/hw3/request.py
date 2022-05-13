import requests

def test_list_spb():
    payload = {'by_city': 'chicago'}
    link = 'https://api.openbrewerydb.org/breweries'
    r = requests.get(link, params=payload)
    print(r.json())

test_list_spb()
