import json
import pytest
from typing import Generator
from pathlib import Path
from openbrewerydb.brewery_client import BreweryClient


base_url_brewery = 'https://api.openbrewerydb.org'

@pytest.fixture(scope='session')
def brewery_client() -> BreweryClient:
    return BreweryClient(base_url_brewery)

@pytest.fixture
def expected_brewery(brewery_id: str) -> Generator[dict, None, None]:
    example_brewery_path = Path(__file__).parent / f'{brewery_id}.json'
    with open(example_brewery_path, 'r') as f:
        example_brewery = json.load(f)
        yield example_brewery