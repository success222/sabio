from datetime import datetime

from pydantic import BaseModel


class SourceBase(BaseModel):
    name: str
    slug: str
    rss_url: str
    website_url: str


class SourceRead(SourceBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True