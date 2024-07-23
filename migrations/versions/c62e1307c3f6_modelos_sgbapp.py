"""modelos sgbapp

Revision ID: c62e1307c3f6
Revises: 
Create Date: 2024-07-22 21:57:27.568735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c62e1307c3f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditorias',
    sa.Column('id_auditoria', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=True),
    sa.Column('modulo_afectado', sa.String(length=255), nullable=True),
    sa.Column('detalles_adicional', sa.String(length=500), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_auditoria')
    )
    op.create_table('categorias',
    sa.Column('id_categoria', sa.Integer(), nullable=False),
    sa.Column('nombre_categoria', sa.String(length=100), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_categoria')
    )
    op.create_table('ciudades',
    sa.Column('id_ciudad', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_ciudad')
    )
    op.create_table('cooperativas',
    sa.Column('id_cooperativa', sa.Integer(), nullable=False),
    sa.Column('razonsocial', sa.String(length=200), nullable=True),
    sa.Column('Ruc', sa.String(length=13), nullable=True),
    sa.Column('telefono', sa.String(length=10), nullable=True),
    sa.Column('direccion', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('usuariocreacion', sa.String(length=100), nullable=True),
    sa.Column('usuarioelimina', sa.String(length=100), nullable=True),
    sa.Column('fechacreacion', sa.DateTime(), nullable=True),
    sa.Column('fechaeliminacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_cooperativa')
    )
    op.create_table('medodosPago',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_eliminacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=True),
    sa.Column('valor', sa.Float(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('andenes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_cooperativa', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cooperativa'], ['cooperativas.id_cooperativa'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clientes',
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.Column('nombre_cliente', sa.String(length=255), nullable=False),
    sa.Column('apellido_cliente', sa.String(length=255), nullable=False),
    sa.Column('cedula', sa.String(length=13), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=False),
    sa.Column('direccion', sa.String(length=255), nullable=False),
    sa.Column('telefono', sa.String(length=255), nullable=False),
    sa.Column('ciudad', sa.Integer(), nullable=False),
    sa.Column('estado_cliente', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('cod_postal', sa.String(length=255), nullable=False),
    sa.Column('fecha_registro', sa.Date(), nullable=False),
    sa.Column('fecha_eliminacion', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['ciudad'], ['ciudades.id_ciudad'], ),
    sa.PrimaryKeyConstraint('id_cliente')
    )
    op.create_table('conductores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('cedula', sa.String(length=10), nullable=False),
    sa.Column('id_cooperativa', sa.Integer(), nullable=True),
    sa.Column('disco', sa.Integer(), nullable=True),
    sa.Column('licencia', sa.String(length=20), nullable=False),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=False),
    sa.Column('direccion', sa.String(length=200), nullable=True),
    sa.Column('telefono', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('fecha_contratacion', sa.Date(), nullable=False),
    sa.Column('estado_empleo', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_cooperativa'], ['cooperativas.id_cooperativa'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_cooperativa', sa.Integer(), nullable=True),
    sa.Column('user', sa.String(length=12), nullable=True),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('apellido', sa.String(length=100), nullable=True),
    sa.Column('contraseña', sa.String(length=10), nullable=True),
    sa.Column('usuariocreacion', sa.String(length=100), nullable=True),
    sa.Column('usuarioelimina', sa.String(length=100), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('fechacreacion', sa.DateTime(), nullable=True),
    sa.Column('fechaeliminacion', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_cooperativa'], ['cooperativas.id_cooperativa'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cab_factura',
    sa.Column('id_factura', sa.Integer(), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('id_vendedor', sa.Integer(), nullable=True),
    sa.Column('fecha_vta', sa.Date(), nullable=True),
    sa.Column('numero_factura', sa.String(length=20), nullable=True),
    sa.Column('cedula_o_ruc', sa.String(length=13), nullable=True),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('apellido', sa.String(length=100), nullable=True),
    sa.Column('razon_social', sa.String(length=255), nullable=True),
    sa.Column('direccion', sa.String(length=255), nullable=True),
    sa.Column('telefono', sa.String(length=10), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['clientes.id_cliente'], ),
    sa.PrimaryKeyConstraint('id_factura')
    )
    op.create_table('unidades',
    sa.Column('id_unidad', sa.Integer(), nullable=False),
    sa.Column('id_cooperativa', sa.Integer(), nullable=True),
    sa.Column('id_conductor', sa.Integer(), nullable=True),
    sa.Column('placa', sa.String(length=10), nullable=True),
    sa.Column('modelo', sa.String(length=30), nullable=True),
    sa.Column('ano', sa.Integer(), nullable=True),
    sa.Column('nro_disco', sa.Integer(), nullable=True),
    sa.Column('nrodeasientos', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('usuariocreacion', sa.String(length=100), nullable=True),
    sa.Column('usuarioelimina', sa.String(length=100), nullable=True),
    sa.Column('fechacreacion', sa.DateTime(), nullable=True),
    sa.Column('fechaeliminacion', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_conductor'], ['conductores.id'], ),
    sa.ForeignKeyConstraint(['id_cooperativa'], ['cooperativas.id_cooperativa'], ),
    sa.PrimaryKeyConstraint('id_unidad')
    )
    op.create_table('detalle_factura',
    sa.Column('id_detalle', sa.Integer(), nullable=False),
    sa.Column('id_factura', sa.Integer(), nullable=True),
    sa.Column('cod_producto', sa.String(length=20), nullable=True),
    sa.Column('nombre_producto', sa.String(length=350), nullable=True),
    sa.Column('numero_factura', sa.String(length=50), nullable=True),
    sa.Column('fecha_fact', sa.Date(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_factura'], ['cab_factura.id_factura'], ),
    sa.PrimaryKeyConstraint('id_detalle')
    )
    op.create_table('rutas',
    sa.Column('id_ruta', sa.Integer(), nullable=False),
    sa.Column('id_unidad', sa.Integer(), nullable=False),
    sa.Column('id_cooperativa', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('lugar_origen', sa.String(length=100), nullable=False),
    sa.Column('lugar_destino', sa.String(length=100), nullable=False),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=False),
    sa.Column('fecha_eliminacion', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_cooperativa'], ['cooperativas.id_cooperativa'], ),
    sa.ForeignKeyConstraint(['id_unidad'], ['unidades.id_unidad'], ),
    sa.PrimaryKeyConstraint('id_ruta')
    )
    op.create_table('calificaciones',
    sa.Column('id_calificacion', sa.Integer(), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('id_viaje', sa.Integer(), nullable=True),
    sa.Column('puntuacion', sa.Integer(), nullable=True),
    sa.Column('comentario_texto', sa.String(length=500), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['clientes.id_cliente'], ),
    sa.ForeignKeyConstraint(['id_viaje'], ['rutas.id_ruta'], ),
    sa.PrimaryKeyConstraint('id_calificacion')
    )
    op.create_table('comentarios',
    sa.Column('id_comentario', sa.Integer(), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('id_viaje', sa.Integer(), nullable=True),
    sa.Column('fecha_registro', sa.DateTime(), nullable=True),
    sa.Column('texto_comentario', sa.String(length=500), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['clientes.id_cliente'], ),
    sa.ForeignKeyConstraint(['id_viaje'], ['rutas.id_ruta'], ),
    sa.PrimaryKeyConstraint('id_comentario')
    )
    op.create_table('horarios',
    sa.Column('id_horario', sa.Integer(), nullable=False),
    sa.Column('id_ruta', sa.Integer(), nullable=True),
    sa.Column('id_autobus', sa.Integer(), nullable=True),
    sa.Column('hora_salida', sa.Time(), nullable=True),
    sa.Column('hora_llegada', sa.Time(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_autobus'], ['unidades.id_unidad'], ),
    sa.ForeignKeyConstraint(['id_ruta'], ['rutas.id_ruta'], ),
    sa.PrimaryKeyConstraint('id_horario')
    )
    op.create_table('itinerarios',
    sa.Column('id_itinerario', sa.Integer(), nullable=False),
    sa.Column('id_viaje', sa.Integer(), nullable=True),
    sa.Column('descripcion', sa.String(length=500), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_viaje'], ['rutas.id_ruta'], ),
    sa.PrimaryKeyConstraint('id_itinerario')
    )
    op.create_table('productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_ruta', sa.Integer(), nullable=True),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_eliminacion', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_ruta'], ['rutas.id_ruta'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boletos',
    sa.Column('id_boleto', sa.Integer(), nullable=False),
    sa.Column('cod_viaje', sa.String(length=20), nullable=True),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('id_horario', sa.Integer(), nullable=True),
    sa.Column('id_ruta', sa.Integer(), nullable=True),
    sa.Column('id_detalle', sa.Integer(), nullable=True),
    sa.Column('id_tasa', sa.Integer(), nullable=True),
    sa.Column('nro_factura', sa.String(length=255), nullable=True),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('oficina', sa.String(length=100), nullable=True),
    sa.Column('codigo', sa.String(length=255), nullable=True),
    sa.Column('asiento', sa.String(length=10), nullable=True),
    sa.Column('fecha_compra', sa.DateTime(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_eliminacion', sa.DateTime(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['clientes.id_cliente'], ),
    sa.ForeignKeyConstraint(['id_detalle'], ['productos.id'], ),
    sa.ForeignKeyConstraint(['id_horario'], ['horarios.id_horario'], ),
    sa.ForeignKeyConstraint(['id_ruta'], ['rutas.id_ruta'], ),
    sa.ForeignKeyConstraint(['id_tasa'], ['tasas.id'], ),
    sa.PrimaryKeyConstraint('id_boleto')
    )
    op.create_table('pagos',
    sa.Column('id_pago', sa.Integer(), nullable=False),
    sa.Column('id_metodo', sa.Integer(), nullable=True),
    sa.Column('id_reserva', sa.Integer(), nullable=True),
    sa.Column('monto', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('fechahora_pago', sa.DateTime(), nullable=True),
    sa.Column('estado_pago', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id_metodo'], ['medodosPago.id'], ),
    sa.ForeignKeyConstraint(['id_reserva'], ['boletos.id_boleto'], ),
    sa.PrimaryKeyConstraint('id_pago')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pagos')
    op.drop_table('boletos')
    op.drop_table('productos')
    op.drop_table('itinerarios')
    op.drop_table('horarios')
    op.drop_table('comentarios')
    op.drop_table('calificaciones')
    op.drop_table('rutas')
    op.drop_table('detalle_factura')
    op.drop_table('unidades')
    op.drop_table('cab_factura')
    op.drop_table('usuarios')
    op.drop_table('conductores')
    op.drop_table('clientes')
    op.drop_table('andenes')
    op.drop_table('tasas')
    op.drop_table('medodosPago')
    op.drop_table('cooperativas')
    op.drop_table('ciudades')
    op.drop_table('categorias')
    op.drop_table('auditorias')
    # ### end Alembic commands ###
