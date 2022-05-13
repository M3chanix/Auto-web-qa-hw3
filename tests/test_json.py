import requests
import pytest
from hw3.Post import Post
from hw3.Comment import Comment


# Поддерживаются все основные методы по работе с ресурсами - post, get, patch, delete
# можно организовать фикстуры с предварительным созданием тестовых сущностей
@pytest.fixture
def create_post():
    post_dict = {'title': 'a new post title', 'body': 'new post spawned', 'userId': 1}
    post = Post(**post_dict)
    return post

def send_post(post):
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = post.dict()
    r = requests.post(url, params=payload)

def get_post(post):
    url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(post.id)
    r = requests.get(url)
    my_post = post.dict()
    portal_post = r.json()
    return(my_post, portal_post)

