from pymongo import MongoClient
from config import config

class Database(object):
    def __init__(self):
        self.client = MongoClient(config["db"]["url"])  #configure db
        self.db     = self.client[config["db"]["name"]]