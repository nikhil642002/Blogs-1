"""Initial Migration

Revision ID: 299fb49c2830
Revises: 
Create Date: 2019-03-04 15:41:22.231319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '299fb49c2830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('title', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'title')
    # ### end Alembic commands ###