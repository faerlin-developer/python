from databases import Database

DATABASE_URL = "sqlite:///./test.db"

_database = Database(DATABASE_URL)


def get_database() -> Database:
	return _database


async def database_connect():
	await _database.connect()


async def database_disconnect():
	await _database.disconnect()
