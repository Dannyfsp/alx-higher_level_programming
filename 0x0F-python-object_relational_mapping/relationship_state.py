#!/usr/bin/python3
"""
This script defines a State class that
inherits from Base class to work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    This class links to the 'states' table of our database
    Attributes:
        __tablename__(str): The table name of the class
        id(int): The State id of the class
        name(Str): The State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
