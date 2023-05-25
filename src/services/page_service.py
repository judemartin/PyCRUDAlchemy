# page service

def find_all():
    return ['Page1', 'Page2', 'Page3']


def find_one(page_id: int):
    return f'Page {page_id}'


def create():
    return 'Page created!'


def update(page_id: int):
    return f'Page {page_id} updated!'


def delete(page_id: int):
    return f'Page {page_id} deleted!'
