import requests
import pytest


@pytest.mark.parametrize('page',  [1, 2, 3])
@pytest.mark.parametrize('per_page', [1, 5, 9, 12])
def test_per_page(page, per_page, city='chicago'):
    payload = {'by_city': city, 'page': page, 'per_page': per_page}
    url = 'https://api.openbrewerydb.org/breweries'
    r = requests.get(url, params=payload)
    assert len(r.json()) == per_page

@pytest.mark.parametrize(
        'brew_type', 
        ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning'])
def test_type(brew_type, city='chicago'):
    payload = {'by_city': city, 'by_type': brew_type, 'page': 1, 'per_page': 5}
    url = 'https://api.openbrewerydb.org/breweries'
    r = requests.get(url, params=payload)
    for brew in r.json():
        assert brew['brewery_type'] == brew_type

def test_get():
    list_url = 'https://api.openbrewerydb.org/breweries'
    payload = {'page': 1, 'per_page': 10}
    list_req = requests.get(list_url, params=payload)
    for brew in list_req.json():
        get_url = list_url + '/{}'.format(brew['id'])
        get_req = requests.get(get_url)
        assert get_req.json()['name'] == brew['name']

@pytest.mark.parametrize('query', ['beer', 'dog'])
def test_search(query):
    url = 'https://api.openbrewerydb.org/breweries/search'
    payload = {'page': 1, 'per_page': 10, 'query':query}
    r = requests.get(url, params=payload)
    for brew in r.json():
        assert query in brew['name'].lower()

def test_char_postal_code():
    payload = {'by_postal': 'chicago'}
    url = 'https://api.openbrewerydb.org/breweries'
    r = requests.get(url, params=payload)
    assert len(r.json()) == 0

