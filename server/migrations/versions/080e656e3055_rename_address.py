"""rename address

Revision ID: 080e656e3055
Revises: 17b4d23dec78
Create Date: 2024-02-02 18:18:32.087976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '080e656e3055'
down_revision = '17b4d23dec78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')

    # ### end Alembic commands ###
