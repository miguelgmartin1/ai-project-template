from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All configuration comes from env vars / .env. Never hardcode keys or model names."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    anthropic_api_key: str = ""
    openrouter_api_key: str = ""
    langfuse_public_key: str = ""
    langfuse_secret_key: str = ""
    langfuse_host: str = "https://cloud.langfuse.com"

    frontier_model: str = "anthropic/claude-sonnet-4.5"  # OpenRouter id
    open_model: str = "qwen/qwen-2.5-7b-instruct"  # OpenRouter id


settings = Settings()
