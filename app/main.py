from typing import Union
import os
import logging
from fastapi import FastAPI
from route import router

CORS_ALLOW_ORIGINS = os.environ.get("CORS_ALLOW_ORIGINS", "*")

app = FastAPI()

logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(router)
