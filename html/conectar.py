from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId


url = "mongodb+srv://benjaminmartinez29:Martinez890@mybasadate.bhz2ags.mongodb.net/?retryWrites=true&w=majority"

def conexion():
    cliente = MongoClient(url,Server_Api=ServerApi('1'))
    print("Conectado a la base de datos")
    try:
        cliente.admin.command('ping')
        db = cliente.restauranteDB
        return db
    
    except Exception as e:
        print(e)