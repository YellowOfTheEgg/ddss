import distutils.util
import os
import secrets
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator

#this class contains settings definition for the backend services
class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    AUTHENTICATION_API_SECRET_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    @classmethod
    def assemble_cors_origins(
        cls, value: Union[str, List[str]]
    ) -> Union[List[str], str]:
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]
        elif isinstance(value, (list, str)):
            return value
        raise ValueError(value)

    PROJECT_NAME: str

    # Testing
    INTEGRATION_TESTS: bool = distutils.util.strtobool(
        os.getenv("INTEGRATION_TESTS", "False")
    )

    # Services
    DDX_AUTHENTICATION_API_HOST: str
    DDX_AUTHENTICATION_API_PORT: int
    DDX_AUTHENTICATION_API: str

    DDX_BACKEND_API_HOST: str
    DDX_BACKEND_API_PORT: int
    DDX_BACKEND_API: str

    DDX_WEBSITE_API_HOST: str
    DDX_WEBSITE_API_PORT: int
    DDX_WEBSITE_API: str


    class Config:
        case_sensitive = True


settings = Settings()
