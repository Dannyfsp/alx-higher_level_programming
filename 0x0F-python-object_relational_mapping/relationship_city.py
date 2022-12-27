#!/usr/bin/python3
"""
This script defines a city class that
inherits from Base class to work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    This class links to the 'cities' table of our database
    Attributes:
        __tablename__(str): The table name of the class
        id(int): The City id of the class
        name(Str): The name of the city
        state_id(int): The State id of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
