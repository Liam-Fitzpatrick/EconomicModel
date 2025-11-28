FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY libs ./libs
COPY services/notification ./services/notification

RUN pip install --no-cache-dir -r services/notification/requirements.txt

EXPOSE 8004
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD \
  curl -f http://localhost:8004/health || exit 1

CMD ["uvicorn", "services.notification.app.main:app", "--host", "0.0.0.0", "--port", "8004"]
