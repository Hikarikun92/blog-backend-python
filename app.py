from http import HTTPStatus

from flask import Flask, jsonify, request, json, abort, Response

from config import load_config_from_environment, Config
from database import db
from post.repository import Repository as PostRepository
from post.rest.dtos import PostByUserDto, PostByIdDto, CreatePostDto
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

db.init_app(app)

user_repository = UserRepository()
user_service = UserService(user_repository)
user_facade = UserFacade(user_service)

post_repository = PostRepository(db)
post_service = PostService(post_repository)
post_facade = PostFacade(post_service)


@app.route('/users', methods=['GET'])
def find_all_users():
    dtos: list[UserReadDto] = user_facade.find_all()
    return jsonify([dto.to_json() for dto in dtos])


@app.route('/users/<int:user_id>/posts', methods=['GET'])
def find_post_by_user_id(user_id: int):
    dtos: list[PostByUserDto] = post_facade.find_by_user_id(user_id)
    return jsonify([dto.to_json() for dto in dtos])


@app.route('/posts', methods=['POST'])
def create_post():
    # TODO validate required data
    record = json.loads(request.data)
    title = record['title'] if 'title' in record else None
    body = record['body'] if 'body' in record else None
    user_id = record['userId'] if 'userId' in record else None # TODO this should be retrieved via the credentials

    dto = CreatePostDto(title, body)
    id:int = post_facade.create(dto, user_id)

    return Response(status=HTTPStatus.CREATED, headers=[('Location', f'/posts/{id}')])


@app.route('/posts/<int:id>', methods=['GET'])
def find_post_by_id(id: int):
    dto: PostByIdDto | None = post_facade.find_by_id(id)
    if dto is None:
        abort(HTTPStatus.NOT_FOUND)

    return jsonify(dto.to_json())


if __name__ == '__main__':
    app.run(host=config.server_address, port=config.server_port)
