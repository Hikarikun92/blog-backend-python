from collections.abc import Callable
from unittest import TestCase

from user.models import User
from user.rest.dtos import UserReadDto, to_read_dto
from user.rest.facade import Facade
from user.service import Service


class MockService(Service):
    def __init__(self, find_all_impl: Callable[[], list[User]]):
        self.find_all_impl = find_all_impl

    def find_all(self) -> list[User]:
        return self.find_all_impl()


class TestFacade(TestCase):
    def test_find_all(self):
        entities: list[User] = [
            User(id=1, username='Administrator'),
            User(id=2, username='John Doe'),
            User(id=3, username='Mary Doe')
        ]
        service = MockService(lambda: entities)
        facade = Facade(service)

        dtos: list[UserReadDto] = facade.find_all()
        self.assertEqual(len(dtos), len(entities))

        for index, entity in enumerate(entities):
            self.assertEqual(dtos[index], to_read_dto(entity))
