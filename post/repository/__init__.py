from post.models import Post

from post.repository.models import PostModel


# TODO
class Repository:
    def find_by_user_id(self, user_id: int) -> list[Post]:
        post_models: list[PostModel] = PostModel.query.filter(PostModel.user_id == user_id)
        print(post_models)
        pass

    def find_by_id(self, id: int) -> Post | None:
        pass

    def create(self, post: Post) -> int:
        pass
