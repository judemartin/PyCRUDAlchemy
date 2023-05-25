import json

from flask import jsonify


class PageResponseDTO:
    def __init__(self, id: int, url: str, content: str, number: int, book_id: int):
        self.id = id
        self.url = url
        self.content = content
        self.number = number
        self.book_id = book_id

    @classmethod
    def map_entity_to_dto(cls, page):
        return cls(
            id=page.id,
            url=page.url,
            content=page.content,
            number=page.number,
            book_id=page.book_id
        ).to_dict()

    @classmethod
    def map_entity_list_to_dto_list(cls, pages):
        return [cls.map_entity_to_dto(page) for page in pages]

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'content': self.content,
            'number': self.number,
            'book_id': self.book_id
        }

    def to_json(self):
        return jsonify(self.to_dict())

    @staticmethod
    def serialize(data):
        return json.dumps(data, cls=CustomJSONEncoder)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PageResponseDTO):
            return obj.__dict__
        return super().default(obj)
