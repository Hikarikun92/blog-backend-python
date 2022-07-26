from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import *

# Note: these models must be defined in the same module, otherwise it won't be possible (in a simple way) to build
# relationships between them
db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)


class PostModel(db.Model):
    __tablename__ = "post"

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(Text(), nullable=False)
    published_date = Column(DateTime(), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'))
    user = relationship('UserModel')
    comments: list['CommentModel'] = relationship('CommentModel')


class CommentModel(db.Model):
    __tablename__ = "comment"

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(Text(), nullable=False)
    published_date = Column(DateTime(), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'))
    user = relationship('UserModel')
    post_id = Column(Integer(), ForeignKey('post.id'))
