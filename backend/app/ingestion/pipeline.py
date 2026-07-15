import time

from app.core.logging import logger
from app.db.database import SessionLocal
from app.ingestion.fetchers.rss_fetcher import fetch_articles_from_source
from app.services.article_service import create_article_if_not_exists
from app.services.source_service import get_active_sources


def run_ingestion_pipeline():
    db = SessionLocal()

    start_time = time.perf_counter()

    total_imported = 0
    total_duplicates = 0

    logger.info("=" * 60)
    logger.info("Starting ingestion pipeline")
    logger.info("=" * 60)

    try:
        sources = get_active_sources(db)

        for source in sources:

            try:
                logger.info(f"Ingesting articles from {source.name}")

                imported = 0
                duplicates = 0

                articles = fetch_articles_from_source(source)

                for article in articles:

                    result = create_article_if_not_exists(db, article)

                    if result:
                        imported += 1
                    else:
                        duplicates += 1

                total_imported += imported
                total_duplicates += duplicates

                logger.info(
                    f"{source.name}: imported={imported}, duplicates={duplicates}"
                )

            except Exception:
                logger.exception(
                    f"Failed to ingest articles from {source.name}"
                )

        elapsed = time.perf_counter() - start_time

        logger.info("=" * 60)
        logger.info("Ingestion completed successfully")
        logger.info(f"Total imported: {total_imported}")
        logger.info(f"Total duplicates: {total_duplicates}")
        logger.info(f"Completed in {elapsed:.2f} seconds")
        logger.info("=" * 60)

    finally:
        db.close()