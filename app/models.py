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
    
    
class Conductor(db.Model):
     __tablename__ = 'conductores'
     id = db.Column(db.Integer, primary_key=True)
     nombre = db.Column(db.String(100), nullable=False)
     apellido = db.Column(db.String(100), nullable=False)
     id_cooperativa = db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'))
     licencia = db.Column(db.String(20), nullable=False)
     fecha_nacimiento = db.Column(db.Date, nullable=False)
     direccion = db.Column(db.String(200), nullable=True)
     telefono = db.Column(db.String(15), nullable=True)
     email = db.Column(db.String(120), unique=True, nullable=False)
     fecha_contratacion = db.Column(db.Date, nullable=False)
     estado_empleo = db.Column(db.String(20), nullable=False)  # Por ejemplo: 'activo', 'suspendido', 'retirado'
     cooperativa = db.relationship('Cooperativa', backref=db.backref('conductores', lazy=True))
     
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


class Unidad(db.Model):
    __tablename__ = 'unidades'
    id_unidad = db.Column(db.Integer, primary_key=True)
    id_conductor = db.Column(db.Integer, db.ForeignKey('conductores.id'))
    id_cooperativa = db.Column(db.Integer, db.ForeignKey('cooperativas.id_cooperativa'))
    placa = db.Column(db.String(10))
    modelo = db.Column(db.String(30))
    ano = db.Column(db.Integer)
    nro_disco = db.Column(db.Integer)
    nrodeasientos = db.Column(db.Integer)
    estado = db.Column(db.Integer)
    usuariocreacion = db.Column(db.String(100))
    usuarioelimina = db.Column(db.String(100))
    fechacreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaeliminacion = db.Column(db.DateTime)
    cooperativa = db.relationship('Cooperativa', backref=db.backref('unidades', lazy=True))


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(12))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    contraseña = db.Column(db.String(10))
    usuariocreacion = db.Column(db.String(100))
    usuarioelimina = db.Column(db.String(100))
    estado = db.Column(db.Integer)
 #   id_unidad = db.Column(db.Integer, db.ForeignKey('unidades.id_unidad'))
    fechacreacion = db.Column(db.DateTime, default=datetime.utcnow)
    fechaeliminacion = db.Column(db.DateTime)
   # unidad = db.relationship('Unidad', backref=db.backref('usuarios', lazy=True))


class Ciudad(db.Model):
    __tablename__ = 'ciudades'
    id_ciudad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Integer)


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
    ciudad = db.Column(db.Integer, db.ForeignKey('ciudad.id_ciudad'), nullable=False)
    estado_cliente = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer)
    cod_postal = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False)
    fecha_eliminacion = db.Column(db.Date)
    ciudad_rel = db.relationship('Ciudad', backref=db.backref('cliente', lazy=True))


class Destino(db.Model):
    __tablename__ = 'destinos'
    id_destino = db.Column(db.Integer, primary_key=True)
    ubicacion = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.Integer, db.ForeignKey('ciudad.id_ciudad'), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    fecha_creacion = db.Column(db.Date, nullable=False)
    fecha_modificacion = db.Column(db.Date, nullable=False)
    fecha_eliminacion = db.Column(db.Date)
    ciudad_rel = db.relationship('Ciudad', backref=db.backref('destinos', lazy=True))


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
    hora_salida = db.Column(db.Time, nullable=False)
    hora_llegada = db.Column(db.Time, nullable=False)
    unidad = db.relationship('Unidad', backref=db.backref('rutas', lazy=True))
    cooperativa = db.relationship('Cooperativa', backref=db.backref('rutas', lazy=True))


class Horario(db.Model):
    __tablename__ = 'horarios'
    id_horario = db.Column(db.Integer, primary_key=True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    id_autobus = db.Column(db.Integer, db.ForeignKey('unidades.id_unidad'))
    hora_salida = db.Column(db.Time)
    hora_llegada = db.Column(db.Time)
    estado = db.Column(db.Integer)
    ruta = db.relationship('Ruta', backref=db.backref('horarios', lazy=True))
    autobus = db.relationship('Unidad', backref=db.backref('horarios', lazy=True))


class Boleto(db.Model):
    __tablename__ = 'boletos'
    id_boleto = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_horario = db.Column(db.Integer, db.ForeignKey('horarios.id_horario'))
    asiento = db.Column(db.String(10))
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow)
    precio = db.Column(db.Numeric(10, 2))
    estado = db.Column(db.Integer)
    cliente = db.relationship('Cliente', backref=db.backref('boletos', lazy=True))
    horario = db.relationship('Horario', backref=db.backref('boletos', lazy=True))


class Pago(db.Model):
    __tablename__ = 'pagos'
    id_pago = db.Column(db.Integer, primary_key=True)
    id_reserva = db.Column(db.Integer, db.ForeignKey('boletos.id_boleto'))
    metodo_pago = db.Column(db.String(30))
    monto = db.Column(db.Numeric(10, 2))
    fechahora_pago = db.Column(db.DateTime, default=datetime.utcnow)
    estado_pago = db.Column(db.String(30))
    estado = db.Column(db.Integer)
    reserva = db.relationship('Boleto', backref=db.backref('pagos', lazy=True))


class Auditoria(db.Model):
    __tablename__ = 'auditorias'
    id_auditoria = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))
    modulo_afectado = db.Column(db.String(255))
    detalles_adicional = db.Column(db.String(500))
    estado = db.Column(db.Integer)


class Itinerario(db.Model):
    __tablename__ = 'itinerarios'
    id_itinerario = db.Column(db.Integer, primary_key=True)
    id_viaje = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    descripcion = db.Column(db.String(500))
    estado = db.Column(db.Integer)
    viaje = db.relationship('Ruta', backref=db.backref('itinerarios', lazy=True))


class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id_comentario = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_viaje = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    texto_comentario = db.Column(db.String(500))
    estado = db.Column(db.Integer)
    cliente = db.relationship('Cliente', backref=db.backref('comentarios', lazy=True))
    viaje = db.relationship('Ruta', backref=db.backref('comentarios', lazy=True))


class Calificacion(db.Model):
    __tablename__ = 'calificaciones'
    id_calificacion = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_viaje = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))
    puntuacion = db.Column(db.Integer)
    comentario_texto = db.Column(db.String(500))
    estado = db.Column(db.Integer)
    cliente = db.relationship('Cliente', backref=db.backref('calificaciones', lazy=True))
    viaje = db.relationship('Ruta', backref=db.backref('calificaciones', lazy=True))


class Categoria(db.Model):
    __tablename__ = 'categorias'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(100))
    estado = db.Column(db.Integer)


class CabFactura(db.Model):
    __tablename__ = 'cab_factura'
    id_factura = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_vendedor = db.Column(db.Integer)
    fecha_vta = db.Column(db.Date)
    numero_factura = db.Column(db.String(20))
    cedula_o_ruc = db.Column(db.String(13))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    razon_social = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(10))
    estado = db.Column(db.Integer)
    cliente = db.relationship('Cliente', backref=db.backref('cab_factura', lazy=True))


class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'
    id_detalle = db.Column(db.Integer, primary_key=True)
    id_factura = db.Column(db.Integer, db.ForeignKey('cab_factura.id_factura'))
    cod_producto = db.Column(db.String(20))
    nombre_producto = db.Column(db.String(350))
    numero_factura = db.Column(db.String(50))
    fecha_fact = db.Column(db.Date)
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.Integer)
    cab_factura = db.relationship('CabFactura', backref=db.backref('detalle_factura', lazy=True))
