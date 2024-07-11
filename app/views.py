# app/views.py
from flask import Blueprint, flash, render_template, request, redirect, url_for
from datetime import datetime
from .models import Cooperativa
from .models import Unidad
from .models import Conductor
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


@main_bp.route('/ciudad/list')
def list_ciudades():
    ciudades = Ciudad.query.filter(Ciudad.estado != 0).all()
    return render_template('ciudad/list_ciudad.html', ciudades=ciudades)

@main_bp.route('/ciudad/add', methods=['GET', 'POST'])
def crear_ciudad():
    if request.method == 'POST':
        nombre = request.form['nombre']
        estado = 1
        ciudad = Ciudad(nombre=nombre, estado=estado)
        db.session.add(ciudad)
        db.session.commit()
        return redirect(url_for('main.list_ciudades'))
    return render_template('ciudad/add_ciudad.html')

@main_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_ciudad(id):
    ciudad = Ciudad.query.get_or_404(id)
    if request.method == 'POST':
        ciudad.nombre = request.form['nombre']
        ciudad.estado = request.form['estado']
        db.session.commit()
        return redirect(url_for('main.list_ciudades'))
    return render_template('ciudad/edit_ciudad.html', ciudad=ciudad)

@main_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_ciudad(id):
    ciudad = Ciudad.query.get_or_404(id)
    db.session.delete(ciudad)
    db.session.commit()
    return redirect(url_for('main.list_ciudades'))











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
        flash("cliente creado exitosamente")
        return redirect(url_for('main.list_clients'))
    return render_template('cliente/add_client.html')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lista unidades 
@main_bp.route('/unidad/list' , methods=['GET'])
def list_unidades():
    unit = Unidad.query.filter(Unidad.estado != 0).all()
    return render_template('unidad/list_unidades.html', unit=unit)



@main_bp.route('/unidad/<int:id>/edit', methods=['GET', 'POST'])
def edit_unidad(id):
    unit = Unidad.query.get_or_404(id)
    if request.method == 'POST':
        # Aquí deberías manejar la actualización de la unidad
        unit.id_conductor = request.form['id_conductor']
        unit.placa = request.form['placa']
        unit.modelo = request.form['modelo']
        unit.ano = request.form['ano']
        unit.nro_disco = request.form['nro_disco']
        unit.nrodeasientos = request.form['nrodeasientos']
        db.session.commit()
        return redirect(url_for('main.list_unidades'))
    mostrar_contenido = False
    return render_template('unidad/edit_unidades.html', unit=unit,mostrar_contenido=mostrar_contenido)




# Ruta para agregar una unidad
@main_bp.route('/unidad/add', methods=['GET', 'POST'])
def add_unidad():
    if request.method == 'POST':
          # Extraer los datos del formulario
        id_conductor = request.form['id_conductor']
        id_cooperativa = request.form['id_cooperativa']
        placa = request.form['placa']
        modelo = request.form['modelo']
        ano = request.form['ano']
        nro_disco = request.form['nro_disco']
        nrodeasientos = request.form['nrodeasientos']
        estado = 1
        usuariocreacion = "root"
        fechacreacion = datetime.now()

        # Crear una nueva instancia del modelo Unidad
        nueva_unidad = Unidad(
            id_conductor=id_conductor,
            id_cooperativa=id_cooperativa,
            placa=placa,
            modelo=modelo,
            ano=ano,
            nro_disco=nro_disco,
            nrodeasientos=nrodeasientos,
            estado=estado,
            usuariocreacion=usuariocreacion,
            fechacreacion=fechacreacion
        )

        # Guardar la nueva unidad en la base de datos
        db.session.add(nueva_unidad)
        db.session.commit()

        return redirect(url_for('main.list_unidades'))
    mostrar_contenido = False
    return render_template('unidad/add_unidades.html',mostrar_contenido=mostrar_contenido)

 
 #Eliminar unidad de la tabla
@main_bp.route('/unidad/<int:id>/delete', methods=['POST'])
def delete_unidad(id):
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



@main_bp.route('/conductores', methods=['GET'])
def listar_conductores():
    conductores = conductores.query.all()
    return render_template('listar_conductores.html', conductores=conductores)


