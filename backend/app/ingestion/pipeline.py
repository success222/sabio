from app.db.database import SessionLocal
from app.ingestion.fetchers.rss_fetcher import fetch_articles_from_source
from app.services.article_service import create_article_if_not_exists
from app.services.source_service import get_active_sources


def run_ingestion_pipeline():
    db = SessionLocal()

    try:
        sources = get_active_sources(db)

        for source in sources:
            print(f"Ingesting from {source.name}...")

            articles = fetch_articles_from_source(source)

            for article in articles:
                create_article_if_not_exists(db, article)

        print("Ingestion complete.")

    finally:
        db.close()