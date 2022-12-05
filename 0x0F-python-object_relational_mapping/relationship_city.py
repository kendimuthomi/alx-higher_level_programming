#!/usr/bin/python3
"""
class definition of a City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from relationship_state import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(Base):
    """
    State class:
    inherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, cant be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and cant be null
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
