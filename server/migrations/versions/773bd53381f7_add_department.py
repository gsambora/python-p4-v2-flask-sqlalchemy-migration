"""add Department

Revision ID: 773bd53381f7
Revises: 1a1fc7c8d375
Create Date: 2024-02-08 15:02:27.831110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '773bd53381f7'
down_revision = '1a1fc7c8d375'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
