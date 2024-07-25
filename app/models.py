# app/models.py
from . import db
from datetime import datetime
from sqlalchemy.sql import func


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return f'<User {self.username}>'


# class Cliente(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(150))
#     apellido = db.Column(db.String(150))
#     #bio = db.Column(db.Text)
#     dni = db.Column(db.String(13))
#     estado = db.Column(db.Integer)
#     #fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
#     # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     #fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     #usuario_creacion = db.Column(db.String(15))
#     #usuario_modificacion = db.Column(db.String(15))

#     # Definir más campos según sea necesario
#     def __repr__(self):
#         return f'<Cliente {self.nombre}>'


# class CategoriaProducto(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100))
#     descripcion = db.Column(db.Text)
#     estado = db.Column(db.Integer)
#     fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
#     # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow)
#     usuario_creacion = db.Column(db.String(15))
#     usuario_modificacion = db.Column(db.String(15))
#     # Definir más campos según sea necesario
#     def __repr__(self):
#         return f'<CategoriaProducto {self.nombre}>'


# class Producto(db.Model):
#     id = db.Column(db.Integer, primary_key=True , autoincrement=True)
#     categoria_id = db.Column(db.Integer,  nullable=False)
#    # categoria_id = db.Column(db.Integer, db.ForeignKey('categoria_producto.id'), nullable=False)
#    # categoria = db.relationship('CategoriaProducto', backref=db.backref('categorias', lazy=True))
#     nombre = db.Column(db.String(100))
#     descripcion = db.Column(db.Text)
#     precio = db.Column(db.Float)
#     estado = db.Column(db.Integer)
#     fecha_creacion = db.Column(db.DateTime(timezone=True))
#     # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     fecha_modificacion = db.Column(db.DateTime, nullable=True)
#     #usuario_creacion = db.Column(db.String(15))
#     #usuario_modificacion = db.Column(db.String(15))
#     # Definir más campos según sea necesario
#     def __repr__(self):
#         return f'<Producto {self.nombre}>'


# class Venta(db.Model):
#     id = db.Column(db.Integer, primary_key=True ,autoincrement=True)
#     codigo = db.Column(db.String(100))
#     cliente_id = db.Column(db.Integer, nullable=False)
#     #cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
#     #cliente = db.relationship('Cliente', backref=db.backref('ventas', lazy=True))
#     fecha_venta = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     estado = db.Column(db.Integer)
#     fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
#     # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     fecha_modificacion = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
#     usuario_creacion = db.Column(db.String(15))
#     usuario_modificacion = db.Column(db.String(15))

    # Definir más campos según sea necesario


#class VentaDetalle(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), nullable=False)
   # venta = db.relationship('Venta', backref=db.backref('items', lazy=True))
   # producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
   # producto = db.relationship('Producto', backref=db.backref('venta_items', lazy=True))
   # cantidad = db.Column(db.Integer, nullable=False)
   # estado = db.Column(db.Integer)
   # fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #usuario_creacion = db.Column(db.String(15))
    #usuario_modificacion = db.Column(db.String(15))
    # Otros campos como precio unitario, descuento, etc.



class metodopago(db.Model):
    __tablename__ = 'medodospago'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    estado = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime)
    fecha_eliminacion = db.Column(db.DateTime)



# Instalar wkhtmltopdf en tu sistema desde el sitio web oficial: https://wkhtmltopdf.org/downloads.html

class Tasas(db.Model):
    __tablename__ = 'tasas'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    valor = db.Column(db.Float)
    estado = db.Column(db.Integer)


class Cooperativa(db.Model):
    __tablename__ = 'cooperativas'
    id_cooperativa = db.Column(db.Integer, primary_key=True)
    razonsocial = db.Column(db.String(200))
    Ruc = db.Column(db.String(13))
    telefono = db.Column(db.String(10))
    direccion = db.Column(db.String(200))
    email = db.Column(db.String(200))
    estado = db.Column(db.Integer)
    usuariocreacion = db.Column(db.String(100))
    usuarioelimina = db.Column(db.String(100))
    fechacreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaeliminacion = db.Column(db.DateTime)
    conductores = db.relationship('Conductor', backref='cond_cooperativa', lazy=True)
    unidades = db.relationship('Unidad', backref='unidad_cooperativa', lazy=True)
    ruta = db.relationship('Ruta', backref='rutacooperativa',lazy=True)
    andenes = db.relationship('Anden', backref='andencooperativa',lazy=True)
    
