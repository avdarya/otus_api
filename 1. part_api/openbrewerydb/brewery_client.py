from service.base_session import BaseSession


class BreweryClient(BaseSession):

    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_by_id(self, brewery_id: str) -> dict:
        return self.get(url=f'{self.base_url}/v1/breweries/{brewery_id}')

    def get_by_params(self, params: dict) -> dict:
        return self.get(
            url=f'{self.base_url}/v1/breweries',
            params=params
        )

    def get_by_search_query(self, query: str) -> dict:
        return self.get(
            url=f'{self.base_url}/v1/breweries/search',
            params={'query': query}
        )