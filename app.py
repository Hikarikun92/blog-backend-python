from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import load_config_from_environment, Config
from user.repository import Repository as UserRepository
from user.rest.dtos import UserReadDto
from user.rest.facade import Facade as UserFacade
from user.service import Service as UserService

config: Config = load_config_from_environment()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] \
    = f'mysql+pymysql://{config.db_user}:{config.db_password}@{config.db_server}:{config.db_port}/{config.db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

user_repository = UserRepository()
user_service = UserService(user_repository)
user_facade = UserFacade(user_service)


@app.route('/users', methods=['GET'])
def find_all_users():
    dtos: list[UserReadDto] = user_facade.find_all()
    return jsonify([{'id': dto.id, 'username': dto.username} for dto in dtos])


if __name__ == '__main__':
    app.run(host=config.server_address, port=config.server_port)
