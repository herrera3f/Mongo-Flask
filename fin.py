from conectar import *

db = conexion()
coleccion = db.clientes

documentos = coleccion.find()

for documentos in documentos:
    print(documentos)