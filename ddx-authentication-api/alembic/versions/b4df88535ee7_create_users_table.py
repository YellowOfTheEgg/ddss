"""create users table

Revision ID: b4df88535ee7
Revises: 
Create Date: 2019-06-25 12:23:45.012287

"""

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

# revision identifiers, used by Alembic.
revision = "b4df88535ee7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", UUID(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True) 
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_user_id"), table_name="user") 
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
