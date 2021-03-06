"""rich_text_posts

Revision ID: 1403bb6e9a1a
Revises: 99acc29c0a57
Create Date: 2020-11-08 15:37:25.688569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1403bb6e9a1a'
down_revision = '99acc29c0a57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
