# app/views.py
from flask import Blueprint, flash, render_template, request, redirect, url_for
# import pdfkit 
from datetime import datetime
from .models import Cooperativa
from .models import Unidad
from .models import Conductor
from .models import Usuario
from .models import Ciudad
from .models import Cliente
from .models import Ruta
from .models import Horario
from .models import Boleto
from .models import Pago
from .models import Itinerario
from .models import Comentario
from .models import Calificacion
from .models import Categoria
from .models import CabFactura
from .models import DetalleFactura
from .models import metodopago
from .models import Anden
from .models import Producto

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
        ciudad.estado = 1
        db.session.commit()
        return redirect(url_for('main.list_ciudades'))
    return render_template('ciudad/edit_ciudad.html', ciudad=ciudad)

@main_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_ciudad(id):
    ciudades = Ciudad.query.get(id)
    if ciudades:
        ciudades.estado = 0    
    
    db.session.commit()
    return redirect(url_for('main.list_ciudades'))




#Lista de usuarios
@main_bp.route('/user/list' , methods=['GET'])
def list_user():
    users = Usuario.query.filter(Usuario.estado != 0).all()
    return render_template('user/list_users.html', users=users)

#Nuevo usuarios
@main_bp.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user = request.form['user']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contraseña = request.form['pass']
        id_cooperativa = int(request.form['id_cooperativa'])
        usuariocreacion = "root"
        fechacreacion = datetime.now()
        estado  = 1
        
        if id_cooperativa is None:
            user = Usuario(user=user, nombre=nombre,apellido=apellido, contraseña=contraseña, usuariocreacion=usuariocreacion, fechacreacion=fechacreacion, estado=estado)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.list_user'))
        else:
            user = Usuario(user=user, nombre=nombre, id_cooperativa=id_cooperativa,apellido=apellido, contraseña=contraseña, usuariocreacion=usuariocreacion, fechacreacion=fechacreacion, estado=estado)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.list_user'))
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    return render_template('user/add_user.html',cooperativas=cooperativas)

