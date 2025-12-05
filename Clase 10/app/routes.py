from flask import jsonify, request
from app.models import Actor, Film
from app import db


def register_routes(app):

    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the sakila API"})

    @app.route("/actors", methods=["GET"])
    def get_actors():
        try:
            actors = Actor.query.all()
            return jsonify([actor.to_dict() for actor in actors]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/actors/<int:actor_id>", methods=["GET"])
    def get_actor(actor_id):
        try:
            actor = Actor.query.get(actor_id)
            if not actor:
                return jsonify({"error": "Actor not found"}), 404
            return jsonify(actor.to_dict()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/actors", methods=["POST"])
    def create_actor():
        try:
            data = request.get_json()
            # validamos que los campos sean correctos
            if not data or "first_name" not in data or "last_name" not in data:
                return jsonify({"error": "Missing required fields"}), 400

            actor = Actor(
                first_name=data["first_name"].upper(),
                last_name=data["last_name"].upper(),
            )

            db.session.add(actor)
            db.session.commit()
            return jsonify(actor.to_dict()), 201
        except Exception as e:
            db.session.rollback()  # si falla, revertir la transacción
            return jsonify({"error": str(e)}), 500

    @app.route("/actors/bulk", methods=["POST"])
    def create_actors_bulk():
        try:
            data = request.get_json()
            # validamos que los campos sean correctos
            if not isinstance(data, list):
                return jsonify({"error": "Invalid data format"}), 400

            actors = []
            # validamos que los campos sean correctos
            for actor_data in data:
                if (
                    not actor_data
                    or "first_name" not in actor_data
                    or "last_name" not in actor_data
                ):
                    return jsonify({"error": "Missing required fields"}), 400

                actor = Actor(
                    first_name=actor_data["first_name"].upper(),
                    last_name=actor_data["last_name"].upper(),
                )
                actors.append(actor)
                db.session.add(actor)

            db.session.commit()
            return jsonify([actor.to_dict() for actor in actors]), 201

        except Exception as e:
            db.session.rollback()  # si falla, revertir la transacción
            return jsonify({"error": str(e)}), 500

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        try:
            actor = Actor.query.get(actor_id)
            if not actor:
                return jsonify({"error": "Actor not found"}), 404

            db.session.delete(actor)
            db.session.commit()
            return jsonify({"message": "Actor deleted"}), 200
        except Exception as e:
            db.session.rollback()  # si falla, revertir la transacción
            return jsonify({"error": str(e)}), 500

    """ 
    ---------------------------------------------------------------------------
                            Rutas para films
    ---------------------------------------------------------------------------
    """

    @app.route("/films", methods=["GET"])
    def get_films():
        try:
            limit = request.args.get("limit", 10, type=int)
            offset = request.args.get("offset", 0, type=int)

            if limit > 100:
                limit = 100

            films = Film.query.offset(offset).limit(limit).all()
            return jsonify([film.to_dict() for film in films]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/films/<int:film_id>", methods=["GET"])
    def get_film(film_id):
        try:
            film = Film.query.get(film_id)
            if not film:
                return jsonify({"error": "Film not found"}), 404
            return jsonify(film.to_dict()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/films", methods=["POST"])
    def create_film():
        try:
            data = request.get_json()
            # validamos que los campos sean correctos
            if not data or "title" not in data:
                return jsonify({"error": "Missing required fields"}), 400

            film = Film(
                title=data["title"],
                description=data.get("description", ""),
                release_year=data.get("release_year", 0),
                language_id=data.get("language_id", 1),
                original_language_id=data.get("original_language_id", 1),
                rental_duration=data.get("rental_duration", 0),
                rental_rate=data.get("rental_rate", 0),
                length=data.get("length", 0),
                replacement_cost=data.get("replacement_cost", 0),
                rating=data.get("rating", "G"),
                special_features=data.get("special_features", ""),
            )

            db.session.add(film)
            db.session.commit()
            return jsonify(film.to_dict()), 201
        except Exception as e:
            db.session.rollback()  # si falla, revertir la transacción
            return jsonify({"error": str(e)}), 500

    @app.route("/films/<int:film_id>", methods=["PUT"])
    def update_film(film_id):
        try:
            data = request.get_json()
            # validamos que los campos sean correctos
            if not data or "title" not in data:
                return jsonify({"error": "Missing required fields"}), 400

            # Validamos que la pelicula a modificar exista
            film = Film.query.get(film_id)
            if not film:
                return jsonify({"error": "Film not found"}), 404

            # actualizamos los campos
            if "title" in data:
                film.title = data["title"]
            if "description" in data:
                film.description = data["description"]
            if "release_year" in data:
                film.release_year = data["release_year"]
            if "language_id" in data:
                film.language_id = data["language_id"]
            if "original_language_id" in data:
                film.original_language_id = data["original_language_id"]
            if "rental_duration" in data:
                film.rental_duration = data["rental_duration"]
            if "rental_rate" in data:
                film.rental_rate = data["rental_rate"]
            if "length" in data:
                film.length = data["length"]
            if "replacement_cost" in data:
                film.replacement_cost = data["replacement_cost"]
            if "rating" in data:
                film.rating = data["rating"]
            if "special_features" in data:
                film.special_features = data["special_features"]

            db.session.commit()
            return jsonify(film.to_dict()), 200
        except Exception as e:
            db.session.rollback()  # si falla, revertir la transacción
            return jsonify({"error": str(e)}), 500

    @app.route("/films/<int:film_id>", methods=["DELETE"])
    def delete_film(film_id):
        try:
            film = Film.query.get(film_id)
            if not film:
                return jsonify({"error": "Film not found"}), 404

            db.session.delete(film)
            db.session.commit()
            return jsonify({"message": "Film deleted"}), 200
        except Exception as e:
            db.session.rollback()  # si falla, revertir la transacción
            return jsonify({"error": str(e)}), 500
