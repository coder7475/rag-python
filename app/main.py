from fastapi import FastAPI
from app.config import settings
from ingest_data import ingest_data
from create_vector_index import create_vector_index

# Initialize FastAPI application
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


# Root route
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


@app.get("/env-test")
def test_env_vars():
    """Test endpoint to verify environment variables are loaded correctly"""
    return {
        "app_settings": {
            "name": settings.app_name,
            "version": settings.app_version,
            "debug": settings.debug,
        },
        "server_settings": {"host": settings.host, "port": settings.port},
        "database_url": settings.database_url.replace(settings.secret_key, "****")
        if settings.secret_key in settings.database_url
        else settings.database_url,
    }


@app.get("/ingest-data")
async def chunk_pdf():
    "Take the pdf and chunk it into 400 character pieces"
    result = await ingest_data()
    print(result)
    return {
        "message": "Data ingested successfully!",
    }


@app.get("/create-index")
def create_index():
    "Create a vector search index in MongoDB Atlas"
    create_vector_index()
    return {"message": "Index created successfully!"}
