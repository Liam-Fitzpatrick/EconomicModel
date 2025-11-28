from fastapi import FastAPI

from libs.schemas.v1 import AuthToken, HealthStatus, UserCredentials


app = FastAPI(title="Auth Service")


@app.get("/health", response_model=HealthStatus)
def health() -> HealthStatus:
    return HealthStatus(service="auth")


@app.post("/login", response_model=AuthToken)
def login(credentials: UserCredentials) -> AuthToken:
    fake_token = f"token-for-{credentials.username}"
    return AuthToken(access_token=fake_token)
