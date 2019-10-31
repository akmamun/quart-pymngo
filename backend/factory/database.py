from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from config import config

class Database(object):
    def __init__(self):
        self.client = AsyncIOMotorClient(config["db"]["url"])  #configure db
        self.db     = self.client[config["db"]["name"]]

    async def insert(self, element, collection_name):
        element["created"] = datetime.now()
        element["updated"] = datetime.now()
        inserted = await self.db[collection_name].insert_one(element)  # insert data to db
        return str(inserted.inserted_id)

    async def find(self,criteria ,collection_name,projection=None, limit=0, sort=None, cursor=False): 
        if "_id"  in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        found = self.db[collection_name].find(filter=criteria, projection=projection, limit=limit, sort=sort)    
       
        if cursor:
            return found

        found = list(found)

        for i in range(len(found)):  # to serialize object id need to convert string
            if "_id" in found[i]:
                found[i]["_id"] = str(found[i]["_id"])

        return found

    async def delete(self, id, collection_name):
        deleted = await self.db[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)