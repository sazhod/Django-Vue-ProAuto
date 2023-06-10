# Python
FROM python:3.11

WORKDIR /proauto

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "212.113.117.97:8000"]