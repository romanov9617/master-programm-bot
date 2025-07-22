import logging

from src.adapter.telegram.bot import app

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Start the bot (async)
    logger.info("Starting async echo bot...")
    app.run_polling()
