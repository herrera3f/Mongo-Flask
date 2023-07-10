from flask import Flask, render_template, request , redirect
from conectar import *
from jinja2 import Template
from datetime import datetime
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
@app.route('/home')
#esto sirve para que se pueda ver la pagina principal
def home():
    db = conexion()

    menu = db.menu.find({'status': 1})
    clientes = db.clientes.find({'status': 1})
    pedidos = db.pedidos.find({'status': 1})
    
    
   
    return render_template('index.html', clientes=clientes, pedidos=pedidos, menu=menu)


db = conexion()  



@app.route('/activar-desactivar')
def activar_desactivar():
    menu = db.menu.find()
    clientes = db.clientes.find()
    pedidos = db.pedidos.find()
    return render_template('activar-desactivar.html', menu=menu, clientes=clientes, pedidos=pedidos)

@app.route('/eliminar/<item_id>')
def eliminar(item_id):
    db.menu.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': 0}})
    db.clientes.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': 0}})
    db.pedidos.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': 0}})
    return redirect('/activar-desactivar')

@app.route('/activar/<item_id>')
def activar(item_id):
    db.menu.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': 1}})
    db.clientes.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': 1}})
    db.pedidos.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': 1}})
    return redirect('/activar-desactivar')




@app.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        db = conexion()
        #cliente#
        NombreC = request.form['nombre_cliente']
        RutC = request.form['Rut_cliente']
        Apellido = request.form['apellido_cliente']
        Teléfono = request.form['telefono_cliente']
        Dirección = request.form['direccion_cliente']
        Email = request.form['email_cliente']

        #menu#
        NombreM = request.form['nombre_menu']
        DescripciónM = request.form['descripcion_menu']
        Platos = []
        
        for i in range(3):
            
            NombreP = request.form[f'nombre_plato{i}']
            DescripciónP = request.form[f'descripcion_plato{i}']
            Preciop = request.form[f'precio_plato{i}']
            Plato = {"Nombre": NombreP, "Descripción": DescripciónP , "Precio": Preciop}
            Platos.append(Plato)
                        
        #pedido#
        RutC = request.form['Rut_cliente']
        fecha_actual = datetime.now()
        Articulos = []
        
        for i in range(2):
            NombreA = request.form[f'nombre_articulos{i}']
            cantidad = request.form[f'cantidad_articulos{i}']
            Precio = request.form[f'precio_articulos{i}']
            Articulo = {"Nombre": NombreA, "Cantidad": cantidad, "PrecioUnitario": Precio}
            Articulos.append(Articulo)

        
        db.clientes.insert_one({"Nombre": NombreC,"rut":RutC, "Apellido": Apellido, "Teléfono": Teléfono, "Dirección": Dirección, "Email": Email}) 
        db.menu.insert_one({"Nombre": NombreM, "Descripción": DescripciónM,"Platos":Platos})
        db.pedidos.insert_one({"rut": RutC, "Fecha": fecha_actual , "Artículos": Articulos})
        
        return redirect('/')  
    else:
        return render_template('insert.html')

db = conexion()
clientes = db.clientes.find()

@app.route('/Actualizar', methods=['GET', 'POST'])
def actualizar():
    if request.method == 'POST':
        db = conexion()
        db.clientes.find()  

        #cliente#
        NombreC = request.form['nombre_cliente']
        RutC = request.form['Rut_cliente']
        Apellido = request.form['apellido_cliente']
        Teléfono = request.form['telefono_cliente']
        Dirección = request.form['direccion_cliente']
        Email = request.form['email_cliente']                
        #menu#
        NombreM = request.form['nombre_menu']
        DescripciónM = request.form['descripcion_menu']
        Platos = []        
        for i in range(3):
            
            NombreP = request.form[f'nombre_plato{i}']
            DescripciónP = request.form[f'descripcion_plato{i}']
            Preciop = request.form[f'precio_plato{i}']
            Plato = {"Nombre": NombreP, "Descripción": DescripciónP , "Precio": Preciop}
            Platos.append(Plato)
        
        #pedido#

        RutC = request.form['Rut_cliente']
        fecha_actual = datetime.now()
        Articulos = []
        
        for i in range(2):
            NombreA = request.form[f'nombre_articulos{i}']
            cantidad = request.form[f'cantidad_articulos{i}']
            Precio = request.form[f'precio_articulos{i}']
            Articulo = {"Nombre": NombreA, "Cantidad": cantidad, "PrecioUnitario": Precio}
            Articulos.append(Articulo)                  
        # Actualizar cliente
        db.clientes.update_one({"rut":RutC}, {'$set': {"Nombre": NombreC, "Apellido": Apellido, "Teléfono": Teléfono, "Dirección": Dirección, "Email": Email}})

        # Actualizar menú 
        db.menu.update_one({"Nombre": NombreM}, {'$set': {"Descripción": DescripciónM, "Platos": Platos}})

        # Actualizar pedido
        db.pedidos.update_one({"rut":RutC}, {'$set': { "Fecha": fecha_actual, "Artículos": Articulos}})
        
        return redirect('/')
    else:
        return render_template('actualizar.html', actualizar=True, clientes=clientes)  
   










if __name__ == '__main__':
    app.run(debug=True)