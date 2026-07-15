from logging.handlers import RotatingFileHandler
import logging
from pathlib import Path

# backend/
BASE_DIR = Path(__file__).resolve().parents[2]

# backend/logs/
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "sabio.log"

logger = logging.getLogger("sabio")
logger.setLevel(logging.INFO)

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Print to terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Save to file
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)