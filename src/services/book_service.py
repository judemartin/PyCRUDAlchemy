# book service

from src.data import db_session
from src.dto.outbound.book_response_dto import BookResponseDTO
from src.entities.book import Book
from src.utils.not_found_exception import NotFoundException, json_response


@json_response
def find_all():
    session = db_session.create_session()
    books = session.query(Book).all()
    book_responses = BookResponseDTO.map_entity_list_to_dto_list(books)
    return book_responses, 200


@json_response
def find_one(book_id: int):
    session = db_session.create_session()
    book = session.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise NotFoundException(f'Book with id {book_id} not found')
    book_response = BookResponseDTO.map_entity_to_dto(book)
    return book_response, 200


@json_response
def create(create_book_request):
    session = db_session.create_session()
    book = Book(title=create_book_request.get('title'), author=create_book_request.get('author'),
                description=create_book_request.get('description'), isbn=create_book_request.get('isbn'))
    session.add(book)
    session.commit()
    book_response = BookResponseDTO.map_entity_to_dto(book)
    return book_response, 201


@json_response
def update(book_id: int, update_book_request: dict):
    session = db_session.create_session()
    book = session.query(Book).get(book_id)

    if book is None:
        raise NotFoundException(f'Book with id: {book_id} not found')

    for key, value in update_book_request.items():
        setattr(book, key, value)

    session.commit()
    return find_one(book_id)


@json_response
def delete(book_id: int):
    session = db_session.create_session()
    book = session.query(Book).get(book_id)

    if book is None:
        raise NotFoundException(f'Book with id: {book_id} not found')

    session.delete(book)
    session.commit()

    return '', 204
