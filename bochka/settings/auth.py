from pydantic.v1 import BaseSettings


class AuthSettings(BaseSettings):
    secret_key: str
    algorythm: str
    access_token_expire_minutes: int

    class Config:
        env_prefix = "AUTH_"
        env_file = ".env"


auth_settings = AuthSettings()
