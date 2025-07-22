from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import (
    ContextTypes,
)

PROGRAM_QUESTIONS = {
    "Искусственный интеллект": [
        # Общие вопросы
        "Какие ключевые курсы входят в программу «Искусственный интеллект»?",
        "В каком семестре читается «Глубокое обучение» и сколько у него ЗЕТ/часов?",
        "Сколько часов в целом отводится на проектный семинар?",
        "Какие компании-партнёры участвуют в учебных проектах?",
        # Вопросы на основе DataFrame учебного плана
        "В каком семестре проходит курс «Машинное обучение» и сколько в нём ЗЕТ/академических часов?",
        "Сколько академических часов у курса «Математическая статистика»?",
        "Сколько ЗЕТ начисляется за курс «Алгоритмы и структуры данных»?",
        "Какие дисциплины предусмотрены в 2-м семестре и сколько часов каждая из них занимает?",
    ],
    "Управление ИИ-продуктами": [
        # Общие вопросы
        "Какова структура программы «Управление ИИ-продуктами»?",
        "Какие дисциплины посвящены продуктовой аналитике и менеджменту?",
        "Сколько ЗЕТ в курсе «Стратегия развития AI-продукта»?",
        "Есть ли курсы по UX/UI для ML-продуктов?",
        # Вопросы на основе DataFrame учебного плана
        "В каком семестре читается курс «Стратегия развития AI-продукта» и сколько у него ЗЕТ?",
        "Сколько академических часов отведено на курс «Управление проектами AI»?",
        "Сколько ЗЕТ и часов занимают элективные дисциплины по выбору?",
        "Какие дисциплины предусмотрены в 1-м семестре и сколько часов по каждой?",
    ],
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton(p)] for p in PROGRAM_QUESTIONS.keys()]
    markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Выберите программу для работы:", reply_markup=markup
    )


async def program_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected = update.message.text
    if selected in PROGRAM_QUESTIONS:
        context.user_data["program"] = selected
        await update.message.reply_text(
            f"Вы выбрали программу: {selected}. Используйте команду /questions для списка вопросов."
        )
    else:
        await update.message.reply_text("Пожалуйста, выберите программу из списка.")


async def questions_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    program = context.user_data.get("program")
    if not program:
        await update.message.reply_text(
            "Сначала выберите программу через команду /start."
        )
        return
    questions = PROGRAM_QUESTIONS.get(program, [])
    text = "\n".join(f"- {q}" for q in questions)
    await update.message.reply_text(
        f"Возможные вопросы для программы «{program}»:\n{text}"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(
        f'Вы спросили: "{user_text}". (Заглушка: здесь будет обработка вашего вопроса на основе DataFrame и словаря.)'
    )
