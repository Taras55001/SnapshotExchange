"""add photo & tags

Revision ID: 09db308a3a3d
Revises: 692c63d675ca
Create Date: 2023-09-01 16:21:23.711382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09db308a3a3d'
down_revision: Union[str, None] = '692c63d675ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('photo_tags',
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photos.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    op.add_column('photos', sa.Column('url', sa.String(length=255), nullable=False))
    op.drop_column('photos', 'cloud_url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photos', sa.Column('cloud_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('photos', 'url')
    op.drop_table('photo_tags')
    op.drop_table('tags')
    # ### end Alembic commands ###