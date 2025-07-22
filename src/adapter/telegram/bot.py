from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.adapter.config.config import config
from src.adapter.telegram.handlers.echo import (
    handle_message,
    program_choice,
    questions_list,
    start,
)

app = ApplicationBuilder().token(config.bot.token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("questions", questions_list))
# Update Filters to filters.TEXT and filters.COMMAND
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, program_choice), group=1
)
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message), group=2
)
