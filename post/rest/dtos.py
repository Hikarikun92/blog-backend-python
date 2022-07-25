from comment.rest.dtos import CommentReadDto
from user.rest.dtos import UserReadDto


class PostByUserDto:
    def __init__(self, id: int, title: str, body: str, published_date: str):
        self.id = id
        self.title = title
        self.body = body
        self.published_date = published_date


class PostByIdDto:
    def __init__(self, id: int, title: str, body: str, published_date: str, user: UserReadDto,
                 comments: list[CommentReadDto]):
        self.id = id
        self.title = title
        self.body = body
        self.published_date = published_date
        self.user = user
        self.comments = comments


class CreatePostDto:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body
