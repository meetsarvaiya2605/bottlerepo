from database import Base
from sqlalchemy import TIMESTAMP , Column, Integer, String,Boolean,Time,Float, ForeignKey, Table , DateTime
from pydoc import text
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "userss"
    id = Column(Integer,primary_key=True,autoincrement=True)
    # bottle_id =Column(Integer, ForeignKey("bottles.id"))
    username = Column(String,nullable=False)
    email_id = Column(String,unique=True,nullable=False)
    firstname = Column(String,nullable=False)
    lastname= Column(String,nullable=False)
    hashed_password =Column(String,nullable=False)
    set_goal = Column(Integer,nullable=False)
    current_status = Column(Integer,nullable=False)
    notification_on = Column(Boolean,nullable=False)
    notification_off = Column(Boolean,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
    updated_at  = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
    bottle = relationship("Bottle" , back_populates="user", uselist=False)

class Bottle(Base):
    __tablename__ = "bottles"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id  =Column(Integer, ForeignKey("userss.id"))
    bottle_capacity = Column(Integer,nullable=False, default=100)
    bottle_amount = Column(Integer,nullable=False,default=0)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default= text('now()'))
    user = relationship("User", back_populates="bottle")



