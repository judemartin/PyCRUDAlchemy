import os
import sys

import flask

from data import db_session

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True, port=5000)


def setup_db():
    db_conn_str = "replace this with a real connection string"
    db_session.global_init(db_conn_str)


def register_blueprints():
    from api import book_api
    from api import page_api

    app.register_blueprint(book_api.blueprint)
    app.register_blueprint(page_api.blueprint)


if __name__ == '__main__':
    main()
