from contextlib import asynccontextmanager
from fastapi import FastAPI
import os

from routers import repo_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure repos directory exists
    os.makedirs(os.getenv("REPOS_PATH", "./repos"), exist_ok=True)
    yield

app = FastAPI(
    title="Code Architect API",
    description="API for managing and analyzing code repositories",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(repo_router.router, prefix="/api/v1", tags=["repositories"])