class Anden(db.Model):
    __tablename__ = 'andenes'
    id = db.Column(db.Integer,primary_key=True)
    nro_anden =db.Column(db.Integer)
    id_cooperativa =db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'))
    estado =db.Column(db.Integer)




class Conductor(db.Model):
    __tablename__ = 'conductores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(10), nullable=False)
    id_cooperativa = db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'))
    disco = db.Column(db.Integer)
    licencia = db.Column(db.String(20), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    direccion = db.Column(db.String(200), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fecha_contratacion = db.Column(db.Date, nullable=False)
    estado_empleo = db.Column(db.Integer, nullable=False)  # Por ejemplo: 'activo', 'suspendido', 'retirado'



class Unidad(db.Model):
    __tablename__ = 'unidades'
    id_unidad = db.Column(db.Integer, primary_key=True)
    id_cooperativa = db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'))
    id_conductor = db.Column(db.Integer,  db.ForeignKey('conductores.id'))
    placa = db.Column(db.String(10))
    modelo = db.Column(db.String(30))
    ano = db.Column(db.Integer)
    nro_disco = db.Column(db.Integer)
    nrodeasientos = db.Column(db.Integer)
    estado = db.Column(db.Integer)
    usuariocreacion = db.Column(db.String(100))
    usuarioelimina = db.Column(db.String(100))
    fechacreacion = db.Column(db.DateTime)
    fechaeliminacion = db.Column(db.DateTime)
    conductor = db.relationship('Conductor', foreign_keys=[id_conductor], backref='unidades_rel')
    ruta = db.relationship('Ruta', backref='ruta_unidad',lazy=True)
    horario = db.relationship('Horario', backref='horario_unidad',lazy=True)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    id_cooperativa = db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'))
    user = db.Column(db.String(12))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    contraseña = db.Column(db.String(10))
    usuariocreacion = db.Column(db.String(100))
    usuarioelimina = db.Column(db.String(100))
    estado = db.Column(db.Integer)
    fechacreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaeliminacion = db.Column(db.DateTime)
    

class Ciudad(db.Model):
    __tablename__ = 'ciudades'
    id_ciudad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Integer)
    clientes = db.relationship('Cliente', backref='ciudad_ref', lazy=True)
   

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(255), nullable=False)
    apellido_cliente = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.Integer, db.ForeignKey('ciudades.id_ciudad'), nullable=False)
    estado_cliente = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer)
    cod_postal = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False)
    fecha_eliminacion = db.Column(db.Date)
    boletos = db.relationship('Boleto', backref='cliente', lazy=True)
    comentarios = db.relationship('Comentario', backref='cliente_ref', lazy=True)
    calificaciones = db.relationship('Calificacion', backref='cliente_ref', lazy=True)


class Ruta(db.Model):
    __tablename__ = 'rutas'
    id_ruta = db.Column(db.Integer, primary_key=True)
    id_unidad = db.Column(db.Integer, db.ForeignKey('unidades.id_unidad'), nullable=False)
    id_cooperativa = db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'), nullable=False)
    estado = db.Column(db.Integer)
    lugar_origen = db.Column(db.String(100), nullable=False)
    lugar_destino = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_eliminacion = db.Column(db.DateTime)
    horarios = db.relationship('Horario', backref='ruta_ref', lazy=True)
    itinerarios = db.relationship('Itinerario', backref='ruta_ref', lazy=True)
    comentarios = db.relationship('Comentario', backref='ruta_ref', lazy=True)
    calificaciones = db.relationship('Calificacion', backref='ruta_ref', lazy=True)
    productos = db.relationship('Producto', backref='producto_ruta_ref', lazy=True)
