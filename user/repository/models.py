from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)

    def __init__(self, id: int | None, username: str):
        self.id = id
        self.username = username
