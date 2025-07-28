from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.database import database_connect, database_disconnect


@asynccontextmanager
async def lifespan(app: FastAPI):
	print("Initialize resources")
	await database_connect()
	yield
	print("Tear down resources")
	await database_disconnect()
