from datetime import datetime

from pydantic import BaseModel, ConfigDict


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
        
class SourceResponse(BaseModel):
    id: int
    name: str
    slug: str

    model_config = ConfigDict(from_attributes=True)