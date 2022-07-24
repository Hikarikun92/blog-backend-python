from user.models import User
from user.repository import Repository


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    def find_all(self) -> list[User]:
        return self.repository.find_all()
