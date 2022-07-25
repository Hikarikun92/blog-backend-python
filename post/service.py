from post.models import Post
from post.repository import Repository


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    def find_by_user_id(self, user_id: int) -> list[Post]:
        return self.repository.find_by_user_id(user_id)

    def find_by_id(self, id: int) -> Post | None:
        return self.repository.find_by_id(id)

    def create(self, post: Post) -> int:
        return self.repository.create(post)
