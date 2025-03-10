"""test4

Revision ID: 47b8d44b55f0
Revises: 2cab166d35bf
Create Date: 2025-03-10 10:24:16.539754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '47b8d44b55f0'
down_revision: Union[str, None] = '2cab166d35bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bottles', sa.Column('email_id', sa.String(), nullable=True))
    op.add_column('bottles', sa.Column('password', sa.String(), nullable=True))
    op.alter_column('bottles', 'bottle_capacity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('bottles', 'bottle_amount',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('bottles', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('now()'))
    op.create_unique_constraint(None, 'bottles', ['email_id'])
    op.create_unique_constraint(None, 'bottles', ['user_id'])
    op.alter_column('userss', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('userss', 'email_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('userss', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('userss', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('userss', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('userss', 'set_goal',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('userss', 'current_status',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('userss', 'notification_on',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('userss', 'notification_off',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('userss', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('now()'))
    op.alter_column('userss', 'updated_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('userss', 'updated_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('userss', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('userss', 'notification_off',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('userss', 'notification_on',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('userss', 'current_status',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('userss', 'set_goal',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('userss', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('userss', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('userss', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('userss', 'email_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('userss', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint(None, 'bottles', type_='unique')
    op.drop_constraint(None, 'bottles', type_='unique')
    op.alter_column('bottles', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('bottles', 'bottle_amount',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('bottles', 'bottle_capacity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('bottles', 'password')
    op.drop_column('bottles', 'email_id')
    # ### end Alembic commands ###
