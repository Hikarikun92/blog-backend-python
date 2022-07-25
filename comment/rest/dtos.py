from user.rest.dtos import UserReadDto


class CommentReadDto:
    def __init__(self, id: int | None, title: str, body: str, published_date: str, user: UserReadDto):
        self.id = id
        self.title = title
        self.body = body
        self.published_date = published_date
        self.user = user
