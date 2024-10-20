FROM python:3.13.0

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
    libpq-dev \
    gdal-bin \
    binutils \
    postgresql-client

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY dutch_municipalities/ .

CMD ["sh", "-c", "python manage.py makemigrations api && python manage.py migrate api && python manage.py runserver 0.0.0.0:8000"]