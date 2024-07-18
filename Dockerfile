FROM semaphoreui/semaphore:latest

# Copy application files
COPY /core /app/core
COPY .env /app/.env

WORKDIR /app

ENV PYTHONPATH=/app:$PYTHONPATH

WORKDIR /app/core

RUN pip install -r requirements/requirements.txt 

WORKDIR /app/core/setup

COPY --chmod=777 /core/setup/config.json /app/core/setup

RUN python semaphore_config.py