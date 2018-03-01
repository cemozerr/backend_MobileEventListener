"""empty message

Revision ID: 3de853d460bd
Revises: 
Create Date: 2018-02-28 15:46:01.401436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3de853d460bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transactionHash', sa.String(length=200), nullable=True),
    sa.Column('blockNumber', sa.Integer(), nullable=True),
    sa.Column('event', sa.String(length=50), nullable=True),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    # ### end Alembic commands ###
