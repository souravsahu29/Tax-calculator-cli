import pymongo

class DatabaseConnection:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client["tax_calculator_db"]
        self.collection = self.db["users"]

    def insert_user(self, user_data):
        self.collection.insert_one(user_data)

