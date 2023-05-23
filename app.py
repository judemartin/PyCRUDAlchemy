from flask import Flask

from api.book import blueprint as book_app
from api.page import blueprint as page_app


def register_blueprints():
    app.register_blueprint(book_app)
    app.register_blueprint(page_app)


app = Flask(__name__)
register_blueprints()

if __name__ == '__main__':
    app.run()
