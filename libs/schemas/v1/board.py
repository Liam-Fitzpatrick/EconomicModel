from pydantic import BaseModel


class Board(BaseModel):
    """A simple board description."""

    id: str
    name: str
    owner_id: str
