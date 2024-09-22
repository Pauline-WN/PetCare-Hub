"""initial migration

Revision ID: 020389567212
Revises: c79a6df455c1
Create Date: 2024-09-23 00:17:05.397654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '020389567212'
down_revision: Union[str, None] = 'c79a6df455c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
