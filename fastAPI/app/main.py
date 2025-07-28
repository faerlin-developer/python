from fastapi import FastAPI

import util.slog  # noqa: F401
from handlers.context import lifespan
from handlers.middleware import PreProcessRequest
from handlers.routes import router

app = FastAPI(lifespan=lifespan)

# noinspection PyTypeChecker
app.add_middleware(PreProcessRequest)
app.include_router(router)
