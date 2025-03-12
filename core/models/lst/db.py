from src.main.database import Base

from sqlalchemy import Column, Integer, String, Boolean, DATETIME
from datetime import datetime

class LstModel(Base):
    """ """
    __tablename__ = "lst"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())
    is_del = Column(Boolean, nullable=False, default=False)
