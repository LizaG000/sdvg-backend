# Импортируем образ для работы с питоном
FROM python:3.12.3

ENV PROJECT_PATH=/app

# создание папки, в которой будет последующая работа
WORKDIR $PROJECT_PATH

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
