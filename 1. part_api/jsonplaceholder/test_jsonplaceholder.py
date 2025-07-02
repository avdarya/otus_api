import pytest
from jsonplaceholder.jsonplaceholder_client import JsonplaceholderClient

base_url_jsonplaceholder = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='session')
def jsonplaceholder_client() -> JsonplaceholderClient:
    return JsonplaceholderClient(base_url_jsonplaceholder)

@pytest.mark.parametrize('post_id, expected_title, expected_body', [
    (4, 'eum et est occaecati', 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit')
])
def test_get_post_by_id(jsonplaceholder_client: JsonplaceholderClient, post_id: int, expected_title: str, expected_body: str):
    post = jsonplaceholder_client.get_post_by_id(post_id)
    assert post['id'] == post_id
    assert post['title'] == expected_title
    assert post['body'] == expected_body

@pytest.mark.parametrize('user_id, title, body', [(1, 'my title', 'my content')])
def test_add_post(jsonplaceholder_client: JsonplaceholderClient, user_id: int, title: str, body: str):
    payload = {
        'userId': user_id,
        'title': title,
        'body': body
    }
    added_post = jsonplaceholder_client.add_post(payload)
    assert added_post['id'] is not None
    assert isinstance(added_post['id'], int)
    assert added_post['userId'] == user_id
    assert added_post['title'] == title
    assert added_post['body'] == body

@pytest.mark.parametrize('user_id', [3])
def test_get_posts_by_user_id(jsonplaceholder_client: JsonplaceholderClient, user_id: int):
    get_all_posts = jsonplaceholder_client.get_posts()
    expected_posts = [post for post in get_all_posts if post['userId'] == user_id]
    posts = jsonplaceholder_client.get_posts_by_query({'userId': user_id})
    user_post = {post['userId'] for post in posts}
    assert len(expected_posts) == len(posts)
    assert user_post == {user_id}

@pytest.mark.parametrize('post_id, field, new_value', [
    (1, 'userId', 5),
    (1, 'title', 'new title'),
    (1, 'body', 'new content'),
])
def test_update_post_by_field(jsonplaceholder_client: JsonplaceholderClient, post_id: int, field: str, new_value: str | int):
    post_before = jsonplaceholder_client.get_post_by_id(post_id)
    post_before.pop(field)
    payload = {field: new_value}
    updated_post = jsonplaceholder_client.update_post_field(post_id=post_id, body=payload)
    assert updated_post[field] == new_value
    updated_post.pop(field)
    assert updated_post == post_before

@pytest.mark.parametrize('post_id', [1])
def test_get_post_comments(jsonplaceholder_client: JsonplaceholderClient, post_id: int):
    all_comments = jsonplaceholder_client.get_comments()
    expected_comments = [comment for comment in all_comments if comment['postId'] == post_id]
    comments = jsonplaceholder_client.get_post_comments(post_id)
    post_id_comments = {comment['postId'] for comment in comments}
    assert len(expected_comments) == len(comments)
    assert sorted(expected_comments, key=lambda c: c['id']) == sorted(comments, key=lambda c: c['id'])
    assert post_id_comments == {post_id}