import requests
import pytest

def test_get_random():
    link = 'https://dog.ceo/api/breed/vizsla/images/random'
    r = requests.get(link)
    assert r.json()['status'] == 'success' and r.status_code == 200

def test_unvalid_breed(breed='varg'):
    link = 'https://dog.ceo/api/breed/{}/images/random'.format(breed)
    r = requests.get(link)
    assert r.json()['status'] == 'error' and r.status_code == 404

@pytest.mark.parametrize('breed', ['vizsla', 'malinois', 'basenji'])
def test_breed(breed):
    link = 'https://dog.ceo/api/breed/{}/images/random'.format(breed)
    r = requests.get(link)
    assert r.json()['status'] == 'success' and r.status_code == 200

def test_breed_list():
    link = 'https://dog.ceo/api/breeds/list/all'
    r = requests.get(link)
    assert r.json()['message'] != []

def test_subbreeds(breed='hound'):
    link = 'https://dog.ceo/api/breed/{}/list'.format(breed)
    sublink = 'https://dog.ceo/api/breed/{breed}/{subbreed}/images/random'
    r = requests.get(link)
    for subbreed in r.json()['message']:
        sub_r = requests.get(sublink.format(breed=breed, subbreed=subbreed))
        assert sub_r.json()['status'] == 'success' and sub_r.status_code == 200

@pytest.mark.parametrize('number', range(1, 51, 5))
def test_number(number):
    link = 'https://dog.ceo/api/breeds/image/random/{}'.format(number)
    r = requests.get(link)
    assert len(r.json()['message']) == number

