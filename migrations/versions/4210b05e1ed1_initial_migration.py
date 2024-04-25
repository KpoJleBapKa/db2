"""Initial migration

Revision ID: 4210b05e1ed1
Revises: 
Create Date: 2024-04-25 20:33:51.263559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '4210b05e1ed1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    op.alter_column('catalog', 'ComputerID',
               existing_type=mysql.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_constraint('catalog_ibfk_1', 'catalog', type_='foreignkey')
    op.alter_column('client', 'PhoneNumber',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('computer', 'SSD',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('computer', 'PSU',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('computer', 'GPU',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('computer', 'CPU',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('computer', 'RAM',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('computer', 'HDD',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('computer', 'Motherboard',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('orders', 'ClientPhoneNumber',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('warehouse', 'ComputerID',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('warehouse', 'ComputerID',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('orders', 'ClientPhoneNumber',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=True)
    op.alter_column('computer', 'Motherboard',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('computer', 'HDD',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('computer', 'RAM',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('computer', 'CPU',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('computer', 'GPU',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('computer', 'PSU',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('computer', 'SSD',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('client', 'PhoneNumber',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=True)
    op.create_foreign_key('catalog_ibfk_1', 'catalog', 'computer', ['ComputerID'], ['ID'])
    op.alter_column('catalog', 'ComputerID',
               existing_type=mysql.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.create_table('cart',
    sa.Column('ClientID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ComputerID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ClientID'], ['client.ID'], name='cart_ibfk_1'),
    sa.ForeignKeyConstraint(['ComputerID'], ['computer.ID'], name='cart_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
