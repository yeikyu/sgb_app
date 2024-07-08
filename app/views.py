# app/views.py
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .models import Cooperativa
from .models import Unidad
from .models import Usuario
from .models import Ciudad
from .models import Cliente
from .models import Destino
from .models import Ruta
from .models import Horario
from .models import Boleto
from .models import Pago
from .models import Auditoria
from .models import Itinerario
from .models import Comentario
from .models import Calificacion
from .models import Categoria
from .models import CabFactura
from .models import DetalleFactura
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
    users = Usuario.query.all()
    return render_template('user/list_users.html', users=users)

#Nuevo usuarios
@main_bp.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user = request.form['user']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contraseña = request.form['pass']
        usuariocreacion = "root"
        fechacreacion = datetime.now()
        estado  = 1
        user = Usuario(user=user, nombre=nombre, apellido=apellido, contraseña=contraseña, usuariocreacion=usuariocreacion, fechacreacion=fechacreacion, estado=estado)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.list_user'))
    return render_template('user/add_user.html')

#Editar usuarios
@main_bp.route('/user/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id):
    user = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        user.user = request.form['user']
        user.nombre = request.form['nombre']
        user.apellido = request.form['apellido']
        user.contraseña = request.form['pass']
        db.session.commit()
        return redirect(url_for('main.list_user'))
    return render_template('user/edit_user.html', user=user)

#Eliminar usuarios
@main_bp.route('/user/<int:id>/delete', methods=['POST'])
def delete_user(id):
    user = Usuario.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.list_user'))

#-----------------------------------------------------------------------------------------------------------------
#Eliminar/Inactivar cliente
@main_bp.route('/client/<int:id>', methods=['POST'])
def delete_client(id):
    cliente = Cliente.query.get(id)
    if cliente:
        cliente.estado_cliente = 0  # Cambiar el estado a '0'
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
        clientes.nombre_cliente = request.form['nombre']
        clientes.apellido_cliente = request.form['apellido']
        clientes.cedula = request.form['cedula']
        clientes.email = request.form['email']
        clientes.fecha_nacimiento = request.form['fecha_nacimiento']
        clientes.direccion = request.form['direccion']
        clientes.telefono = request.form['telefono']
        clientes.cod_postal = request.form['cod_postal']
        db.session.commit()
        return redirect(url_for('main.list_clients'))
    return render_template('cliente/edit_client.html', clientes=clientes)


#Lista clientes
@main_bp.route('/client/list' , methods=['GET'])
def list_clients():
    clientes =  Cliente.query.filter(Cliente.estado_cliente != 0).all()
    for cliente in clientes:
        if cliente.estado_cliente == 1:
            cliente.estado_cliente = 'ACTIVO'
        else:
            cliente.estado_cliente = 'INACTIVO'
    return render_template('cliente/list_clients.html', clientes=clientes)




#Nuevo clientes
@main_bp.route('/client/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre']
        apellido_cliente = request.form['apellido']
        cedula = request.form['cedula']
        email = request.form['email']
        fecha_nacimiento = request.form['fecha_nacimiento']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        cod_postal = request.form['cod_postal']
        fecha_registro = datetime.now()
        ciudad = 1
        estado_cliente = 1
        fecha_nacimientostr = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        client = Cliente(nombre_cliente=nombre_cliente, apellido_cliente=apellido_cliente, cedula=cedula, estado_cliente=estado_cliente,email=email,fecha_nacimiento=fecha_nacimientostr,telefono=telefono,direccion=direccion,cod_postal=cod_postal,fecha_registro=fecha_registro,ciudad=ciudad)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('main.list_clients'))
    return render_template('cliente/add_client.html')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lista unidades 
@main_bp.route('/unidad/list' , methods=['GET'])
def list_unidades():
    unit = Unidad.query.filter(Unidad.estado != 0).all()
    return render_template('unidad/list_unidades.html', unit=unit)



