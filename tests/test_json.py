from tests.request_methods import post_request, patch_request, \
        get_request, delete_request
import pytest
from hw3.Post import Post


@pytest.fixture
def create_post():
    post_dict = {'id': 46, 'title': 'aut quo modi neque nostrum ducimus',
            'body': 'voluptatem quisquam iste\nvoluptatibus natus officiis facilis dolorem\nquis quas ipsam\nvel et voluptatum in aliquid',
            'userId': 5}
    post = Post(**post_dict)
    return post

def test_post_created(create_post):
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = create_post.dict(exclude={'id'})
    returned_post = post_request(url, payload)
    assert returned_post.status_code == 201

def test_post_updated(create_post):
    create_post.body = 'new post body'
    url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(create_post.id)
    payload = create_post.dict(exclude={'id'})
    returned_post = patch_request(url, payload)
    assert returned_post.status_code == 200

def test_post_getted(create_post):
    url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(create_post.id)
    returned_post = get_request(url).json()
    created_post = create_post.dict()
    for key in created_post:
        assert created_post[key] == returned_post[key]

def test_post_deleted(create_post):
    url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(create_post.id)
    returned_post = delete_request(url)
    assert returned_post.status_code == 200


@pytest.mark.parametrize('resource', ['albums', 'todos', 'posts'])
def test_user_methods(resource, id=1):
    url = 'https://jsonplaceholder.typicode.com/users/{}/{}'.format(id, resource)
    resources = get_request(url)
    assert resources.json() != []

@pytest.mark.parametrize('id', range(1, 10))
def test_post_comments(id):
    url = 'https://jsonplaceholder.typicode.com/posts/{}/comments'.format(id)
    comments = get_request(url)
    assert comments.json() != []
