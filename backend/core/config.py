from pydantic_settings import BaseSettings
from pydantic import Field
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Nova Clinical Companion API"
    
    # AWS Credentials (Pulled automatically from Codespace Secrets or .env)
    AWS_ACCESS_KEY_ID: str = Field(default_factory=lambda: os.getenv("AWS_ACCESS_KEY_ID", ""))
    AWS_SECRET_ACCESS_KEY: str = Field(default_factory=lambda: os.getenv("AWS_SECRET_ACCESS_KEY", ""))
    AWS_REGION: str = Field(default_factory=lambda: os.getenv("AWS_REGION", "us-east-1"))

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

if not settings.AWS_ACCESS_KEY_ID:
    print("⚠️ WARNING: AWS credentials missing. Nova API calls will fail.")