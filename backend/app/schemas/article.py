from datetime import datetime

from pydantic import BaseModel


class ArticleResponse(BaseModel):
    id: int
    title: str
    summary: str | None = None
    source: str
    url: str
    published_at: datetime | None = None

    model_config = {
        "from_attributes": True
    }