from pydantic import BaseModel


class GatewayRoute(BaseModel):
    """Route mapping used by the gateway to forward requests."""

    path: str
    service: str
    url: str
