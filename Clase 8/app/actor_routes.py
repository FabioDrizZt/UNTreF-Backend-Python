from flask import Blueprint, jsonify
from app.actor_queries import get_actors, get_actors_dict, get_actor_films

actor_bp = Blueprint("actor", __name__)


@actor_bp.route("/actores")
def actores():
    actores = get_actors(limit=25)
    return jsonify(actores), 200


@actor_bp.route("/api/lista_actores")
def lista_actores():
    """Endpoint de listado de actores"""
    return "Listado de actores"


@actor_bp.route("/api/lista_dict_actores")
def lista_dict_actores():
    """Endpoint de listado de actores"""
    return "Listado de actores"


@actor_bp.route("/api/lista_films_actor/<actor_id>")
def lista_films_actor(actor_id):
    """Endpoint de listado de actores"""
    return f"Listado de películas del actor {actor_id}"
