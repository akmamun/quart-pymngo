from db.validation import Validator
from db.database import Database


class Todo(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.collection_name = 'todos'  # collection name

        self.fields = {
            "title": "string",
            "body": "string",
            "created": "datetime",
            "updated": "datetime"
        }

        self.create_required_fields = ["title", "body"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = ["title", "body"]

        # Fields optional for UPDATE
        self.update_optional_fields = []

    async def create(self, todo):
        # Validator will throw error if invalid
        self.validator.validate(
            todo, self.fields, self.create_required_fields, self.create_optional_fields)
        return await self.db.insert(todo, self.collection_name)

    async def find(self, todo):  # find all
        return await self.db.find(todo, self.collection_name)

    async def find_by_id(self, id):
        return await self.db.find_by_id(id, self.collection_name)

    async def update(self, id, todo):
        self.validator.validate(
            todo, self.fields, self.update_required_fields, self.update_optional_fields)
        return await self.db.update(id, todo, self.collection_name)

    async def delete(self, id):
        return await self.db.delete(id, self.collection_name)
