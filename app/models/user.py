
from sqlalchemy import Column, Integer, String, Boolean
from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_admin = Column(Boolean(), default=True)
    is_business = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)
