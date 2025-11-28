from fastapi import FastAPI

from libs.schemas.v1 import GatewayRoute, HealthStatus


app = FastAPI(title="Gateway Service")


@app.get("/health", response_model=HealthStatus)
def health() -> HealthStatus:
    return HealthStatus(service="gateway")


@app.get("/routes", response_model=list[GatewayRoute])
def list_routes() -> list[GatewayRoute]:
    return [
        GatewayRoute(path="/auth", service="auth", url="http://auth:8001"),
        GatewayRoute(path="/board", service="board", url="http://board:8002"),
        GatewayRoute(path="/card", service="card", url="http://card:8003"),
        GatewayRoute(path="/notification", service="notification", url="http://notification:8004"),
        GatewayRoute(path="/analytics", service="analytics", url="http://analytics:8005"),
    ]
