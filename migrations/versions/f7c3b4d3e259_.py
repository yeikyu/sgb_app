"""empty message

Revision ID: f7c3b4d3e259
Revises: 176e9bdfc958
Create Date: 2024-06-11 09:09:26.171116

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f7c3b4d3e259'
down_revision = '176e9bdfc958'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.drop_column('bio')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', mysql.TEXT(), nullable=True))

    # ### end Alembic commands ###
