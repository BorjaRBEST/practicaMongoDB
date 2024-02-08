from pymongo import MongoClient

class Conexion:
    def __init__(self, uri):
        self.client = MongoClient(uri)

    def get_client(self):
        return self.client
