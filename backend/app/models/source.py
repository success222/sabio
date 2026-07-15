from sqlalchemy import Boolean, Column, DateTime, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False, unique=True)

    slug = Column(String(100), nullable=False, unique=True, index=True)

    rss_url = Column(String(1000), nullable=False)

    website_url = Column(String(1000), nullable=False)
    
    is_active = Column(
        Boolean,
        nullable=False,
        #default=True,
        server_default=text("true"),
    )
   
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    articles = relationship(
        "Article",
        back_populates="source",
        #cascade="all, delete-orphan",
    )