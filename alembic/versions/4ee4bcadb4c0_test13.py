"""test13

Revision ID: 4ee4bcadb4c0
Revises: 121a8e9240e9
Create Date: 2025-03-13 12:02:14.655944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ee4bcadb4c0'
down_revision: Union[str, None] = '121a8e9240e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('set_goal', 'current_status')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('set_goal', sa.Column('current_status', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
