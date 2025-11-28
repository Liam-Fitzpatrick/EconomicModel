FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY libs ./libs
COPY services/auth ./services/auth

RUN pip install --no-cache-dir -r services/auth/requirements.txt

EXPOSE 8001
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD \
  curl -f http://localhost:8001/health || exit 1

CMD ["uvicorn", "services.auth.app.main:app", "--host", "0.0.0.0", "--port", "8001"]
