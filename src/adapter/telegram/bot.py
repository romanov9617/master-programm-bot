from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.adapter.config.config import config
from src.adapter.telegram.handlers.echo import echo, error_handler, start

app = ApplicationBuilder().token(config.bot.token).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.add_error_handler(error_handler)
