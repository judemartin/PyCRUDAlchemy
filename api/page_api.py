import flask

from services import page_service

blueprint = flask.Blueprint('pages', __name__)


@blueprint.route('/pages')
def get_all():
    return page_service.find_all()


@blueprint.route('/pages/<page_id>')
def get(page_id):
    return page_service.find_one(page_id)


@blueprint.route('/pages', methods=['POST'])
def create():
    return page_service.create()


@blueprint.route('/pages/<page_id>', methods=['PATCH'])
def update(page_id):
    return page_service.update(page_id)


@blueprint.route('/pages/<page_id>', methods=['DELETE'])
def delete(page_id):
    return page_service.delete(page_id)
