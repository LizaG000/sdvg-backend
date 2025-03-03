from database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Lst(Base):
    """ """
    __tablename__ = "lst"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())
    #del = Column(Boolean, nullable=False, default=False) # del - это вообще ключевое слово, так то
