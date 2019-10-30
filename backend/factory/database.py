from motor.motor_asyncio import AsyncIOMotorClient
from config import config

class Database(object):
    def __init__(self):
        self.client = AsyncIOMotorClient(config["db"]["url"])  #configure db
        self.db     = self.client[config["db"]["name"]]

    async def inset(self, element, collection_name):
        element["created"] = datetime.now()
        element["updated"] = datetime.now()
        inserted = await self.db[collection_name].insert_one(element)  # insert data to db
        return str(inserted.inserted_id)
    
    async def delete(self, id, collection_name):
        deleted = await self.db[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)