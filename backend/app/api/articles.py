from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.ingestion.pipeline import run_ingestion_pipeline
from app.schemas.article import ArticleResponse
from app.services.article_service import get_all_articles

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post("/import")
def import_articles():
    run_ingestion_pipeline()

    return {
        "message": "Ingestion completed successfully."
    }


@router.get("", response_model=list[ArticleResponse])
def list_articles(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    source: str | None = Query(None),
    search: str | None = Query(None),
    db: Session = Depends(get_db),
):
    return get_all_articles(
        db=db,
        skip=skip,
        limit=limit,
        source=source,
        search=search,
    )