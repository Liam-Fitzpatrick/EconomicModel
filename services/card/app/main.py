from fastapi import FastAPI

from libs.schemas.v1 import Card, HealthStatus


app = FastAPI(title="Card Service")


@app.get("/health", response_model=HealthStatus)
def health() -> HealthStatus:
    return HealthStatus(service="card")


@app.get("/cards/{card_id}", response_model=Card)
def get_card(card_id: str) -> Card:
    return Card(id=card_id, board_id="board-1", title="Sample Card", description="Placeholder")
