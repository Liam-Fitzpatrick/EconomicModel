# EconomicModel Microservices

This repository hosts a collection of FastAPI-based microservices plus a shared `libs/schemas` package used for cross-service DTOs. Each service exposes a simple health endpoint and minimal placeholder routes so you can iterate on functionality and contracts independently.

## Project layout

- `libs/` – shared Python packages
  - `libs/schemas/v1/` – versioned Pydantic DTOs (health, gateway routing, auth, board, card, notification, analytics)
- `services/` – microservices
  - `gateway/` – routes requests to downstream services
  - `auth/` – basic authentication placeholder
  - `board/` – board management placeholder
  - `card/` – card management placeholder
  - `notification/` – notification placeholder
  - `analytics/` – analytics event placeholder

## Service endpoints

Every service exposes `GET /health` returning `HealthStatus(service=<name>)`.

Additional sample routes:

- Gateway: `GET /routes` returns upstream mappings.
- Auth: `GET /users/{user_id}` returns a sample `UserProfile`.
- Board: `GET /boards/{board_id}` returns a sample `Board`.
- Card: `GET /cards/{card_id}` returns a sample `Card`.
- Notification: `POST /notify` accepts `Notification` payloads.
- Analytics: `POST /events` accepts `AnalyticsEvent` payloads.

## Running with Docker

Each service includes its own `Dockerfile` that:

- Installs FastAPI and Uvicorn
- Copies the shared `libs` package and the service code
- Exposes its port
- Adds a curl-based `HEALTHCHECK` hitting `/health`

Build and run commands per service (replace `<service>` with one of `gateway`, `auth`, `board`, `card`, `notification`, `analytics`):

```bash
# Build the image
cd services/<service>
docker build -t economicmodel-<service>:latest .

# Run the container
# Ports: gateway 8000, auth 8001, board 8002, card 8003, notification 8004, analytics 8005
docker run --rm -p <port>:<port> economicmodel-<service>:latest
```

Example (gateway):

```bash
cd services/gateway
docker build -t economicmodel-gateway:latest .
docker run --rm -p 8000:8000 economicmodel-gateway:latest
```

Once running, verify health:

```bash
curl http://localhost:<port>/health
```

## Testing

Each service provides a pytest skeleton under `services/<service>/tests/test_app.py`. To run tests locally (requires FastAPI dependencies available):

```bash
pytest
```

## Next steps

- Flesh out real business logic per service
- Add authentication/authorization where appropriate
- Introduce inter-service communication patterns and persistence layers
