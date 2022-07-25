from datetime import datetime

from user.models import User


class Comment:
    def __init__(self, id: int | None, title: str, body: str, published_date: datetime, user: User):
        self.id = id
        self.title = title
        self.body = body
        self.published_date = published_date
        self.user = user
