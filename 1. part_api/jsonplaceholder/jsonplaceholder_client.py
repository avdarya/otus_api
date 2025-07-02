from service.base_session import BaseSession


class JsonplaceholderClient(BaseSession):

    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_posts(self) -> list[dict]:
        return self.get(f'{self.base_url}/posts')

    def get_comments(self) -> list[dict]:
        return self.get(f'{self.base_url}/comments')

    def get_post_by_id(self, post_id: int) -> dict:
        return self.get(f'{self.base_url}/posts/{post_id}')

    def get_posts_by_query(self, params: dict) -> list[dict]:
        return self.get(
            url=f'{self.base_url}/posts',
            params=params
        )

    def get_post_comments(self, post_id: int) -> list[dict]:
        return self.get(f'{self.base_url}/posts/{post_id}/comments')

    def add_post(self, post: dict) -> dict:
        return self.post(
            url=f'{self.base_url}/posts',
            body=post
        )

    def update_post_field(self, post_id: int, body: dict) -> dict:
        return self.patch(
            url=f'{self.base_url}/posts/{post_id}',
            body=body
        )