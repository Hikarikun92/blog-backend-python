from user.models import User
from user.rest.dtos import UserReadDto, to_read_dto
from user.service import Service


class Facade:
    def __init__(self, service: Service):
        self.service = service

    def find_all(self) -> list[UserReadDto]:
        entities: list[User] = self.service.find_all()

        return [to_read_dto(entity) for entity in entities]
