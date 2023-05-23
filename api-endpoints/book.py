import flask

blueprint = flask.Blueprint('books', __name__)


@blueprint.route('/books')
def get_all():
    return ['Book1', 'Book2']


@blueprint.route('/books/<book_id>')
def get(book_id):
    return f'Book {book_id}'


@blueprint.route('/books', methods=['POST'])
def create():
    return 'Book created'


@blueprint.route('/books/<book_id>', methods=['PATCH'])
def update(book_id):
    return f'Book {book_id} updated'


@blueprint.route('/books/<book_id>', methods=['DELETE'])
def delete(book_id):
    return f'Book {book_id} deleted'
