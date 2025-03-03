from database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, Numeric, DateTime, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Profile(Base):
    __tablename__ = "profile"  # Убедитесь, что название совпадает с именем таблицы в БД

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key с автоинкрементом
    phone = Column(BigInteger, nullable=False)  # Поле phone как bigint
    username = Column(String(64), nullable=False)  # username с ограничением длины 64
    password = Column(String(72), nullable=False)  # password с ограничением длины 72
    email = Column(String(320), nullable=False)  # email с ограничением длины 320
    date_created = Column(DateTime, nullable=True, default=datetime.utcnow)  # Время создания с автозаполнением
    date_modified = Column(DateTime, nullable=True, default=datetime.utcnow)  # Время изменения
    balance = Column(Numeric, nullable=False, default=0)  # Числовое поле с начальным значением 0
    del_ = Column('del', Boolean, default=False)
    # отношения между таблицами??
    #achievements_profiles = relationship("AchievementProfile", back_populates="achievement_profile")
