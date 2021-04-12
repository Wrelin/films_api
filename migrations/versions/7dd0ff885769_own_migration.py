"""add age_rating

Revision ID: 7dd0ff885763
Revises: 0aa7cfedc9e7
Create Date: 2021-04-11 18:30:45.387036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = '7dd0ff885764'
down_revision = '7dd0ff885763'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET age_rating = 17
                WHERE title like '%Deathly Hallows%'
            """
        )
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET age_rating = NULL
                WHERE title like '%Deathly Hallows%'
            """
        )
    )
