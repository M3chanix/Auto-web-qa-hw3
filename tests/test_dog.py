import requests
import pytest

def test_get_random():
    url = 'https://dog.ceo/api/breed/vizsla/images/random'
    r = requests.get(url)
    assert r.json()['status'] == 'success' and r.status_code == 200

def test_unvalid_breed(breed='varg'):
    url = 'https://dog.ceo/api/breed/{}/images/random'.format(breed)
    r = requests.get(url)
    assert r.json()['status'] == 'error' and r.status_code == 404

@pytest.mark.parametrize('breed', ['vizsla', 'malinois', 'basenji'])
def test_breed(breed):
    url = 'https://dog.ceo/api/breed/{}/images/random'.format(breed)
    r = requests.get(url)
    assert r.json()['status'] == 'success' and r.status_code == 200

def test_breed_list():
    url = 'https://dog.ceo/api/breeds/list/all'
    r = requests.get(url)
    assert r.json()['message'] != []

def test_subbreeds(breed='hound'):
    url = 'https://dog.ceo/api/breed/{}/list'.format(breed)
    suburl = 'https://dog.ceo/api/breed/{breed}/{subbreed}/images/random'
    r = requests.get(url)
    for subbreed in r.json()['message']:
        sub_r = requests.get(suburl.format(breed=breed, subbreed=subbreed))
        assert sub_r.json()['status'] == 'success' and sub_r.status_code == 200

@pytest.mark.parametrize('number', range(1, 51, 5))
def test_number(number):
    url = 'https://dog.ceo/api/breeds/image/random/{}'.format(number)
    r = requests.get(url)
    assert len(r.json()['message']) == number

