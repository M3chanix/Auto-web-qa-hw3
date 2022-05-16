import pytest
import requests

@pytest.fixture
def cmdopt(request):
    url = request.config.getoption('--url') 
    status_code = request.config.getoption('--status_code')
    return (url, status_code)

def test_url_code(cmdopt):
    url, expected_code = cmdopt
    r = requests.get(url)
    print(r.status_code)
    assert r.status_code == int(expected_code)

