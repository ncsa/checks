FROM python:3.8-slim

# We are going to build the postgres psycopg2 library from source
# so we need postgres binaries and gcc
RUN apt-get update && apt-get install -y libpq-dev build-essential

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

ARG VERSION="unknown"
ARG GITSHA1="unknown"

LABEL org.opencontainers.image.title="Container to be used as init containers to check if the service is ready"
LABEL org.opencontainers.image.authors="Rob Kooper <kooper@illinois.edu"
LABEL org.opencontainers.image.source="https://github.com/ncsa/checks"
LABEL org.opencontainers.image.version="${VERSION}"
LABEL org.opencontainers.image.revision="${GITSHA1}"

# Install requirements
WORKDIR /usr/src
COPY requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt

# Copy application
COPY *.py checks.json /usr/src/

# Start application
CMD python /usr/src/main.py
