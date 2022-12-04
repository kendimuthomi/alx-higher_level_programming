#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from model_city import City

if __name__ == "__main__":
    State.cities = relationship(
                "City", order_by=City.id, back_populates="state")
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).filter(
            City.state_id == State.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city[0].name, city[1].id, city[1].name))
