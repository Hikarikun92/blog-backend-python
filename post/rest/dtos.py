from typing import Any

from comment.rest.dtos import CommentReadDto
from user.rest.dtos import UserReadDto


class PostByUserDto:
    def __init__(self, id: int, title: str, body: str, published_date: str):
        self.id = id
        self.title = title
        self.body = body
        self.published_date = published_date

    def to_json(self) -> dict[str, Any]:
        return {'id': self.id, 'title': self.title, 'body': self.body, 'publishedDate': self.published_date}


class PostByIdDto:
    def __init__(self, id: int, title: str, body: str, published_date: str, user: UserReadDto,
                 comments: list[CommentReadDto]):
        self.id = id
        self.title = title
        self.body = body
        self.published_date = published_date
        self.user = user
        self.comments = comments

    def to_json(self) -> dict[str, Any]:
        return {'id': self.id, 'title': self.title, 'body': self.body, 'publishedDate': self.published_date,
                'comments': [c.to_json() for c in self.comments]}


class CreatePostDto:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body