@main_bp.route('/conductores/nuevo', methods=['GET', 'POST'])
def nuevo_conductor():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        id_cooperativa = request.form.get('id_cooperativa')
        licencia = request.form.get('licencia')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        fecha_contratacion = request.form.get('fecha_contratacion')
        estado_empleo = request.form.get('estado_empleo')

        nuevo_conductor = Conductor(
            nombre=nombre,
            apellido=apellido,
            id_cooperativa=id_cooperativa,
            licencia=licencia,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            estado_empleo=estado_empleo
        )
        db.session.add(nuevo_conductor)
        db.session.commit()
        flash('Conductor creado exitosamente.')
        return redirect(url_for('listar_conductores'))
    return render_template('nuevo_conductor.html')

@main_bp.route('/conductores/editar/<int:id>', methods=['GET', 'POST'])
def editar_conductor(id):
    conductor = Conductor.query.get_or_404(id)
    if request.method == 'POST':
        conductor.nombre = request.form.get('nombre')
        conductor.apellido = request.form.get('apellido')
        conductor.id_cooperativa = request.form.get('id_cooperativa')
        conductor.licencia = request.form.get('licencia')
        conductor.fecha_nacimiento = request.form.get('fecha_nacimiento')
        conductor.direccion = request.form.get('direccion')
        conductor.telefono = request.form.get('telefono')
        conductor.email = request.form.get('email')
        conductor.fecha_contratacion = request.form.get('fecha_contratacion')
        conductor.estado_empleo = request.form.get('estado_empleo')

        db.session.commit()
        flash('Conductor actualizado exitosamente.')
        return redirect(url_for('listar_conductores'))
    return render_template('editar_conductor.html', conductor=conductor)



@main_bp.route('/conductores/eliminar/<int:id>', methods=['POST'])
def eliminar_conductor(id):
    conductor = Conductor.query.get_or_404(id)
    db.session.delete(conductor)
    db.session.commit()
    flash('Conductor eliminado exitosamente.')
    return redirect(url_for('listar_conductores'))







# # CRUD para Destino
# @main_bp.route('/destinos', methods=['GET'])
# def mostrar_destinos():
#     destinos = Destino.query.all()
#     return render_template('destinos.html', destinos=destinos)

# @app.route('/destinos/crear', methods=['GET', 'POST'])
# def crear_destino():
#     if request.method == 'POST':
#         data = request.form
#         nuevo_destino = Destino(
#             ubicacion=data['ubicacion'],
#             ciudad=data['ciudad'],
#             descripcion=data['descripcion'],
#             estado=data['estado'],
#             fecha_creacion=datetime.strptime(data['fecha_creacion'], '%Y-%m-%d'),
#             fecha_modificacion=datetime.strptime(data['fecha_modificacion'], '%Y-%m-%d')
#         )
#         db.session.add(nuevo_destino)
#         db.session.commit()
#         return redirect(url_for('mostrar_destinos'))
#     return render_template('crear_destino.html')

# @app.route('/destinos/<int:id_destino>', methods=['GET'])
# def obtener_destino(id_destino):
#     destino = Destino.query.get_or_404(id_destino)
#     return render_template('detalle_destino.html', destino=destino)

# @app.route('/destinos/<int:id_destino>/editar', methods=['GET', 'POST'])
# def editar_destino(id_destino):
#     destino = Destino.query.get_or_404(id_destino)
#     if request.method == 'POST':
#         data = request.form
#         destino.ubicacion = data['ubicacion']
#         destino.ciudad = data['ciudad']
#         destino.descripcion = data['descripcion']
#         destino.estado = data['estado']
#         destino.fecha_modificacion = datetime.utcnow()
#         if 'fecha_eliminacion' in data:
#             destino.fecha_eliminacion = datetime.strptime(data['fecha_eliminacion'], '%Y-%m-%d')
#         db.session.commit()
#         return redirect(url_for('mostrar_destinos'))
#     return render_template('editar_destino.html', destino=destino)

# @app.route('/destinos/<int:id_destino>/eliminar', methods=['POST'])
# def eliminar_destino(id_destino):
#     destino = Destino.query.get_or_404(id_destino)
#     db.session.delete(destino)
#     db.session.commit()
#     return redirect(url_for('mostrar_destinos'))

