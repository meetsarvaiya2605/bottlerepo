"""test14

Revision ID: c60be3da46eb
Revises: 4ee4bcadb4c0
Create Date: 2025-03-13 12:25:49.453478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c60be3da46eb'
down_revision: Union[str, None] = '4ee4bcadb4c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bottles', sa.Column('last_recorded_amount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bottles', 'last_recorded_amount')
    # ### end Alembic commands ###
