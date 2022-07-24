from flask import Flask, jsonify

from user.repository import Repository as UserRepository
from user.rest.dtos import UserReadDto
from user.rest.facade import Facade as UserFacade
from user.service import Service as UserService

app = Flask(__name__)

user_repository = UserRepository()
user_service = UserService(user_repository)
user_facade = UserFacade(user_service)


@app.route('/users', methods=['GET'])
def find_all_users():
    dtos: list[UserReadDto] = user_facade.find_all()
    return jsonify([{'id': dto.id, 'username': dto.username} for dto in dtos])


if __name__ == '__main__':
    app.run()
