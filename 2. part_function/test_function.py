import requests


def test_check_status_code(url: str, status_code: str):
    response = requests.get(url)
    assert response.status_code == int(status_code)
