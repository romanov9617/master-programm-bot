# 🚀 master-programm-bot

 Телеграм бот для ответов на вопросы абитуриентов.



### Особенности
1. Реализован парсинг сайтов с извлечением информации с сайтов прогамм ИТМО:
   * [Искусственный интеллект](https://abit.itmo.ru/program/master/ai)
   * [Управление ИИ-продуктами/AI Product](https://abit.itmo.ru/program/master/ai_product)
   
 Стек: BS4 + requests
 
2. Реализован парсинг учебных планов из pdf в pandas.Dataframe
   
   Стек: pdfplumber + pandas

3. Реализован простой Telegram бот, с несложным управлением

4. На данный момент, модель представлена в виде заглушки с хардкод вопросами.
 
### 🛠 Технологии

1. Python 3.9+

2. python-telegram-bot

3. Poetry

### ⚙️ Требования

Установленный Python 3.9 или выше

Poetry для управления зависимостями

### 📦 Установка

#### Клонируем репозиторий
```
git clone https://github.com/romanov9617/master-programm-bot.git
cd master-programm-bot
```

#### Устанавливаем зависимости
poetry install

### 🔧 Настройка

#### Создайте свою конфигурацию
```
 {
  "files": {
    "ai": "./plans/ai",
    "ai_product": "./plans/ai_product"
  },
  "bot": {
    "token": "YOUR_TOKEN"
  },
  "sites": {
    "ai": "https://abit.itmo.ru/program/master/ai",
    "ai_product": "https://abit.itmo.ru/program/master/ai_product"
  }
}
```
#### Создайте переменную окружения CONFIG_PATH с путем до файла конфига
`export CONFIG_PATH=./configs/config.json`


### 📂 Структура проекта
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
### ▶️ Запуск

`poetry run python main.py`
 или
`python main.py`


