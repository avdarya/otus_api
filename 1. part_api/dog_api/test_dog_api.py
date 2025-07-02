import pytest
from dog_api.dog_client import DogClient


base_url_dog_api = 'https://dog.ceo'

@pytest.fixture(scope='session')
def dog_client() -> DogClient:
    return DogClient(base_url_dog_api)

@pytest.mark.parametrize('breed', ['briard'])
def test_get_images_by_breed(dog_client: DogClient, breed: str):
    result = dog_client.get_images_by_breed(breed)
    assert result['status'] == 'success'
    assert isinstance(result['message'], list)
    for link in result['message']:
        assert link.startswith('https://images.dog.ceo/breeds')
        assert breed in link

@pytest.mark.parametrize('breed', ['briard'])
def test_get_random_image_by_breed(dog_client: DogClient, breed: str):
    result = dog_client.get_random_image_by_breed(breed)
    assert result['status'] == 'success'
    assert isinstance(result['message'], str)
    assert result['message'].startswith('https://images.dog.ceo/breeds')
    assert breed in result['message']


@pytest.mark.parametrize('breed, count', [('spaniel', 2)])
def test_get_random_images_by_breed(dog_client: DogClient, breed: str, count: int):
    result = dog_client.get_random_images_by_breed(breed=breed, count=count)
    assert result['status'] == 'success'
    assert isinstance(result['message'], list)
    for link in result['message']:
        assert link.startswith('https://images.dog.ceo/breeds')
        assert breed in link
    assert len(result['message']) == count

@pytest.mark.parametrize('breed, expected_sub_breeds', [
    ('spaniel', ["blenheim", "brittany", "cocker", "irish", "japanese", "sussex", "welsh"])
])
def test_sub_breed_list(dog_client: DogClient, breed: str, expected_sub_breeds: list[str]):
    result = dog_client.get_sub_breeds(breed)
    expected_count = len(expected_sub_breeds)
    assert result['status'] == 'success'
    assert isinstance(result['message'], list)
    assert len(result['message']) == expected_count
    assert set(result['message']) == set(expected_sub_breeds)

@pytest.mark.parametrize('breed, sub_breed', [('mastiff', 'english')])
def test_get_images_by_sub_breed(dog_client: DogClient, breed: str, sub_breed:str):
    result = dog_client.get_images_by_sub_breed(breed=breed, sub_breed=sub_breed)
    assert result['status'] == 'success'
    assert isinstance(result['message'], list)
    for link in result['message']:
        assert link.startswith('https://images.dog.ceo/breeds')
        assert breed in link
        assert sub_breed in link