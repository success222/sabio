from sqlalchemy.orm import Session

from app.models.article import Article


def create_article_if_not_exists(db: Session, article_data: dict):
    """
    Save an article if it doesn't already exist.
    """

    existing = (
        db.query(Article)
        .filter(Article.url == article_data["url"])
        .first()
    )

    if existing:
        return None

    article = Article(**article_data)

    db.add(article)
    db.commit()
    db.refresh(article)

    return article

def get_all_articles(
    db: Session,
    skip: int = 0,
    limit: int = 20,
    source: str | None = None,
    search: str | None = None,
):
    """
    Retrieve articles with optional source filtering and pagination.
    """
    query = db.query(Article)
    
    if source:
        query = query.join(Article.source).filter_by(slug=source)
    
    if search:
        query = query.filter(
            Article.title.ilike(f"%{search}%")
        )
    
    return (
        query
        .order_by(Article.published_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )