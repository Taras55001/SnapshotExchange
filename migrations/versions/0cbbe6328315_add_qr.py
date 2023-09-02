"""add qr

Revision ID: 0cbbe6328315
Revises: 251d7982b553
Create Date: 2023-09-02 15:47:58.304902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0cbbe6328315'
down_revision: Union[str, None] = '251d7982b553'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Qr_codes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('photo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['photo_id'], ['photos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('photo_m2m_tags', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photo_m2m_tags', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_table('Qr_codes')
    # ### end Alembic commands ###