"""incluyo la cedula en conductor

Revision ID: adae64836fa5
Revises: 1bb0850a481b
Create Date: 2024-07-14 11:14:26.756281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adae64836fa5'
down_revision = '1bb0850a481b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conductores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cedula', sa.String(length=10), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conductores', schema=None) as batch_op:
        batch_op.drop_column('cedula')

    # ### end Alembic commands ###