from src.main.database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from core.models.transaction.db import TransactionModel

class AchievementProfileModel(Base):
    """ """
    __tablename__ = "achievement_profile"
    profile_id = Column(Integer, primary_key=True, nullable=False)
    achievement_id = Column(Integer, ForeignKey("transaction.id"), nullable=False)
