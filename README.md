🚀 master-programm-bot

 Простой и расширяемый асинхронный Telegram-бот на Python с функцией эхо-сервиса.
 
🛠 Технологии

Python 3.9+

python-telegram-bot

Poetry

⚙️ Требования

Установленный Python 3.9 или выше

Poetry для управления зависимостями

📦 Установка

# Клонируем репозиторий
```
git clone https://github.com/romanov9617/master-programm-bot.git
cd master-programm-bot
```

# Устанавливаем зависимости
poetry install

🔧 Настройка

Создайте и экспортируйте токен вашего Telegram-бота:
```
  "bot": {
    "token": "YOUR_TOKEN"
  },
```

При необходимости настройте логирование и сценарии в папках configs/ и plans/.

📂 Структура проекта
```
master-programm-bot/
├── configs/                # Конфигурации (логи и др.)
├── plans/                  # Сценарии и шаблоны сообщений
├── src/                    # Исходный код
│   └── adapter/telegram/   # Модуль Telegram-бота
│       └── bot.py          # Инициализация и регистрация хендлеров
├── main.py                 # Запуск бота через polling
├── pyproject.toml          # Описание проекта и зависимостей (Poetry)
├── poetry.lock             # Фиксация версий зависимостей
└── .gitignore              # Исключённые файлы
```
▶️ Запуск

poetry run python main.py
# или
python main.py

💡 Расширение функционала

Откройте src/adapter/telegram/bot.py.

Импортируйте нужные классы:

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

Добавьте новый обработчик:

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я мастер-бот программы.")

app.add_handler(CommandHandler("start", start))

Перезапустите бота.
