from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    subscriptions = relationship("Subscription", back_populates="user")

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)
    user = relationship("User", back_populates="subscriptions")

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    video_url = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    gif_url = Column(String)
