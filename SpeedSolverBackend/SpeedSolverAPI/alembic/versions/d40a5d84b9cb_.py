"""empty message

Revision ID: d40a5d84b9cb
Revises: b8313aedc993
Create Date: 2024-12-09 15:12:30.049315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd40a5d84b9cb'
down_revision: Union[str, None] = 'b8313aedc993'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objectives', sa.Column('parent_objectiveId', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'objectives', 'objectives', ['parent_objectiveId'], ['objectiveId'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'objectives', type_='foreignkey')
    op.drop_column('objectives', 'parent_objectiveId')
    # ### end Alembic commands ###
