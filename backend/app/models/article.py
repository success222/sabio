from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.db.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(500), nullable=False)

    summary = Column(Text)

    source = Column(String(255), nullable=False)

    url = Column(String(1000), unique=True, nullable=False)

    published_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )