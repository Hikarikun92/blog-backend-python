from flask import Flask, jsonify, request, json, abort
from flask_sqlalchemy import SQLAlchemy

from config import load_config_from_environment, Config
from post.repository import Repository as PostRepository
from post.rest.dtos import PostByUserDto, PostByIdDto
from post.rest.facade import Facade as PostFacade
from post.service import Service as PostService
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

post_repository = PostRepository()
post_service = PostService(post_repository)
post_facade = PostFacade(post_service)


@app.route('/users', methods=['GET'])
def find_all_users():
    dtos: list[UserReadDto] = user_facade.find_all()
    return jsonify([{'id': dto.id, 'username': dto.username} for dto in dtos])


@app.route('/users/<int:user_id>/posts', methods=['GET'])
def find_post_by_user_id(user_id: int):
    dtos: list[PostByUserDto] = post_facade.find_by_user_id(user_id)
    return jsonify(
        [{'id': dto.id, 'title': dto.title, 'body': dto.body, 'publishedDate': dto.published_date} for dto in dtos])


@app.route('/posts', methods=['POST'])
def create_post():
    record = json.loads(request.data)
    # TODO
    print(record)


@app.route('/posts/<int:id>', methods=['GET'])
def find_post_by_id(id: int):
    dto: PostByIdDto | None = post_facade.find_by_id(id)
    if dto is None:
        abort(404)

    # TODO
    return None


if __name__ == '__main__':
    app.run(host=config.server_address, port=config.server_port)
