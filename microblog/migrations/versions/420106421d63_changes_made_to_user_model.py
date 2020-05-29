"""Changes made to user model

Revision ID: 420106421d63
Revises: b653463b9d46
Create Date: 2020-05-18 18:24:34.463204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '420106421d63'
down_revision = 'b653463b9d46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
