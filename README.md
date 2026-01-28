# PoetrySite

Сайт для публикации и чтения стихов.  
Простая платформа, где авторы выкладывают свои произведения, а читатели находят и читают поэзию.

### Технологии
- Фреймворк: **FastAPI**
- ORM: **SQLAlchemy**
- База данных: **PostgreSQL**
- Миграции: **Alembic**
- Пакетный менеджер: **uv**

### Структура проекта

```
PoetrySite/
├── app/
│   ├── api/          # роутеры FastAPI
│   ├── Models/       # SQLAlchemy модели
│   ├── Schemas/      # Pydantic схемы
│   ├── Services/     # бизнес-логика
│   └── DataBase/     # подключение к БД, init_db.py
├── Alembic/       # Alembic: файлы миграций
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── alembic.ini       # конфигурация Alembic
├── main.py           # точка входа FastAPI
├── .env.example
├── docker-compose.yml
├── uv.lock # файл с зависимостями
└── README.md
```

### Текущий статус

| Функционал                        | Статус        |
|-----------------------------------|---------------|
| Регистрация / вход + JWT          | Сделано       |
| CRUD стихотворений                | Сделано       |
| Настройка Docker                  | Сделано       |
| Подключение к Redis               | Запланировано |
| Тесты                             | Запланировано |

### Запуск проекта

1. Клонируем репозиторий
```bash
git clone https://github.com/Artonkes/PoetrySite.git
cd PoetrySite
```

2. Настраиваем .env
```bash
cp .env.example .env
```
Отредактируй `.env` (обязательно SECRET_KEY и данные БД).

#### Через uv

```bash
# Установка uv (если нужно)
curl -LsSf https://astral.sh/uv/install.sh | sh

uv sync
uv run app/DataBase/init_db.py     # создать таблицы
uv run main.py                     # запуск
```

→ http://127.0.0.1:8000/docs

#### Через Docker

```bash
docker compose up -d
docker compose exec web uv run app/DataBase/init_db.py
```

→ http://127.0.0.1:8000/docs
