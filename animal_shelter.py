from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initialize MongoClient
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method: C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method: R in CRUD
    def read(self, query):
        if query is not None:
            return list(self.database.animals.find(query))
        else:
            return list(self.database.animals.find())

