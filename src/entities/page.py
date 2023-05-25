import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from src.data.modelbase import SqlAlchemyBase


class Page(SqlAlchemyBase):
    __tablename__ = 'page'

    id = Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=True)
    content = Column(String, nullable=True)
    number = Column(Integer, nullable=True, index=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='pages')

    __table_args__ = (UniqueConstraint('book_id', 'number', name='book_number_uc'),)
