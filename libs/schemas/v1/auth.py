from pydantic import BaseModel


class UserCredentials(BaseModel):
    """Credentials used when authenticating a user."""

    username: str
    password: str


class AuthToken(BaseModel):
    """Token returned after successful authentication."""

    access_token: str
    token_type: str = "bearer"
