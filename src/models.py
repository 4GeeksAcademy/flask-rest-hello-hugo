from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites:Mapped[List['Favorite']] = relationship(
        back_populates="user"
)


    
class Planet(db.Model):
    __tablename__="planets"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(120), nullable=False)
    film:Mapped[str] = mapped_column(String(120),  nullable=False)
    diameter:Mapped[str] = mapped_column(String(120), nullable=False)
    population:Mapped[int] = mapped_column( nullable=False)
    favorites:Mapped[List['Favorite']]= relationship(
    back_populates="planet"
)
    character:Mapped[List['Character']]= relationship(
    back_populates="planet"
)  


class Character(db.Model):
    __tablename__="characters"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(120),  nullable=False)
    age:Mapped[int] = mapped_column( nullable=False)
    eyes_color:Mapped[str] = mapped_column(String(120),  nullable=False)
    planet_id:Mapped[int]=mapped_column(ForeignKey("planets.id"),nullable=True)
    favorites:Mapped[List['Favorite']]= relationship(
    back_populates="character"
)  
    planets:Mapped['Planet']=relationship(
        back_populates="characters"
    )
   

class Favorite(db.Model):
    __tablename__="favorites"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    planet_id:Mapped[int]=mapped_column(ForeignKey("planets.id"),nullable=True)
    character_id:Mapped[int]=mapped_column(ForeignKey("characters.id"),nullable=True)
    user:Mapped['User']=relationship(
        back_populates="favorites"
    )
    planets:Mapped['Planet']=relationship(
        back_populates="favorites"
    )
    character:Mapped['Character']=relationship(
        back_populates="favorites"
    )