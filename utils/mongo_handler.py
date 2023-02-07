from pymongo import MongoClient

from utils.connection_params import mongo_uri

class MongoHandler:
    def __init__(self):
        self.client = MongoClient(mongo_uri)
        self.__database = None
        self.__coll = None

    @property
    def database(self):
        pass

    @database.getter
    def database(self):
        return self.__database
    
    @database.setter
    def database(self, db):
        self.__database = db

    @property
    def coll(self):
        pass

    @coll.getter
    def coll(self):
        return self.__coll
    
    @coll.setter
    def coll(self, collection):
        self.__coll = collection

    def get_database_obj(self):
        return self.client[self.__database]
    
    def get_collection_obj(self):
        return self.get_database_obj()[self.__coll]
    
    def insert_document(self, document):
        return self.get_collection_obj().insert_one(document).inserted_id
    
    def del_doc_by_orig_title(self, movie_title):
        query = {"movie_title": movie_title}
        return self.get_collection_obj().delete_one(query).deleted_count