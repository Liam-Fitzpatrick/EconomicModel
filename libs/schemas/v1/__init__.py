"""Version 1 data transfer objects shared across services."""

from .common import HealthStatus
from .auth import UserCredentials, AuthToken
from .board import Board
from .card import Card
from .gateway import GatewayRoute
from .notification import NotificationMessage
from .analytics import AnalyticsEvent

__all__ = [
    "HealthStatus",
    "UserCredentials",
    "AuthToken",
    "Board",
    "Card",
    "GatewayRoute",
    "NotificationMessage",
    "AnalyticsEvent",
]
