import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Config
    APP_NAME: str = "Financial RAG Agent"
    
    # API Keys
    HUGGINGFACEHUB_API_TOKEN: str
    
    # LangSmith Observability
    LANGCHAIN_TRACING_V2: str = "true"
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str = "Financial_RAG_Production"

    class Config:
        env_file = ".ENV"

settings = Settings()# Environment variables & Settings