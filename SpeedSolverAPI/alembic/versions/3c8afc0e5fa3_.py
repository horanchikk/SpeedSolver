"""empty message

Revision ID: 3c8afc0e5fa3
Revises: 947fe4fd803f
Create Date: 2024-11-22 16:00:01.197457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c8afc0e5fa3'
down_revision: Union[str, None] = '947fe4fd803f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pronounces',
    sa.Column('pronounceId', sa.UUID(), nullable=False),
    sa.Column('pronounceName', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('pronounceId'),
    sa.UniqueConstraint('pronounceName')
    )
    op.add_column('profiles', sa.Column('surname', sa.String(), nullable=False))
    op.add_column('profiles', sa.Column('name', sa.String(), nullable=False))
    op.add_column('profiles', sa.Column('patronymic', sa.String(), nullable=False))
    op.add_column('profiles', sa.Column('pronounceId', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'profiles', 'pronounces', ['pronounceId'], ['pronounceId'])
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'email')
    op.drop_constraint(None, 'profiles', type_='foreignkey')
    op.drop_column('profiles', 'pronounceId')
    op.drop_column('profiles', 'patronymic')
    op.drop_column('profiles', 'name')
    op.drop_column('profiles', 'surname')
    op.drop_table('pronounces')
    # ### end Alembic commands ###
