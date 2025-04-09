FROM python:3.10-slim

WORKDIR /usr/src/APP

# Переменный пайтона
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Запуск
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]