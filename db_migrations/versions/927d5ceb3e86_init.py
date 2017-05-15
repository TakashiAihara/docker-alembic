"""init

Revision ID: 927d5ceb3e86
Create Date: 2017-02-17 11:39:34.769993

"""

# revision identifiers, used by Alembic.
revision = '927d5ceb3e86'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participant',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('gender', sa.Enum('M', 'F', 'O', name='gender'), nullable=True),
    sa.Column('birth_date', sa.DATE(), nullable=True),
    sa.Column('age', sa.DECIMAL(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participant')
    # ### end Alembic commands ###
