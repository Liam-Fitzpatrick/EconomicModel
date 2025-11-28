from pydantic import BaseModel


class Card(BaseModel):
    """Card that belongs to a board."""

    id: str
    board_id: str
    title: str
    description: str | None = None