@main_bp.route('/unidad/<int:id>/edit', methods=['GET', 'POST'])
def edit_(id):
    unit = Unidad.query.get_or_404(id)
    if request.method == 'POST':
        # Aquí deberías manejar la actualización de la unidad
        unit.nombre = request.form['nombre']
        unit.categoria = int(request.form['categoria_id'])
        unit.descripcion = request.form['descripcion']
        unit.precio = request.form['precio']
        db.session.commit()
        return redirect(url_for('main.list_unidades'))
    mostrar_contenido = False
    return render_template('unidad/edit_unidades.html', unit=unit,mostrar_contenido=mostrar_contenido)




# Ruta para agregar una unidad
@main_bp.route('/unidad/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Obtener datos del formulario
        nueva_unidad = None  # Inicializa la variable antes de usarla
        categoria_id = int(request.form['categoria_id'])
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        estado = 1
        fechacreacion = datetime.now()
            # Puedes ajustar la fecha de creación según tus necesidades
        nueva_unidad = Unidad(
            categoria_id=categoria_id,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            estado=estado,fecha_creacion=fechacreacion
        )

        # Guardar la nueva unidad en la base de datos
        db.session.add(nueva_unidad)
        db.session.commit()

        return redirect(url_for('main.list_unidades'))
    mostrar_contenido = False
    return render_template('unidad/add_unidades.html',mostrar_contenido=mostrar_contenido)

 
 #Eliminar unidad de la tabla
@main_bp.route('/unidad/<int:id>/delete', methods=['POST'])
def delete_product(id):
     unidades = Unidad.query.get_or_404(id) 
     db.session.delete(unidades)
     db.session.commit()
     return redirect(url_for('main.list_unidades'))

#------
# lista cooperativas
@main_bp.route('/cooperativa/list' , methods=['GET'])
def list_cooperativa():
     cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
     return render_template('cooperativa/list_cooperativa.html', cooperativas=cooperativas)


# agregar cooperativa 

@main_bp.route('/cooperativa/add', methods=['GET', 'POST'])
def add_cooperativa():
     if request.method == 'POST':
        razonsocial = request.form['razonsocial']
        Ruc = request.form['Ruc']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        email = request.form['email']
        estado = 1
        usuariocreacion = "root"
        fechacreacion = datetime.now()
        cooperativas = Cooperativa(razonsocial=razonsocial, Ruc=Ruc, telefono=telefono, direccion=direccion, email=email, estado=estado , usuariocreacion=usuariocreacion, fechacreacion=fechacreacion)
        db.session.add(cooperativas)
        db.session.commit()
        return redirect(url_for('main.list_cooperativa'))

     return render_template('cooperativa/add_cooperativa.html')

#editar cooperativa

@main_bp.route('/cooperativa/<int:id>/edit', methods=['GET', 'POST'])
def edit_cooperativa(id):
    cooperativa = Cooperativa.query.get_or_404(id)
    if request.method == 'POST':
        # Aquí deberías manejar la actualización del producto
        cooperativa.razonsocial = request.form['razonsocial']
        cooperativa.Ruc = request.form['ruc']
        cooperativa.telefono = request.form['telefono']
        cooperativa.direccion = request.form['direccion']
        cooperativa.email = request.form['email']
        db.session.commit()
        return redirect(url_for('main.list_cooperativa'))
    mostrar_contenido = False
    return render_template('cooperativa/edit_cooperativa.html', cooperativa=cooperativa,mostrar_contenido=mostrar_contenido)



#borrar cooperativa


@main_bp.route('/cooperativa/<int:id>', methods=['POST'])
def delete_cooperativa(id):
    cooperativas = Cooperativa.query.get(id)
    if cooperativas: 
        cooperativas.estado = 0  # Cambiar el estado a '0'
        db.session.commit()
    return redirect(url_for('main.list_cooperativa'))
