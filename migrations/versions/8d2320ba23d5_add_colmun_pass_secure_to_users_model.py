"""add colmun pass_secure to users model

Revision ID: 8d2320ba23d5
Revises: d29b9ea924a4
Create Date: 2018-11-17 21:25:10.873111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d2320ba23d5'
down_revision = 'd29b9ea924a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###