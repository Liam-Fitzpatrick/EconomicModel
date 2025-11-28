from fastapi import FastAPI

from libs.schemas.v1 import Board, HealthStatus


app = FastAPI(title="Board Service")


@app.get("/health", response_model=HealthStatus)
def health() -> HealthStatus:
    return HealthStatus(service="board")


@app.get("/boards/{board_id}", response_model=Board)
def get_board(board_id: str) -> Board:
    return Board(id=board_id, name="Sample Board", owner_id="owner-1")
