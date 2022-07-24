from user.models import User


class UserReadDto:
    def __init__(self, id: int, username: str):
        self.id = id
        self.username = username

    def __eq__(self, other) -> bool:
        if not isinstance(other, UserReadDto):
            return False

        return self.id == other.id and self.username == other.username


def to_read_dto(user: User) -> UserReadDto:
    return UserReadDto(user.id, user.username)
