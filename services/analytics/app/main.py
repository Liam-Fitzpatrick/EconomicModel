from fastapi import FastAPI

from libs.schemas.v1 import AnalyticsEvent, HealthStatus


app = FastAPI(title="Analytics Service")


@app.get("/health", response_model=HealthStatus)
def health() -> HealthStatus:
    return HealthStatus(service="analytics")


@app.post("/events", response_model=AnalyticsEvent)
def ingest_event(event: AnalyticsEvent) -> AnalyticsEvent:
    return event
