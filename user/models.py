class User:
    def __init__(self, id: int | None, username: str):
        self.id = id
        self.username = username

    def __str__(self):
        return f'User(id={self.id}, username={self.username})'


class Credentials:
    def __init__(self, user: User, password: str, roles: list[str]):
        self.user = user
        self.password = password
        self.roles = roles
