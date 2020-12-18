import os
from pydantic import BaseSettings, HttpUrl, PostgresDsn, validator
from typing import Optional, Dict, Any
import pathlib

#loading of the postgress credentials from .env-file
class Settings(BaseSettings):    
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str 
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get('POSTGRES_PORT'),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )
    class Config:
        case_sensitive = True
        env_file='app/engine/models/wmc_v3/.env'


settings=Settings()