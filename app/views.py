# app/views.py
from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Cliente, CategoriaProducto, Producto, Venta, VentaDetalle
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

@main_bp.route('/client')
def list_client():
    cliente = Cliente.query.filter(Cliente.estado != '0').all()  # Excluir registros eliminados
    return render_template('cliente/list_clients.html', cliente=cliente)

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
    clientes = Cliente.query.all()
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

@main_bp.route('/product/list' , methods=['GET'])
def list_products():
    products = Producto.query.all()
    mostrar_contenido = False
    return render_template('producto/list_products.html', products=products,mostrar_contenido=mostrar_contenido)


@main_bp.route('/producto/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.list_products'))
    mostrar_contenido = False
    return render_template('producto/add_product.html',mostrar_contenido=mostrar_contenido)

@main_bp.route('/cate_producto/list' , methods=['GET'])
def list_categoria_products():
    categoria_products = CategoriaProducto.query.all()
    return render_template('cate_product/list_cate_products.html', categoria_products=categoria_products)


@main_bp.route('/cate_producto/add', methods=['GET', 'POST'])
def add_cate_product():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.list_cate_products'))

    return render_template('cate_product/add_cate_product.html')

