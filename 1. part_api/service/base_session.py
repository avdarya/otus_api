import requests


class BaseSession:

    def get(self, url: str, params: dict = None, headers: dict = None) -> dict | list[dict]:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, url: str, body: dict, headers: dict = None) -> dict:
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
        return response.json()

    def patch(self, url: str, body: dict, headers: dict = None):
        response = requests.patch(url, json=body, headers=headers)
        response.raise_for_status()
        return response.json()