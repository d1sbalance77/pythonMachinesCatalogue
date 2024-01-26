from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer, unique=True)
    password = Column(String)

    reg_date = Column(DateTime)


class Machine(Base):
    __tablename__ = 'machines'

    machine_id = Column(Integer, primary_key=True,)
    machine_name = Column(String)
    machine_color = Column(String)
    machine_year = Column(Integer)
    machine_cost = Column(Integer)
    base_price = Column(String, default=0)
    machine_photo = Column(String, primary_key=True)
    machine_engine = Column(String)
    changed_machine = Column(String)
    machine_engine_id = Column(String, primary_key=True)


