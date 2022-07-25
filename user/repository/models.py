from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)

    def __init__(self, id: int | None, username: str):
        self.id = id
        self.username = username
