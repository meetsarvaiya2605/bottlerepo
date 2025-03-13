from database import Base
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
    Boolean,
    Time,
    Float,
    ForeignKey,
    Table,
    DateTime,
)
from pydoc import text
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "userss"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # bottle_id =Column(Integer, ForeignKey("bottles.id"))
    username = Column(String)
    email_id = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    hashed_password = Column(String)
    notification_on = Column(Boolean)
    notification_off = Column(Boolean)
    last_drink_time = Column(DateTime, default=datetime.utcnow())
    reminder_count = Column(Integer)
     

    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    bottle = relationship("Bottle", back_populates="user", uselist=False)


class Bottle(Base):
    __tablename__ = "bottles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("userss.id"), unique=True)
    bottle_capacity = Column(Integer, default=1000)
    bottle_amount = Column(Integer, default=0)
    last_recorded_amount = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    user = relationship("User", back_populates="bottle")
    # fill_status = relationship("Fill_Bottle", back_populates="bottle", uselist=False)


# class Fill_Bottle(Base):
#     __tablename__ = "fillbottle"
#     id = Column(Integer,autoincrement=True,primary_key=True)
#     is_filled = Column(Boolean, default=False)
#     drank = Column(Boolean, default=False)
#     bottle_id = Column(Integer, ForeignKey('bottles.id'), unique=True)
#     bottle = relationship("Bottle", back_populates="fill_status")


class WaterGoal(Base):
    __tablename__ = "set_goal"
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    set_goal = Column(Integer)
    user_id = Column(Integer, ForeignKey("userss.id"), unique=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