#Editar usuarios
@main_bp.route('/user/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id):
    user = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        user.user = request.form['user']
        user.nombre = request.form['nombre']
        user.apellido = request.form['apellido']
        user.contraseña = request.form['pass']
        user.id_cooperativa = request.form['id_cooperativa']
        db.session.commit()
        return redirect(url_for('main.list_user'))
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    return render_template('user/edit_user.html', user=user,cooperativas=cooperativas)

#Eliminar usuarios
@main_bp.route('/user/<int:id>/delete', methods=['POST'])
def delete_user(id):
    users = Usuario.query.get(id)
    if users: 
        users.estado = 0  # Cambiar el estado a '0'
        db.session.commit()
        flash('Usuario eliminado exitosamente.')

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


#----------------------------------------------------------------------------------------------------------------

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
        ciudad = request.form['ciudad']
        estado_cliente = 1
        fecha_nacimientostr = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        client = Cliente(nombre_cliente=nombre_cliente, apellido_cliente=apellido_cliente, cedula=cedula, estado_cliente=estado_cliente,email=email,fecha_nacimiento=fecha_nacimientostr,telefono=telefono,direccion=direccion,cod_postal=cod_postal,fecha_registro=fecha_registro,ciudad=ciudad)
        db.session.add(client)
        db.session.commit()
        flash("cliente creado exitosamente")
        return redirect(url_for('main.list_clients'))
    ciudades = Ciudad.query.all()
    return render_template('cliente/add_client.html',ciudades=ciudades)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lista unidades 
@main_bp.route('/unidad/list' , methods=['GET'])
def list_unidades():
    unidades = Unidad.query.filter(Unidad.estado != 0).all()
    return render_template('unidad/list_unidades.html', unidades=unidades)



@main_bp.route('/unidad/<int:id>/edit', methods=['GET', 'POST'])
def edit_unidad(id):
    unidades = Unidad.query.get_or_404(id)
    if request.method == 'POST':
        # Aquí deberías manejar la actualización de la unidad
        unidades.id_conductor = request.form['id_conductor']
        unidades.id_cooperativa = request.form['id_cooperativa']
        unidades.placa = request.form['placa']
        unidades.modelo = request.form['modelo']
        unidades.ano = request.form['ano']
        unidades.nro_disco = request.form['nro_disco']
        unidades.nrodeasientos = request.form['nrodeasientos']
        db.session.commit()
        return redirect(url_for('main.list_unidades'))
    mostrar_contenido = False
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    conductores = Conductor.query.filter(Conductor.estado_empleo != 0).all()
    return render_template('unidad/edit_unidades.html', unidades=unidades,mostrar_contenido=mostrar_contenido,cooperativas=cooperativas,conductores=conductores)




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
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    conductores = Conductor.query.filter(Conductor.estado_empleo != 0).all()
    mostrar_contenido = False
    return render_template('unidad/add_unidades.html',mostrar_contenido=mostrar_contenido,cooperativas=cooperativas,conductores=conductores)

 
 #Eliminar unidad de la tabla

@main_bp.route('/unidad/delete/<int:id>', methods=['POST'])
def delete_unidad(id):
    unidades = Unidad.query.get(id)
    if unidades: 
        unidades.estado = 0  # Cambiar el estado a '0'
        db.session.commit()
        flash('unidad eliminada exitosamente.')
    return redirect(url_for('main.list_unidades'))
#------

#CRUD PARA ANDENES
@main_bp.route('/listaandenes')
def list_andens():
    andenes = Anden.query.filter(Anden.estado != 0).all()
    return render_template('anden/list_anden.html', andenes=andenes)




@main_bp.route('/andenes/add', methods=['GET', 'POST'])
def add_anden():
    if request.method == 'POST':
        id_cooperativa = int(request.form['id_cooperativa'])
        nro_anden = int(request.form['nro_anden'])
        estado = 1
        nuevo_anden = Anden(id_cooperativa=id_cooperativa, nro_anden=nro_anden, estado=estado)
        db.session.add(nuevo_anden)
        db.session.commit()
        return redirect(url_for('main.list_andens'))
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    return render_template('anden/add_anden.html',cooperativas=cooperativas)

@main_bp.route('/andenes/edit/<int:id>', methods=['GET', 'POST'])
def edit_anden(id):
    anden = Anden.query.get_or_404(id)
    if request.method == 'POST':
        anden.id_cooperativa = request.form['id_cooperativa']
        anden.nro_anden = request.form['nro_anden']
        
        db.session.commit()
        return redirect(url_for('main.list_andens'))
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    return render_template('anden/edit_anden.html', anden=anden,cooperativas=cooperativas)


@main_bp.route('/eliminar_anden/<int:id>', methods=['POST'])
def eliminar_anden(id):
    anden = Anden.query.get(id)
    if anden:
        anden.estado = 0
        db.session.commit()
        return redirect('main.list_andens')  # Redirige a una lista de andenes
    return 'Anden no encontrado', 404



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
    conductores = Conductor.query.filter(Conductor.estado_empleo != 0).all()
    return render_template('conductor/list_conductor.html', conductores=conductores)


@main_bp.route('/conductores/nuevo', methods=['GET', 'POST'])
def nuevo_conductor():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        disco = request.form.get('disco')
        id_cooperativa = request.form.get('id_cooperativa')
        licencia = request.form.get('licencia')
        cedula = request.form.get('cedula')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        fecha_contratacion = request.form.get('fecha_contratacion')
        estado_empleo = 1

        nuevo_conductor = Conductor(
            nombre=nombre,
            apellido=apellido,
            id_cooperativa=id_cooperativa,disco=disco,
            cedula=cedula,
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
        return redirect(url_for('main.listar_conductores'))
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    return render_template('conductor/add_conductor.html',cooperativas=cooperativas)

@main_bp.route('/conductores/editar/<int:id>', methods=['GET', 'POST'])
def editar_conductor(id):
    conductor = Conductor.query.get_or_404(id)
    if request.method == 'POST':
        conductor.nombre = request.form.get('nombre')
        conductor.apellido = request.form.get('apellido')
        conductor.disco = request.form.get('disco')
        conductor.id_unidad = request.form.get('id_unidad')
        conductor.licencia = request.form.get('licencia')
        conductor.fecha_nacimiento = request.form.get('fecha_nacimiento')
        conductor.direccion = request.form.get('direccion')
        conductor.telefono = request.form.get('telefono')
        conductor.email = request.form.get('email')
        conductor.fecha_contratacion = request.form.get('fecha_contratacion')
       

        db.session.commit()
        flash('Conductor actualizado exitosamente.')
        return redirect(url_for('main.listar_conductores'))
    unidades = Unidad.query.filter(Unidad.estado != 0).all()
    return render_template('conductor/edit_conductor.html', conductor=conductor,unidades=unidades)



@main_bp.route('/conductores/eliminar/<int:id>', methods=['POST'])
def eliminar_conductor(id):
    conductores = Conductor.query.get(id)
    if conductores: 
        conductores.estado = 0  # Cambiar el estado a '0'
        db.session.commit()
        flash('Conductor eliminado exitosamente.')
    return redirect(url_for('main.listar_conductores'))

# # CRUD para Ruta

@main_bp.route('/rutas', methods=['GET'])
def ruta_list():
    rutas = Ruta.query.filter(Ruta.estado != 0).all()
    return render_template('ruta/ruta_list.html', rutas=rutas)

@main_bp.route('/rutas/add', methods=['GET', 'POST'])
def ruta_add():
    if request.method == 'POST':
        data = request.form.get
        nueva_ruta = Ruta(
            id_unidad=data('id_unidad'),
            id_cooperativa=data('id_cooperativa'),
            estado=1 ,
            lugar_origen=data('lugar_origen'),
            lugar_destino=data('lugar_destino'),
            fecha_creacion=datetime.now()
        )
        db.session.add(nueva_ruta)
        db.session.commit()
        return redirect(url_for('main.ruta_list'))
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    unidades = Unidad.query.filter(Unidad.estado != 0).all()
    return render_template('ruta/ruta_add.html',cooperativas=cooperativas,unidades=unidades)

@main_bp.route('/rutas/edit/<int:id>', methods=['GET', 'POST'])
def ruta_edit(id):
    ruta = Ruta.query.get(id)
    if request.method == 'POST':
        data = request.form
        ruta.id_unidad = data.get('id_unidad', ruta.id_unidad)
        ruta.id_cooperativa = data.get('id_cooperativa', ruta.id_cooperativa)
        ruta.lugar_origen = data.get('lugar_origen', ruta.lugar_origen)
        ruta.lugar_destino = data.get('lugar_destino', ruta.lugar_destino)
        db.session.commit()
        return redirect(url_for('main.ruta_list'))
    cooperativas = Cooperativa.query.filter(Cooperativa.estado != 0).all()
    unidades = Unidad.query.filter(Unidad.estado != 0).all()
    return render_template('ruta/ruta_edit.html', ruta=ruta,cooperativas=cooperativas,unidades=unidades)

@main_bp.route('/rutas/delete/<int:id>', methods=['POST'])
def ruta_delete(id):
    rutas = Ruta.query.get(id)
    if rutas: 
        rutas.estado = 0  # Cambiar el estado a '0'
        rutas.fecha_eliminacion = datetime.now()
        db.session.commit()
        flash('ruta eliminada exitosamente.')
    db.session.commit()
    return redirect(url_for('main.ruta_list'))






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





# @main_bp.route('/generate_pdf/<int:id>', methods=['GET'])
# def generate_pdf(id):
#     # Consulta a la base de datos para obtener los datos del registro con el ID especificado
#     datos_registro = db.query(Registro).filter_by(id=id).first()

#     # Renderiza el template HTML con los datos del registro
#     html = render_template('template.html', registro=datos_registro)

#     # Configura las opciones de pdfkit
#     options = {
#         'page-size': 'A4',
#         'argin-top': '0.5in',
#         'argin-right': '0.5in',
#         'argin-bottom': '0.5in',
#         'argin-left': '0.5in',
#         'encoding': 'UTF-8'
#     }

#     # Genera el archivo PDF
#     pdf = pdfkit.from_string(html, False, options=options)

#     # Devuelve el archivo PDF como respuesta
#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename="documento.pdf"'
#     return response















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
