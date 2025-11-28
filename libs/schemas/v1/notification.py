from pydantic import BaseModel


class NotificationMessage(BaseModel):
    """Notification payload."""

    id: str
    recipient_id: str
    message: str
