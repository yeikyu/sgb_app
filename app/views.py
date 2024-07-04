# app/views.py
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .models import User, Cliente, CategoriaProducto, Producto, Venta
from . import db

main_bp = Blueprint('main', __name__)

#-----------------------------------------------------------------------------------------------------------------

@main_bp.route('/')
def index():
    mostrar_contenido = True
    return render_template('index.html',mostrar_contenido=mostrar_contenido)

#Lista de usuarios
@main_bp.route('/user/list' , methods=['GET'])
def list_user():
    users = User.query.all()
    return render_template('user/list_users.html', users=users)

#Nuevo usuarios
@main_bp.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.list_user'))
    return render_template('user/add_user.html')

#Editar usuarios
@main_bp.route('/user/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('main.list_user'))
    return render_template('user/edit_user.html', user=user)

#Eliminar usuarios
@main_bp.route('/user/<int:id>/delete', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.list_user'))

#-----------------------------------------------------------------------------------------------------------------
#Eliminar/Inactivar cliente
@main_bp.route('/client/<int:id>', methods=['POST'])
def delete_client(id):
    cliente = Cliente.query.get(id)
    if cliente:
        cliente.estado = 0  # Cambiar el estado a '0'
        db.session.commit()
    return redirect(url_for('main.list_clients'))  # Redirigir a una página de lista de clientes



#Eliminar cliente de la tabla
#@main_bp.route('/client/<int:id>/delete', methods=['POST'])
#def delete_client(id):
#    cliente = Cliente.query.get_or_404(id) 
#    db.session.delete(cliente)
#    db.session.commit()
#    return redirect(url_for('main.list_clients'))

#--------------------------------------------------------------------------------------------------------------------

#Editar clientes
@main_bp.route('/client/<int:id>/edit', methods=['GET', 'POST'])
def edit_client(id):
    clientes = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        clientes.nombre = request.form['nombre']
        clientes.apellido = request.form['apellido']
        clientes.dni = request.form['dni']
        db.session.commit()
        return redirect(url_for('main.list_clients'))
    return render_template('cliente/edit_client.html', clientes=clientes)

#Lista clientes
@main_bp.route('/client/list' , methods=['GET'])
def list_clients():
    clientes =  Cliente.query.filter(Cliente.estado != 0).all()
    for cliente in clientes:
        if cliente.estado == 1:
            cliente.estado = 'ACTIVO'
        else:
            cliente.estado = 'INACTIVO'
    return render_template('cliente/list_clients.html', clientes=clientes)




#Nuevo clientes
@main_bp.route('/client/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        estado = 1
        client = Cliente(nombre=nombre, apellido=apellido, dni=dni, estado=estado)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('main.list_clients'))
    return render_template('cliente/add_client.html')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lista productos 
@main_bp.route('/product/list' , methods=['GET'])
def list_products():
    products = Producto.query.filter(Producto.estado != 0).all()
    return render_template('producto/list_products.html', products=products)



@main_bp.route('/product/<int:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    products = Producto.query.get_or_404(id)
    if request.method == 'POST':
        # Aquí deberías manejar la actualización del producto
        products.nombre = request.form['nombre']
        products.categoria = int(request.form['categoria_id'])
        products.descripcion = request.form['descripcion']
        products.precio = request.form['precio']
        db.session.commit()
        return redirect(url_for('main.list_products'))
    mostrar_contenido = False
    return render_template('producto/edit_product.html', products=products,mostrar_contenido=mostrar_contenido)




# Ruta para agregar un nuevo producto
@main_bp.route('/product/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Obtener datos del formulario
        nuevo_producto = None  # Inicializa la variable antes de usarla
        categoria_id = int(request.form['categoria_id'])
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        estado = 1
        fechacreacion = datetime.now()
            # Puedes ajustar la fecha de creación según tus necesidades
        nuevo_producto = Producto(
            categoria_id=categoria_id,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            estado=estado,fecha_creacion=fechacreacion
        )

        # Guardar el nuevo producto en la base de datos
        db.session.add(nuevo_producto)
        db.session.commit()

        return redirect(url_for('main.list_products'))
    mostrar_contenido = False
    return render_template('producto/add_product.html',mostrar_contenido=mostrar_contenido)

 
 #Eliminar producto de la tabla
@main_bp.route('/product/<int:id>/delete', methods=['POST'])
def delete_product(id):
     products = Producto.query.get_or_404(id) 
     db.session.delete(products)
     db.session.commit()
     return redirect(url_for('main.list_products'))

#------
@main_bp.route('/cate_producto/list' , methods=['GET'])
def list_cate_products():
     categorias = CategoriaProducto.query.filter(CategoriaProducto.estado != 0).all()
     return render_template('cate_product/list_cate_products.html', categorias=categorias)




@main_bp.route('/cate_producto/add', methods=['GET', 'POST'])
def add_cate_product():
     if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        estado = 1
        fechacreacion = datetime.now()
        CategoryProduct = CategoriaProducto(nombre=nombre, descripcion=descripcion, estado=estado, fecha_creacion=fechacreacion)
        db.session.add(CategoryProduct)
        db.session.commit()
        return redirect(url_for('main.list_cate_products'))

     return render_template('cate_product/add_cate_product.html')


@main_bp.route('/cate_product/<int:id>/edit', methods=['GET', 'POST'])
def edit_cate_product(id):
    products = CategoriaProducto.query.get_or_404(id)
    if request.method == 'POST':
        # Aquí deberías manejar la actualización del producto
        products.nombre = request.form['nombre']
        products.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('main.list_cate_products'))
    mostrar_contenido = False
    return render_template('cate_product/edit_cate_product.html', products=products,mostrar_contenido=mostrar_contenido)



#delete_product


@main_bp.route('/category/<int:id>', methods=['POST'])
def delete_categoria_product(id):
    categoria = CategoriaProducto.query.get(id)
    if categoria: 
        categoria.estado = 0  # Cambiar el estado a '0'
        db.session.commit()
    return redirect(url_for('main.list_cate_products'))
