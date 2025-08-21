FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8080

USER appuser
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]