# page service
from src.data import db_session
from src.dto.outbound.page_response_dto import PageResponseDTO
from src.entities.book import Book
from src.entities.page import Page
from src.utils.not_found_exception import json_response, NotFoundException


@json_response
def find_all():
    session = db_session.create_session()
    pages = session.query(Page).all()
    page_responses = PageResponseDTO.map_entity_list_to_dto_list(pages)
    return page_responses, 200


@json_response
def find_one(page_id: int):
    session = db_session.create_session()
    page = session.query(Page).filter(Page.id == page_id).first()
    if page is None:
        raise NotFoundException(f'Page with id {page_id} not found')
    page_response = PageResponseDTO.map_entity_to_dto(page)
    return page_response, 200


@json_response
def create(create_page_request):
    print(create_page_request)
    session = db_session.create_session()
    book = session.query(Book).get(create_page_request.get('book_id'))
    if book is None:
        raise NotFoundException(f'Book with id: {create_page_request.get("book_id")} not found')
    page = Page(url=create_page_request.get('url'), content=create_page_request.get('content'),
                number=create_page_request.get("number"), book=book)
    session.add(page)
    session.commit()
    page_response = PageResponseDTO.map_entity_to_dto(page)
    return page_response, 201


@json_response
def update(page_id: int, update_page_request):
    session = db_session.create_session()
    page = session.query(Page).get(page_id)
    if page is None:
        raise NotFoundException(f'Page with id: {page_id} not found')

    for key, value in update_page_request.items():
        if key == 'book_id':
            book = session.query(Book).get(value)
            if book is None:
                raise NotFoundException(f'Book with id: {value} not found')
        setattr(page, key, value)

    session.commit()
    return find_one(page_id)


@json_response
def delete(page_id: int):
    session = db_session.create_session()
    page = session.query(Page).get(page_id)

    if page is None:
        raise NotFoundException(f'Page with id: {page_id} not found')

    session.delete(page)
    session.commit()

    return '', 204
