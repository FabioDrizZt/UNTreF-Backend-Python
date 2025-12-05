from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Table

# Tabla intermedia para la relación muchos a muchos entre Film y Actor
film_actor = Table(
    "film_actor",
    db.Model.metadata,
    Column("actor_id", ForeignKey("actor.actor_id")),
    Column("film_id", ForeignKey("film.film_id")),
)

# Tabla para actores
class Actor(db.Model):
    __tablename__ = "actor"
    
    actor_id = db.Column(Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(String(45), nullable=False)
    last_name = db.Column(String(45), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relación muchos a muchos con películas
    
    def to_dict(self):
        return {
            "actor_id": self.actor_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "last_update": self.last_update.isoformat(),
        }
    
# Tabla para películas
class Film(db.Model):
    __tablename__ = "film"
    
    film_id = db.Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(128), nullable=False)
    description = db.Column(String(255))
    release_year = db.Column(Integer)
    language_id = db.Column(Integer)
    original_language_id = db.Column(Integer, nullable=True)
    rental_duration = db.Column(Integer)
    rental_rate = db.Column(db.Numeric(4, 2))
    length = db.Column(Integer, nullable=True)
    replacement_cost = db.Column(db.Numeric(5, 2))
    rating = db.Column(String(10), nullable=True)
    special_features = db.Column(String(255), nullable=True)
    last_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relación muchos a muchos con actores
    
    def to_dict(self):
        return {
            "film_id": self.film_id,
            "title": self.title,
            "description": self.description,
            "release_year": self.release_year,
            "language_id": self.language_id,
            "original_language_id": self.original_language_id,
            "rental_duration": self.rental_duration,
            "rental_rate": self.rental_rate,
            "length": self.length,
            "replacement_cost": self.replacement_cost,
            "rating": self.rating,
            "special_features": self.special_features,
            "last_update": self.last_update.isoformat(),
        }