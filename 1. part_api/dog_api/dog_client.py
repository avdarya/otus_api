from service.base_session import BaseSession


class DogClient(BaseSession):

    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_images_by_breed(self, breed: str) -> dict:
        return self.get(f'{self.base_url}/api/breed/{breed}/images')

    def get_images_by_sub_breed(self, breed: str, sub_breed: str) -> dict:
        return self.get(f'{self.base_url}/api/breed/{breed}/{sub_breed}/images')

    def get_random_image_by_breed(self, breed: str) -> dict:
        return self.get(f'{self.base_url}/api/breed/{breed}/images/random')

    def get_random_images_by_breed(self, breed: str, count: int) -> dict:
        return self.get(f'{self.base_url}/api/breed/{breed}/images/random/{count}')

    def get_sub_breeds(self, breed: str) -> dict:
        return self.get(f'{self.base_url}/api/breed/{breed}/list')