import flask

blueprint = flask.Blueprint('pages', __name__)


@blueprint.route('/pages')
def get_all():
    return ['Page1', 'Page2']


@blueprint.route('/pages/<page_id>')
def get(page_id):
    return f'Page {page_id}'


@blueprint.route('/pages', methods=['POST'])
def create():
    return 'Page created'


@blueprint.route('/pages/<page_id>', methods=['PATCH'])
def update(page_id):
    return f'Page {page_id} updated'


@blueprint.route('/pages/<page_id>', methods=['DELETE'])
def delete(page_id):
    return f'Page {page_id} deleted'
