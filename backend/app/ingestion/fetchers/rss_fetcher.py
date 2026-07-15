from email.utils import parsedate_to_datetime

import feedparser


def fetch_articles_from_source(source):
    feed = feedparser.parse(source.rss_url)

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
                "url": entry.link,
                "published_at": published,
                "source_id": source.id,
            }
        )

    return articles