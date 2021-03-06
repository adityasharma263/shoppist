"""empty message

Revision ID: 90050e0c218f
Revises: 94d4b3b3b6c9
Create Date: 2018-06-28 18:29:47.672309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90050e0c218f'
down_revision = '94d4b3b3b6c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('display_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'display_name')
    # ### end Alembic commands ###
