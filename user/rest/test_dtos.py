from unittest import TestCase, main

from user.models import User
from user.rest.dtos import to_read_dto


class TestDtos(TestCase):
    def test_to_read_dto(self):
        entity = User(3, 'Some user')
        dto = to_read_dto(entity)

        self.assertEqual(dto.id, entity.id)
        self.assertEqual(dto.username, entity.username)


if __name__ == '__main__':
    main()
