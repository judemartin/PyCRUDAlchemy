import flask
from flask import request

from src.services import book_service

blueprint = flask.Blueprint('books', __name__)


@blueprint.route('/books')
def find_all():
    return book_service.find_all()


@blueprint.route('/books/<book_id>')
def find_one(book_id):
    return book_service.find_one(book_id)


@blueprint.route('/books', methods=['POST'])
def create():
    create_book_request = request.get_json()
    return book_service.create(create_book_request)


@blueprint.route('/books/<book_id>', methods=['PATCH'])
def update(book_id):
    update_book_request = request.get_json()
    return book_service.update(book_id, update_book_request)


@blueprint.route('/books/<book_id>', methods=['DELETE'])
def delete(book_id):
    return book_service.delete(book_id)
