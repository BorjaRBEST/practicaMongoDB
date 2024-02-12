from pymongo import MongoClient

# Clase Conexion donde ubicamos pymongo para llamarlo en el Main
class Conexion:
    def __init__(self, uri):
        self.client = MongoClient(uri)

    def get_client(self):
        return self.client
