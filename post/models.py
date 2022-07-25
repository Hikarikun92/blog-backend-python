from datetime import datetime

from comment.models import Comment
from user.models import User


class Post:
    def __init__(self, id: int | None, title: str, body: str, published_date: datetime, user: User,
                 comments: list[Comment] | None = None):
        self.id = id
        self.title = title
        self.body = body
        self.published_date = published_date
        self.user = user
        self.comments = comments
