from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.source import SourceResponse


class ArticleResponse(BaseModel):
    id: int
    title: str
    summary: str | None = None
    source: SourceResponse
    url: str
    published_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)