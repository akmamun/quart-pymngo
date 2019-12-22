from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from config import config


class Database(object):
    def __init__(self):
        self.client = AsyncIOMotorClient(config["db"]["url"])  # configure db
        self.db = self.client[config["db"]["name"]]

    async def insert(self, element, collection_name):
        element["created"] = datetime.now()
        element["updated"] = datetime.now()
        # insert data to db
        res = await self.db[collection_name].insert_one(element)
        success = bool(res.acknowledged)
        return success

    async def find(self, criteria, collection_name, projection=None, limit=0, sort=None, cursor=False):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])

        found = self.db[collection_name].find(
            filter=criteria, projection=projection, limit=limit, sort=sort)
        if cursor:
            return found

        found = await found.to_list(10000)  # length required

        for i in range(len(found)):  # to serialize object id need to convert string
            if "_id" in found[i]:
                found[i]["_id"] = str(found[i]["_id"])

        return found

    async def find_by_id(self, id, collection_name):
        found = await self.db[collection_name].find_one({"_id": ObjectId(id)})
        if found is None:
            return not found

        elif "_id" in found:
            found["_id"] = str(found["_id"])

        return found

    async def update(self, id, element, collection_name):
        criteria = {"_id": ObjectId(id)}

        element["updated"] = datetime.now()
        set_obj = {"$set": element}  # update value

        updated = await self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return "Record Successfully Updated"

    async def delete(self, id, collection_name):
        deleted = await self.db[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)
