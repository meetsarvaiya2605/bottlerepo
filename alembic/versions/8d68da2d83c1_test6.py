"""test6

Revision ID: 8d68da2d83c1
Revises: 129a1b70ceac
Create Date: 2025-03-10 11:33:36.587266

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8d68da2d83c1"
down_revision: Union[str, None] = "129a1b70ceac"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("fillbottle", sa.Column("bottle_id", sa.Integer(), nullable=True))
    op.create_unique_constraint(None, "fillbottle", ["bottle_id"])
    op.create_foreign_key(None, "fillbottle", "bottles", ["bottle_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "fillbottle", type_="foreignkey")
    op.drop_constraint(None, "fillbottle", type_="unique")
    op.drop_column("fillbottle", "bottle_id")
    # ### end Alembic commands ###
