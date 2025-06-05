FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

ENV TRIES=0 \
    RABBITMQ_URI="" \
    MONGO_URI="" \
    PGURI="" \
    PGHUSER="" \
    PGPASSWORD="" \
    PGHOST="" \
    PGPORT="" \
    PGDATABASE="" \
    PGTABLE="" \
    URL=""

# Install requirements
WORKDIR /usr/src
COPY requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt

# Copy application
COPY *.py checks.json /usr/src/

# Start application
CMD python /usr/src/main.py
