"""test16

Revision ID: 36c97c5eb44c
Revises: 50a2661f102d
Create Date: 2025-03-13 17:33:38.709307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36c97c5eb44c'
down_revision: Union[str, None] = '50a2661f102d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userss', sa.Column('reminder_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userss', 'reminder_count')
    # ### end Alembic commands ###
