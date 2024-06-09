from pydantic.v1 import BaseSettings


class DatabaseSettings(BaseSettings):
    username: str
    password: str
    host: str
    port: int
    name: str

    class Config:
        env_prefix = "DB_"
        env_file = ".env"

    def get_db_url(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"


database_settings = DatabaseSettings()
