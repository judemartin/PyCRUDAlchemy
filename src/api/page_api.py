import flask
from flask import request

from src.services import page_service

blueprint = flask.Blueprint('pages', __name__)


@blueprint.route('/pages')
def get_all():
    return page_service.find_all()


@blueprint.route('/pages/<page_id>')
def get(page_id):
    return page_service.find_one(page_id)


@blueprint.route('/pages', methods=['POST'])
def create():
    create_page_request = request.get_json()
    return page_service.create(create_page_request)


@blueprint.route('/pages/<page_id>', methods=['PATCH'])
def update(page_id):
    update_page_request = request.get_json()
    return page_service.update(page_id, update_page_request)


@blueprint.route('/pages/<page_id>', methods=['DELETE'])
def delete(page_id):
    return page_service.delete(page_id)
