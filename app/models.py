# app/models.py
from . import db
from datetime import datetime
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))
    apellido = db.Column(db.String(150))
    #bio = db.Column(db.Text)
    dni = db.Column(db.String(13))
    estado = db.Column(db.Integer)
    #fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #usuario_creacion = db.Column(db.String(15))
    #usuario_modificacion = db.Column(db.String(15))

    # Definir más campos según sea necesario
    def __repr__(self):
        return f'<Cliente {self.nombre}>'


class CategoriaProducto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    estado = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_creacion = db.Column(db.String(15))
    usuario_modificacion = db.Column(db.String(15))
    # Definir más campos según sea necesario
    def __repr__(self):
        return f'<CategoriaProducto {self.nombre}>'


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria_producto.id'), nullable=False)
    categoria = db.relationship('CategoriaProducto', backref=db.backref('categorias', lazy=True))
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float)
    estado = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #usuario_creacion = db.Column(db.String(15))
    #usuario_modificacion = db.Column(db.String(15))
    # Definir más campos según sea necesario
    def __repr__(self):
        return f'<Producto {self.nombre}>'


class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(100))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente', backref=db.backref('ventas', lazy=True))
    fecha_venta = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    estado = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_creacion = db.Column(db.String(15))
    usuario_modificacion = db.Column(db.String(15))

    # Definir más campos según sea necesario


class VentaDetalle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), nullable=False)
    venta = db.relationship('Venta', backref=db.backref('items', lazy=True))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    producto = db.relationship('Producto', backref=db.backref('venta_items', lazy=True))
    cantidad = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_creacion = db.Column(db.String(15))
    usuario_modificacion = db.Column(db.String(15))
    # Otros campos como precio unitario, descuento, etc.
