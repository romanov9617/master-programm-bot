import logging

from telegram import Update
from telegram.ext import (
    ContextTypes,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! Я асинхронный эхо-бот. Напиши что-нибудь, и я повторю это."
    )


# Async echo handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    text = update.message.text
    await update.message.reply_text(text)


# Async error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
