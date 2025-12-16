# Використовуємо образ, зазначений у конфігурації CircleCI
FROM python:3.10-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл залежностей
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код додатку
COPY . .

# Відкриваємо порт, на якому працює Flask
EXPOSE 5000

# Команда запуску
CMD ["python", "app.py"]
