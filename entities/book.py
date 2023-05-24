import sqlalchemy

from data.modelbase import SqlAlchemyBase


class Book(SqlAlchemyBase):
    __tablename__ = 'book'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    isbn = sqlalchemy.Column(sqlalchemy.String, nullable=True)
