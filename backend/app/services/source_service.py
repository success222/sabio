from sqlalchemy.orm import Session

from app.models.source import Source


def get_active_sources(db: Session):
    """
    Retrieve all active news sources.
    """
    return (
        db.query(Source)
        .filter(Source.is_active.is_(True))
        .all()
    )


def get_source_by_slug(db: Session, slug: str):
    return (
        db.query(Source)
        .filter(Source.slug == slug)
        .first()
    )