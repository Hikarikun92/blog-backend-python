from post.models import Post


# TODO
class Repository:
    def find_by_user_id(self, user_id: int) -> list[Post]:
        pass

    def find_by_id(self, id: int) -> Post | None:
        pass

    def create(self, post: Post) -> int:
        pass
