from pydantic import BaseModel


class HealthStatus(BaseModel):
    """Standard health response shared across services."""

    service: str
    status: str = "ok"
    version: str = "v1"
