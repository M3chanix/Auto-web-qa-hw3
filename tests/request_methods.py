import requests

def request(url, method, payload={}):
    r = method(url, params=payload)
    return r

def post_request(url, payload={}):
    return request(url=url, method=requests.post, payload=payload)

def get_request(url):
    return request(url=url, method=requests.get)

def patch_request(url, payload={}):
    return request(url=url, method=requests.patch, payload=payload)

def delete_request(url):
    return request(url=url, method=requests.delete)

