FROM python:3.11-slim

WORKDIR /app

COPY greatest.py .

CMD ["python", "greatest.py"]