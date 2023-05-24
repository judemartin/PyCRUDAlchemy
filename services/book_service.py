# book service

from data import db_session
from entities.book import Book
from utils.not_found_exception import NotFoundException, json_response


def find_all():
    session = db_session.create_session()
    return session.query(Book).all()


@json_response
def find_one(book_id: int):
    session = db_session.create_session()
    book = session.query(Book).filter(Book.id is book_id).first()
    if book is None:
        raise NotFoundException(f'Book with id {book_id} not found')
    return book


def create():
    return 'Book created!'


def update(book_id: int):
    return f'Book {book_id} updated!'


def delete(book_id: int):
    return f'Book {book_id} deleted!'
