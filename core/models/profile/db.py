from src.main.database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, Numeric, DateTime, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class ProfileModel(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(BigInteger, nullable=False)
    username = Column(String(64), nullable=False) 
    password = Column(String(72), nullable=False)
    email = Column(String(320), nullable=False) 
    date_created = Column(DateTime, nullable=True, default=datetime.now()) 
    date_modified = Column(DateTime, nullable=True, default=datetime.now())
    balance = Column(Numeric, nullable=False, default=0) 
    is_del = Column(Boolean, default=False)