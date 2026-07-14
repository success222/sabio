from fastapi import FastAPI

from app.api.articles import router as article_router

app = FastAPI(
    title="Sabio API",
    version="0.0.1"
)

app.include_router(article_router)

@app.get("/")
def root():
    return{
        "message": "Welcome to Sabio API",
        "status": "Under active development."
    }