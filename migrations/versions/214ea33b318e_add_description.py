"""add description

Revision ID: 214ea33b318e
Revises: eb6eef5cdee5
Create Date: 2023-08-31 14:32:18.939651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '214ea33b318e'
down_revision: Union[str, None] = 'eb6eef5cdee5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blacklist_tokens', 'blacklisted_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('users', sa.Column('description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'description')
    op.alter_column('blacklist_tokens', 'blacklisted_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###