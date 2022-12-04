#!usr/binpython3
"""
class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import sys

engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3], pre_pool_ping=True))
Base = declarative_base()


class State(Base):
    """
    State class:
    inherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, cant be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and cant be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
