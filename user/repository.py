from user.models import User, Credentials


# TODO
class Repository:
    def find_all(self) -> list[User]:
        return []

    def find_credentials_by_username(self, username) -> Credentials | None:
        pass
