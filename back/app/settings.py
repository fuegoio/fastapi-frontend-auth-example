from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    env: str = Field("prod", env="ENV")
    app_url: str = Field("http://localhost:8080", env="APP_URL")
    db_uri: str = Field(
        "postgresql://example:example@localhost:5432/postgres", env="DB_URI"
    )
    github_client_id: str = Field("", env="GITHUB_CLIENT_ID")
    github_client_secret: str = Field("", env="GITHUB_CLIENT_SECRET")
    jwt_secret_key: str = Field("example_key_super_secret", env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")

    class Config:
        env_file = '.env'


settings = Settings()

