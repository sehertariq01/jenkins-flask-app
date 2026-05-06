FROM python:3.10

RUN apt update && apt install -y chromium-driver chromium-browser

WORKDIR /tests

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "test_app.py"]