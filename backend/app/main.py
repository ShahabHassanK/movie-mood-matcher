# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routers import questions, recommend
from backend.app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title="Movie Mood Matcher API",
        description="Personality-based movie recommendation engine",
        version="1.0.0"
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routers with prefix
    app.include_router(questions.router, prefix="/api")
    app.include_router(recommend.router, prefix="/api")

    @app.get("/")
    async def health_check():
        return {
            "status": "healthy",
            "version": app.version,
            "docs": {
                "swagger": "/docs",  # Updated to default paths
                "redoc": "/redoc"
            }
        }

    return app

app = create_app()