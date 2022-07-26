from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import *

from comment.repository.models import CommentModel
from user.repository import UserModel

db = SQLAlchemy()


class PostModel(db.Model):
    __tablename__ = "comment"

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(Text(), nullable=False)
    published_date = Column(DateTime(), nullable=False)
    user_id = Column(Integer(), ForeignKey(UserModel.id))
    user = relationship(UserModel)
    comments = relationship(CommentModel)