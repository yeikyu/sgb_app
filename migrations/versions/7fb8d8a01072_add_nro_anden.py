"""add nro anden

Revision ID: 7fb8d8a01072
Revises: 503be8bf4893
Create Date: 2024-07-23 10:32:59.940696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fb8d8a01072'
down_revision = '503be8bf4893'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('andenes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nro_anden', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('andenes', schema=None) as batch_op:
        batch_op.drop_column('nro_anden')

    # ### end Alembic commands ###
