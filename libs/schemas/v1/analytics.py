from pydantic import BaseModel


class AnalyticsEvent(BaseModel):
    """Event reported to analytics service."""

    event_name: str
    user_id: str
    metadata: dict[str, str] | None = None