# # CRUD para Ruta
# @app.route('/rutas', methods=['GET'])
# def mostrar_rutas():
#     rutas = Ruta.query.all()
#     return render_template('rutas.html', rutas=rutas)

# @app.route('/rutas/crear', methods=['GET', 'POST'])
# def crear_ruta():
#     if request.method == 'POST':
#         data = request.form
#         nueva_ruta = Ruta(
#             id_unidad=data['id_unidad'],
#             id_cooperativa=data['id_cooperativa'],
#             estado=data['estado'],
#             lugar_origen=data['lugar_origen'],
#             lugar_destino=data['lugar_destino'],
#             fecha_creacion=datetime.utcnow(),
#             hora_salida=data['hora_salida'],
#             hora_llegada=data['hora_llegada']
#         )
#         db.session.add(nueva_ruta)
#         db.session.commit()
#         return redirect(url_for('mostrar_rutas'))
#     return render_template('crear_ruta.html')

# @app.route('/rutas/<int:id_ruta>', methods=['GET'])
# def obtener_ruta(id_ruta):
#     ruta = Ruta.query.get_or_404(id_ruta)
#     return render_template('detalle_ruta.html', ruta=ruta)

# @app.route('/rutas/<int:id_ruta>/editar', methods=['GET', 'POST'])
# def editar_ruta(id_ruta):
#     ruta = Ruta.query.get_or_404(id_ruta)
#     if request.method == 'POST':
#         data = request.form
#         ruta.id_unidad = data['id_unidad']
#         ruta.id_cooperativa = data['id_cooperativa']
#         ruta.estado = data['estado']
#         ruta.lugar_origen = data['lugar_origen']
#         ruta.lugar_destino = data['lugar_destino']
#         ruta.hora_salida = data['hora_salida']
#         ruta.hora_llegada = data['hora_llegada']
#         if 'fecha_eliminacion' in data:
#             ruta.fecha_eliminacion = datetime.strptime(data['fecha_eliminacion'], '%Y-%m-%d')
#         db.session.commit()
#         return redirect(url_for('mostrar_rutas'))
#     return render_template('editar_ruta.html', ruta=ruta)

# @app.route('/rutas/<int:id_ruta>/eliminar', methods=['POST'])
# def eliminar_ruta(id_ruta):
#     ruta = Ruta.query.get_or_404(id_ruta)
#     db.session.delete(ruta)
#     db.session.commit()
#     return redirect(url_for('mostrar_rutas'))

# # CRUD para Horario
# @app.route('/horarios', methods=['GET'])
# def mostrar_horarios():
#     horarios = Horario.query.all()
#     return render_template('horarios.html', horarios=horarios)

# @app.route('/horarios/crear', methods=['GET', 'POST'])
# def crear_horario():
#     if request.method == 'POST':
#         data = request.form
#         nuevo_horario = Horario(
#             id_ruta=data['id_ruta'],
#             id_autobus=data['id_autobus'],
#             hora_salida=data['hora_salida'],
#             hora_llegada=data['hora_llegada'],
#             estado=data['estado']
#         )
#         db.session.add(nuevo_horario)
#         db.session.commit()
#         return redirect(url_for('mostrar_horarios'))
#     return render_template('crear_horario.html')

# @app.route('/horarios/<int:id_horario>', methods=['GET'])
# def obtener_horario(id_horario):
#     horario = Horario.query.get_or_404(id_horario)
#     return render_template('detalle_horario.html', horario=horario)

# @app.route('/horarios/<int:id_horario>/editar', methods=['GET', 'POST'])
# def editar_horario(id_horario):
#     horario = Horario.query.get_or_404(id_horario)
#     if request.method == 'POST':
#         data = request.form
#         horario.id_ruta = data['id_ruta']
#         horario.id_autobus = data['id_autobus']
#         horario.hora_salida = data['hora_salida']
#         horario.hora_llegada = data['hora_llegada']
#         horario.estado = data['estado']
#         db.session.commit()
#         return redirect(url_for('mostrar_horarios'))
#     return render_template('editar_horario.html', horario=horario)

