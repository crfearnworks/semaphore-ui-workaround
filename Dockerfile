FROM semaphoreui/semaphore:latest

# Create a new user
RUN useradd -m appuser

# Copy application files
COPY --chown=appuser:appuser /core /app/core
COPY --chown=appuser:appuser .env /app/.env

WORKDIR /app

ENV PYTHONPATH=/app:$PYTHONPATH

# Switch to the new user
USER appuser

WORKDIR /app/core

RUN pip install -r requirements/requirements.txt 

WORKDIR /app/core/setup

COPY --chown=appuser:appuser --chmod=777 /core/setup/config.json /app/core/setup

#COPY --chown=semaphore:semaphore .env /app
# Load environment variables and remove .env
RUN set -a && . /app/.env && set +a && rm /app/.env

RUN python semaphore_config.py