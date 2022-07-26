from database import UserModel
from user.models import User, Credentials


class Repository:
    def find_all(self) -> list[User]:
        user_models: list[UserModel] = UserModel.query.all()
        return [User(model.id, model.username) for model in user_models]

    # TODO
    def find_credentials_by_username(self, username) -> Credentials | None:
        pass