class Horario(db.Model):
    __tablename__ = 'horarios'
    id_horario = db.Column(db.Integer, primary_key=True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    id_autobus = db.Column(db.Integer, db.ForeignKey('unidades.id_unidad'))
    hora_salida = db.Column(db.Time)
    hora_llegada = db.Column(db.Time)
    estado = db.Column(db.Integer)
    boletos = db.relationship('Boleto', backref='horario_ref', lazy=True)
    

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    Cod_Prod = db.Column(db.String(6))
    Cod_Aux = db.Column(db.String(10))
    id_ruta = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Numeric(10, 2))
    estado = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime)
    fecha_eliminacion = db.Column(db.DateTime)
    boletos = db.relationship('Boleto', backref='productos_ref', lazy=True)



class Boleto(db.Model):
    __tablename__ = 'boletos'
    id_boleto = db.Column(db.Integer, primary_key=True)
    cod_viaje = db.Column(db.String(20))
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_horario = db.Column(db.Integer, db.ForeignKey('horarios.id_horario'))
    id_ruta = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    id_detalle = db.Column(db.Integer, db.ForeignKey('productos.id'))
    id_tasa = db.Column(db.Integer, db.ForeignKey('tasas.id'))
    nro_factura = db.Column(db.String(255))
    descripcion = db.Column(db.String(100))
    cantidad =db.Column(db.Integer)
    oficina = db.Column(db.String(100))
    codigo = db.Column(db.String(255))
    asiento = db.Column(db.String(10))
    fecha_compra = db.Column(db.DateTime)
    fecha_creacion = db.Column(db.DateTime)
    fecha_eliminacion = db.Column(db.DateTime)
    estado = db.Column(db.Integer)
    pagos = db.relationship('Pago', backref='boleto_ref', lazy=True)
    productos = db.relationship('Producto', backref='boleto_ref', lazy=True)




class Pago(db.Model):
    __tablename__ = 'pagos'
    id_pago = db.Column(db.Integer, primary_key=True)
    id_metodo = db.Column(db.Integer,db.ForeignKey('medodospago.id'))
    id_reserva = db.Column(db.Integer, db.ForeignKey('boletos.id_boleto'))
    monto = db.Column(db.Numeric(10, 2))
    fechahora_pago = db.Column(db.DateTime, default=datetime.utcnow)
    estado_pago = db.Column(db.String(30))


class Itinerario(db.Model):
    __tablename__ = 'itinerarios'
    id_itinerario = db.Column(db.Integer, primary_key=True)
    id_viaje = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    descripcion = db.Column(db.String(500))
    estado = db.Column(db.Integer)

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id_comentario = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_viaje = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    texto_comentario = db.Column(db.String(500))
    estado = db.Column(db.Integer)

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'
    id_calificacion = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_viaje = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    puntuacion = db.Column(db.Integer)
    comentario_texto = db.Column(db.String(500))
    estado = db.Column(db.Integer)

class Categoria_cliente(db.Model):
    __tablename__ = 'categorias'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(100))
    estado = db.Column(db.Integer)



class PuntoDeEmision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    codigo_identificacion = db.Column(db.String(50), unique=True, nullable=False) # formato 002
    tipo = db.Column(db.String(50), nullable=False)
    equipos = db.Column(db.Text, nullable=True)  # Información sobre equipos en formato JSON o texto
    
    def __repr__(self):
        return f'<PuntoDeEmision {self.nombre}>'


class Establecimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False) 
    tipo = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    codigo_identificacion = db.Column(db.String(50), unique=True, nullable=False) # es 001 formato
    infraestructura = db.Column(db.Text, nullable=True)  # Información sobre infraestructura en formato JSON o texto
    horarios = db.Column(db.String(100), nullable=True)  # Horarios de apertura y cierre

    def __repr__(self):
        return f'<Establecimiento {self.nombre}>'





class CabFactura(db.Model):
    __tablename__ = 'cab_factura'
    id_factura = db.Column(db.Integer, primary_key=True)
    id_cooperativa = db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'))
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_responsable = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    fecha_vta = db.Column(db.Date)
    numero_factura = db.Column(db.String(20))
    estado = db.Column(db.Integer)
    detalles = db.relationship('DetalleFactura', backref='cab_factura_ref', lazy=True)

class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'
    id_detalle = db.Column(db.Integer, primary_key=True)
    id_factura = db.Column(db.Integer, db.ForeignKey('cab_factura.id_factura'))
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.Integer)


