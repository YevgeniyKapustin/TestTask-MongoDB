from fastapi import FastAPI

from src.forms.router import router as templates_router
from src import settings


app = FastAPI(
    title=settings.APP_TITLE,
    version='1.0',
)
app.include_router(templates_router)
