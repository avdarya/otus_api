import pytest

from openbrewerydb.brewery_client import BreweryClient


@pytest.mark.parametrize('brewery_id, ', ['b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'])
def test_get_brewery(expected_brewery: dict, brewery_client: BreweryClient, brewery_id: str):
    brewery = brewery_client.get_by_id(brewery_id)

    assert brewery == expected_brewery

@pytest.mark.parametrize('city', ['Louisville'])
def test_get_by_city(brewery_client: BreweryClient, city: str):
    breweries = brewery_client.get_by_params({'by_city': city})
    city_set = {brewery["city"] for brewery in breweries}
    assert {city} == city_set

@pytest.mark.parametrize('per_page', [4, 2])
def test_per_page(brewery_client: BreweryClient, per_page: int):
    breweries = brewery_client.get_by_params({'per_page': per_page})
    assert len(breweries) == per_page

@pytest.mark.parametrize('query', ['Beer Company', 'Iowa'])
def test_search_query(brewery_client: BreweryClient, query: str):
    breweries = brewery_client.get_by_search_query(query)
    assert len(breweries) > 0
    assert query in str(breweries)

@pytest.mark.parametrize('field, direction, per_page', [
    ('name', 'asc', 10), ('name', 'desc', 10),
    ('city', 'asc', 10), ('city', 'desc', 10),
])
def test_sort_by_one_field(brewery_client: BreweryClient, field: str, direction: str, per_page: int):
    params = {
        'sort': f'{field}:{direction}',
        'per_page': per_page
    }
    breweries = brewery_client.get_by_params(params)
    api_sorted = [brewery[field] for brewery in breweries]
    expected_sorted = sorted(api_sorted, reverse=(direction == 'desc'))
    assert api_sorted == expected_sorted
    assert len(breweries) == per_page
