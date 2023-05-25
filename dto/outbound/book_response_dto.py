import json

from flask import jsonify


class BookResponseDTO:
    def __init__(self, id: int, title: str, author: str, description: str, isbn: str):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.isbn = isbn

    @classmethod
    def map_entity_to_dto(cls, book):
        return cls(
            id=book.id,
            title=book.title,
            author=book.author,
            description=book.description,
            isbn=book.isbn
        ).to_dict()

    @classmethod
    def map_entity_list_to_dto_list(cls, books):
        return [cls.map_entity_to_dto(book) for book in books]

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'isbn': self.isbn
        }

    def to_json(self):
        return jsonify(self.to_dict())

    @staticmethod
    def serialize(data):
        return json.dumps(data, cls=CustomJSONEncoder)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BookResponseDTO):
            return obj.__dict__
        return super().default(obj)
