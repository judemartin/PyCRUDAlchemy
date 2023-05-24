from functools import wraps

from flask import jsonify, make_response


class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except NotFoundException as e:
            error_message = {'message': str(e)}
            response = make_response(jsonify(error_message), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

    return wrapper
