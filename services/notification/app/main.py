from fastapi import FastAPI

from libs.schemas.v1 import HealthStatus, NotificationMessage


app = FastAPI(title="Notification Service")


@app.get("/health", response_model=HealthStatus)
def health() -> HealthStatus:
    return HealthStatus(service="notification")


@app.post("/notify", response_model=NotificationMessage)
def notify(message: NotificationMessage) -> NotificationMessage:
    return message
