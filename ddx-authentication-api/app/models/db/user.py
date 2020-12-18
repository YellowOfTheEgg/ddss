import uuid

import sqlalchemy
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.email import EmailType
from sqlalchemy_utils.types.uuid import UUIDType

from app.db.base_class import Base

#definition of the user-table
class User(Base):
    id = Column(UUIDType, default=uuid.uuid4, primary_key=True, index=True)
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(EmailType, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
