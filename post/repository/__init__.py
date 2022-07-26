from flask_sqlalchemy import SQLAlchemy

from comment.models import Comment
from database import PostModel, UserModel, CommentModel
from post.models import Post
from user.models import User


# TODO
class Repository:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def find_by_user_id(self, user_id: int) -> list[Post]:
        post_models: list[PostModel] = PostModel.query.filter(PostModel.user_id == user_id).all()
        if len(post_models) == 0:
            return []

        user_model: UserModel = post_models[0].user
        user = User(user_model.id, user_model.username)

        return [Post(model.id, model.title, model.body, model.published_date, user) for model in post_models]

    def find_by_id(self, id: int) -> Post | None:
        query = PostModel.query.join(PostModel.user).outerjoin(PostModel.comments).filter(
            PostModel.id == id).order_by(CommentModel.published_date)
        post_model: PostModel | None = query.scalar()

        if post_model is None:
            return None

        # Cache to avoid creating multiple already converted users
        user_cache: dict[int, User] = {}

        comments: list[Comment] = []

        for comment_model in post_model.comments:
            if comment_model.user_id in user_cache:
                user: User = user_cache[comment_model.user_id]
            else:
                user: User = User(comment_model.user_id, comment_model.user.username)
                user_cache[comment_model.user_id] = user

            comments.append(
                Comment(comment_model.id, comment_model.title, comment_model.body, comment_model.published_date, user))

        if post_model.user_id in user_cache:
            user: User = user_cache[post_model.user_id]
        else:
            user: User = User(post_model.user_id, post_model.user.username)
            user_cache[post_model.user_id] = user

        return Post(post_model.id, post_model.title, post_model.body, post_model.published_date, user, comments)

    def create(self, post: Post) -> int:
        post_model = PostModel()
        post_model.title = post.title
        post_model.body = post.body
        post_model.published_date = post.published_date
        post_model.user_id = post.user.id

        self.db.session.add(post_model)
        self.db.session.commit()

        return post_model.id
