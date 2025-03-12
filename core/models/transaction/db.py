from src.main.database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class TransactionModel(Base):
    """ """
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(NUMERIC, default=0, nullable=False)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())
