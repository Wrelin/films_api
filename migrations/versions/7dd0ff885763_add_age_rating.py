"""add age_rating

Revision ID: 7dd0ff885763
Revises: 0aa7cfedc9e7
Create Date: 2021-04-11 18:30:45.387036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dd0ff885763'
down_revision = '0aa7cfedc9e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('age_rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'age_rating')
    # ### end Alembic commands ###
