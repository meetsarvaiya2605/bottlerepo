"""test11

Revision ID: 0897c44a365c
Revises: c2ef36ce4e16
Create Date: 2025-03-12 10:24:25.525419

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0897c44a365c"
down_revision: Union[str, None] = "c2ef36ce4e16"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "set_goal", ["id"])
    op.drop_column("userss", "current_status")
    op.drop_column("userss", "set_goal")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "userss",
        sa.Column("set_goal", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "userss",
        sa.Column("current_status", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "set_goal", type_="unique")
    # ### end Alembic commands ###
