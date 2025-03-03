from database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Task(Base):
    """ """
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    title = Column(String)
    text = Column(TEXT, nullable=False)
    till_dt = Column(DATETIME, nullable=False)
    completed_dt = Column(DATETIME)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())

    profiles = relationship("Profile", back_populates="profile")
