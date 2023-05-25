import sqlalchemy
from sqlalchemy.orm import relationship

from src.data.modelbase import SqlAlchemyBase


class Page(SqlAlchemyBase):
    __tablename__ = 'page'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    url = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    book_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('book.id'))
    book = relationship('Book', back_populates='pages')
