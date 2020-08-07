# ------------------------------------------------------------
# create requirements.txt
# ------------------------------------------------------------
FROM python:3 AS pipenv
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

# ------------------------------------------------------------
# build actual container
# ------------------------------------------------------------
FROM python:3-slim

ENV TRIES=0 \
    RABBITMQ_URI="" \
    MONGO_URI="" \
    URL=""

# Install requirements
WORKDIR /usr/src
COPY --from=pipenv /tmp/requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt

# Copy application
COPY *.py checks.json /usr/src/

# Start application
CMD python /usr/src/main.py
