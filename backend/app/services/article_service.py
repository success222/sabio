from sqlalchemy.orm import Session

from app.models.article import Article


def save_article(db: Session, article_data: dict):
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

def get_all_articles(db: Session):
    """
    Retrieve all articles from the database.
    """
    return (
        db.query(Article)
        .order_by(Article.published_at.desc())
        .all()
    )