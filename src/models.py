import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(25), nullable=False)
    email = Column(String(250), nullable=False)
    Sing_up_date = Column(DateTime, nullable=False)
    Fk_favourist_list = Column(Integer, ForeignKey ('favourite.id'))


class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    character_list = relationship("Character")
    planet_list = relationship("Planets")
    user_id = relationship("User")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Specie = Column(String(250))
    Birth = Column(String(250))
    favourite_id = Column(Integer,ForeignKey('favourite.id'))


class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Kind = Column(String(250))
    favourite_id = Column(Integer,ForeignKey('favourite.id'))

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e