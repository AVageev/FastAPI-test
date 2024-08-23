FROM python:3.8-slim

# Устанавливаем рабочий каталог в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочий каталог
COPY requirements.txt /app/

# Устанавливаем зависимости, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочий каталог
COPY . /app/

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем сервер разработки FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

