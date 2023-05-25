# book service
from flask import jsonify

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


@json_response
def create(create_book_request):
    session = db_session.create_session()
    book = Book()
    book.title = create_book_request.get('title')
    book.author = create_book_request.get('author')
    book.description = create_book_request.get('description')
    book.isbn = create_book_request.get('isbn')
    session.add(book)
    session.commit()
    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'description': book.description,
        'isbn': book.isbn
    }
    return jsonify(book_data), 201


def update(book_id: int):
    return f'Book {book_id} updated!'


def delete(book_id: int):
    return f'Book {book_id} deleted!'
