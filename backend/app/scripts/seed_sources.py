from app.db.database import SessionLocal
from app.models.source import Source

db = SessionLocal()

def seed_sources():
    db = SessionLocal()
    sources = [
        {
            "name": "TechCabal",
            "slug": "techcabal",
            "rss_url": "https://techcabal.com/feed/",
            "website_url": "https://techcabal.com",
        },
        {
            "name": "Techpoint Africa",
            "slug": "techpoint-africa",
            "rss_url": "https://techpoint.africa/feed/",
            "website_url": "https://techpoint.africa",
        },
        {
            "name": "Disrupt Africa",
            "slug": "disrupt-africa",
            "rss_url": "https://disruptafrica.com/feed/",
            "website_url": "https://disruptafrica.com",
        },
    ]

    for source in sources:

        existing = (
            db.query(Source)
            .filter(Source.slug == source["slug"])
            .first()
        )

        if not existing:
            db.add(Source(**source))

    db.commit()
    db.close()

    print("Sources seeded successfully!")

if __name__ == "__main__":
    seed_sources()