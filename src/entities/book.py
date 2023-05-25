from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.data.modelbase import SqlAlchemyBase


class Book(SqlAlchemyBase):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    description = Column(String, nullable=True)
    isbn = Column(String, nullable=True)
    pages = relationship("Page", back_populates='book')
