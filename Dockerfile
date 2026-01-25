# Dockerfile
FROM python:3.13
# Устанавливаем uv
RUN pip install --no-cache-dir uv

# Устанавливаем зависимости для asyncpg (PostgreSQL драйвер)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости
COPY pyproject.toml ./
# Если есть uv.lock — скопируйте и его:
# COPY uv.lock ./

# Устанавливаем Python-зависимости
RUN uv pip install --system --no-cache-dir .

# Копируем исходный код
COPY . .

# Создаём непривилегированного пользователя
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Запуск приложения
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]