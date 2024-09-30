from src.cloud_io import MongoIO
from src.constant import MONGO_DATABASE_NAME
from src.exception import CustomException
import os
import sys



def fetch_product_names_from_cloud():
    try:
        mongo=MongoIO
        collection_name=mongo.mongo_ins.mongo_operation_connect_database.list_collection_names()
        return [collection_name.replace('_',' ')
                for collection_name in collection_name]
    except Exception as e:
        raise CustomException(e,sys)