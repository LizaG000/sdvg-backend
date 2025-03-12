from src.main.database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class LstValueModel(Base):
    """ """
    __tablename__ = "lst_value"
    id = Column(Integer, primary_key=True, nullable=False)
    lst_id = Column(Integer, ForeignKey("lst.id"), nullable=False)
    name = Column(String, nullable=False)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())
    is_del = Column(Boolean, nullable=False, default=False)
