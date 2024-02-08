class Metodos:
    def __init__(self, connection, db_name='pokeplaza'):
        self.client = connection.get_client()
        self.db = self.client[db_name]

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def update_document(self, collection_name, query, new_values):
        collection = self.db[collection_name]
        return collection.update_many(query, {"$set": new_values})

    def replace_document(self, collection_name, query, document):
        collection = self.db[collection_name]
        return collection.replace_one(query, document)

    def delete_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def find_documents(self, collection_name, query={}):
        collection = self.db[collection_name]
        return collection.find(query)

    def search_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def delete_all_documents(self, collection_name):
        collection = self.db[collection_name]
        return collection.delete_many({})

    def show_all_documents(self, collection_name):
        collection = self.db[collection_name]
        return collection.find()

    def input_pokemon_data(self):
        pokemon_data = {}
        pokemon_data['nombre'] = input("Ingrese el nombre del Pokémon: ")
        pokemon_data['tipo'] = input("Ingrese el tipo del Pokémon: ")
        pokemon_data['nivel'] = int(input("Ingrese el nivel del Pokémon: "))
        return pokemon_data
    def input_update_values(self, collection_name):
        field_name = input(f"Ingrese el nombre del campo a actualizar en la colección {collection_name}: ")
        field_value = input("Ingrese el nuevo valor para {}: ".format(field_name))
        return {"$set": {field_name: field_value}}

    def input_replace_document(self, collection_name):
        field_name = input(f"Ingrese el nombre del campo en la colección {collection_name}: ")
        field_value = input("Ingrese el valor para {}: ".format(field_name))
        return {field_name: field_value}

    def input_query(self, collection_name):
        field_name = input(f"Ingrese el nombre del campo para la consulta en la colección {collection_name}: ")
        field_value = input("Ingrese el valor para {}: ".format(field_name))
        return {field_name: field_value}