
from alembic import op
import sqlalchemy as sa

revision = 'properties'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_title', sa.String(length=255), nullable=False),
    sa.Column('property_description', sa.String(length=255), nullable=False),
    sa.Column('noOfRooms', sa.Integer(), nullable=False),
    sa.Column('noOfBathrooms', sa.Integer(), nullable=False),
    sa.Column('property_price', sa.String(length=255), nullable=False),
    sa.Column('property_location', sa.String(length=255), nullable=False),
    sa.Column('property_type', sa.String(length=255), nullable=False),
    sa.Column('property_imgFilename', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('properties')