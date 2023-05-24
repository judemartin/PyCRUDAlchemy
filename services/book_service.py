# book service

def find_all():
    return ['Book1', 'Book2', 'Book3']


def find_one(book_id: int):
    return f'Book {book_id}'


def create():
    return 'Book created!'


def update(book_id: int):
    return f'Book {book_id} updated!'


def delete(book_id: int):
    return f'Book {book_id} deleted!'
