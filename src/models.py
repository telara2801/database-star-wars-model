import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy import or_
from sqlalchemy import String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Session
from sqlalchemy.orm import with_polymorphic
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import ConcreteBase


Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    nick_name = Column(String(80), nullable=False)
    email = Column(String(150), nullable=False)
    favorites1 = relationship("Favorite", back_populates="user1")
    def add_favorite():
        pass
    def delete_favorite():
        pass
    def see_more():
        pass
    def login():
        pass
    def log_out():
        pass

class Favorite(Base):
    __tablename__ = 'fovorite'
    favorite_id=Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.user_id'))
    card_id = Column(Integer,ForeignKey('card.card_id'))
    user1= relationship("User", back_populates="favorites1")
    card2= relationship("Card", back_populates="favorites2")


class Card(Base):
    __tablename__ = 'card'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    car_id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    description = Column(String(250), nullable=False)
    img = Column(String(250), nullable=False)
    favorite2 = relationship("Favorite", back_populates="card2")
    discriminator = Column(String(150))

    __mapper_args__ = {
        'polymorphic_identity':'card',
        'polymorphic_on':discriminator
        }


class Planet(Card):
    __tablename__ = None
    population = Column(Integer, nullable=False)
    climate = Column(String(80), nullable=False)
    rotation_period = Column(String(100), nullable=False)
    orbital_period = Column(String(100), nullable=False)
    diameter = Column(String(80), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'planet'}

class Vehicles(Card):
    __tablename__ = None
    model = Column(String(80), nullable=False)
    passengers= Column(Integer(), nullable=False)
    cargo_capacity= Column(String(10), nullable=False)
    length= Column(String(10), nullable=False)
    consumables= Column(String(100), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'vehicle'}

class Character (Card):
    __tablename__ = None
    eye_color = Column(String(40), nullable=False)
    skin_color= Column(String(40), nullable=False)
    birth_year= Column(String(10), nullable=False)
    gender= Column(String(20), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'character',
    }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e