from datetime import datetime
from email.utils import parsedate_to_datetime

import feedparser

RSS_URL = "https://techcabal.com/feed/"


def fetch_articles():
    feed = feedparser.parse(RSS_URL)

    articles = []

    for entry in feed.entries:
        published = None

        if hasattr(entry, "published"):
            try:
                published = parsedate_to_datetime(entry.published)
            except Exception:
                published = None

        articles.append(
            {
                "title": entry.title,
                "summary": getattr(entry, "summary", None),
                "source": "TechCabal",
                "url": entry.link,
                "published_at": published,
            }
        )

    return articles