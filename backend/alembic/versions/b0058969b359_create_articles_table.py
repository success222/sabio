"""create articles table

Revision ID: b0058969b359
Revises: 
Create Date: 2026-07-14 21:44:19.967288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0058969b359'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sources",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.Column("rss_url", sa.String(length=1000), nullable=False),
        sa.Column("website_url", sa.String(length=1000), nullable=False),
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("slug"),
    )

    op.create_index(
        "ix_sources_id",
        "sources",
        ["id"],
    )

    op.create_table(
        "articles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=500), nullable=False),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(length=1000), nullable=False),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["sources.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("url"),
    )

    op.create_index(
        "ix_articles_id",
        "articles",
        ["id"],
    )


def downgrade() -> None:
    op.drop_index("ix_articles_id", table_name="articles")
    op.drop_table("articles")

    op.drop_index("ix_sources_id", table_name="sources")
    op.drop_table("sources")
