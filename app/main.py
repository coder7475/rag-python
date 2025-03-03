from fastapi import FastAPI, Depends
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


@app.get("/")
async def root():
    return {"message": f"Wecome to {settings.app_name}!"}


@app.get("/info")
def app_info():
    """Returns application information from environment variables"""
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "debug_mode": settings.debug,
        "api_prefix": settings.api_prefix,
    }