# @app.route('/horarios/<int:id_horario>/eliminar', methods=['POST'])
# def eliminar_horario(id_horario):
#     horario = Horario.query.get_or_404(id_horario)
#     db.session.delete(horario)
#     db.session.commit()
#     return redirect(url_for('mostrar_horarios'))

# # CRUD para Boleto
# @app.route('/boletos', methods=['GET'])
# def mostrar_boletos():
#     boletos = Boleto.query.all()
#     return render_template('boletos.html', boletos=boletos)

# @app.route('/boletos/crear', methods=['GET', 'POST'])
# def crear_boleto():
#     if request.method == 'POST':
#         data = request.form
#         nuevo_boleto = Boleto(
#             id_cliente=data['id_cliente'],
#             id_horario=data['id_horario'],
#             asiento=data['asiento'],
#             fecha_compra=datetime.utcnow(),
#             precio=data['precio'],
#             estado=data['estado']
#         )
#         db.session.add(nuevo_boleto)
#         db.session.commit()
#         return redirect(url_for('mostrar_boletos'))
#     return render_template('crear_boleto.html')

# @app.route('/boletos/<int:id_boleto>', methods=['GET'])
# def obtener_boleto(id_boleto):
#     boleto = Boleto.query.get_or_404(id_boleto)
#     return render_template('detalle_boleto.html', boleto=boleto)

# @app.route('/boletos/<int:id_boleto>/editar', methods=['GET', 'POST'])
# def editar_boleto(id_boleto):
#     boleto = Boleto.query.get_or_404(id_boleto)
#     if request.method == 'POST':
#         data = request.form
#         boleto.id_cliente = data['id_cliente']
#         boleto.id_horario = data['id_horario']
#         boleto.asiento = data['asiento']
#         boleto.precio = data['precio']
#         boleto.estado = data['estado']
#         db.session.commit()
#         return redirect(url_for('mostrar_boletos'))
#     return render_template('editar_boleto.html', boleto=boleto)

# @app.route('/boletos/<int:id_boleto>/eliminar', methods=['POST'])
# def eliminar_boleto(id_boleto):
#     boleto = Boleto.query.get_or_404(id_boleto)
#     db.session.delete(boleto)
#     db.session.commit()
#     return redirect(url_for('mostrar_boletos'))

# # CRUD para Pago
# @app.route('/pagos', methods=['GET'])
# def mostrar_pagos():
#     pagos = Pago.query.all()
#     return render_template('pagos.html', pagos=pagos)

# @app.route('/pagos/crear', methods=['GET', 'POST'])
# def crear_pago():
#     if request.method == 'POST':
#         data = request.form
#         nuevo_pago = Pago(
#             id_reserva=data['id_reserva'],
#             metodo_pago=data['metodo_pago'],
#             monto=data['monto'],
#             fechahora_pago=datetime.utcnow(),
#             estado_pago=data['estado_pago'],
#             estado=data['estado']
#         )
#         db.session.add(nuevo_pago)
#         db.session.commit()
#         return redirect(url_for('mostrar_pagos'))
#     return render_template('crear_pago.html')

# @app.route('/pagos/<int:id_pago>', methods=['GET'])
# def obtener_pago(id_pago):
#     pago = Pago.query.get_or_404(id_pago)
#     return render_template('detalle_pago.html', pago=pago)

# @app.route('/pagos/<int:id_pago>/editar', methods=['GET', 'POST'])
# def editar_pago(id_pago):
#     pago = Pago.query.get_or_404(id_pago)
#     if request.method == 'POST':
#         data = request.form
#         pago.id_reserva = data['id_reserva']
#         pago.metodo_pago = data['metodo_pago']
#         pago.monto = data['monto']
#         pago.estado_pago = data['estado_pago']
#         pago.estado = data['estado']
#         db.session.commit()
#         return redirect(url_for('mostrar_pagos'))
#     return render_template('editar_pago.html', pago=pago)

# @app.route('/pagos/<int:id_pago>/eliminar', methods=['POST'])
# def eliminar_pago(id_pago):
#     pago = Pago.query.get_or_404(id_pago)
#     db.session.delete(pago)
#     db.session.commit()
#     return redirect(url_for('mostrar_pagos'))
