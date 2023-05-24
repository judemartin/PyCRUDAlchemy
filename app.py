from flask import Flask

from api.book_api import blueprint as book_api
from api.page_api import blueprint as page_api


def register_blueprints():
    app.register_blueprint(book_api)
    app.register_blueprint(page_api)


app = Flask(__name__)
register_blueprints()

if __name__ == '__main__':
    app.run()
