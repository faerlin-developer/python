import sqlalchemy

from db.database import DATABASE_URL

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
	"tasks",
	metadata,
	sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
	sqlalchemy.Column("body", sqlalchemy.String, nullable=False),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
