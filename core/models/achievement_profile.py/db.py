from database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class AchievementProfile(Base):
    """ """
    __tablename__ = "achievement_profile"
    profile_id = Column(Integer, primary_key=True, nullable=False)
    achievement_id = Column(Integer, primary_key=True, nullable=False)

    #profile_id = Column(Integer, ForeignKey("profile.id"), nullable=False)
    #transaction_id = Column(Integer, ForeignKey("transaction.id"), nullable=False)
    
    # отношения между таблицами??
    #profiles = relationship("Profile", back_populates="profile")
    #achievements = relationship("Transaction", back_populates="transaction")
