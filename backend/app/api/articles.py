from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from backend.app.ingestion.fetchers.rss_fetcher import fetch_articles
from app.schemas.article import ArticleResponse
from app.services.article_service import (
    get_all_articles,
    save_article,
)

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post("/import")
def import_articles(db: Session = Depends(get_db)):
    articles = fetch_articles()

    imported = 0
    duplicates = 0

    for article in articles:
        result = save_article(db, article)

        if result:
            imported += 1
        else:
            duplicates += 1

    return {
        "imported": imported,
        "duplicates": duplicates,
    }


@router.get("", response_model=list[ArticleResponse])
def list_articles(db: Session = Depends(get_db)):
    return get_all_articles(db)