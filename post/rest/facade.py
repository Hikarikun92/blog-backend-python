from datetime import datetime

from comment.rest.dtos import CommentReadDto
from post.models import Post
from post.rest.dtos import PostByUserDto, PostByIdDto, CreatePostDto
from post.service import Service
from user.models import User
from user.rest.dtos import UserReadDto, to_read_dto
from util import datetime_to_iso


class Facade:
    def __init__(self, service: Service):
        self.service = service

    def find_by_user_id(self, user_id: int) -> list[PostByUserDto]:
        entities: list[Post] = self.service.find_by_user_id(user_id)
        return [self._to_post_by_user_dto(post) for post in entities]

    def _to_post_by_user_dto(self, post: Post) -> PostByUserDto:
        return PostByUserDto(post.id, post.title, post.body, datetime_to_iso(post.published_date))

    def find_by_id(self, id: int) -> PostByIdDto | None:
        return self._to_post_by_id_dto(self.service.find_by_id(id))

    def _to_post_by_id_dto(self, post: Post) -> PostByIdDto | None:
        if post is None:
            return None

        # Cache to avoid creating DTOs of already converted users
        user_cache: dict[int, UserReadDto] = {}

        comments: list[CommentReadDto] = []
        for comment in post.comments:
            if comment.user.id in user_cache:
                user: UserReadDto = user_cache[comment.user.id]
            else:
                user: UserReadDto = to_read_dto(comment.user)
                user_cache[comment.user.id] = user

            comment_dto = CommentReadDto(comment.id, comment.title, comment.body,
                                         datetime_to_iso(comment.published_date), user)
            comments.append(comment_dto)

        if post.user.id in user_cache:
            user = user_cache[post.user.id]
        else:
            user: UserReadDto = to_read_dto(post.user)
            user_cache[post.user.id] = user

        return PostByIdDto(post.id, post.title, post.body, datetime_to_iso(post.published_date), user, comments)

    def create(self, dto: CreatePostDto, user_id: int) -> int:
        # Note: we can set some of these fields to None, they won't be used by the creation method
        post: Post = Post(None, dto.title, dto.body, datetime.now(), User(user_id, None))
        return self.service.create(post)
