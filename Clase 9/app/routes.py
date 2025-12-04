from flask import jsonify, request
from app import app
import json
import os

movies_path = os.path.join(os.getcwd(), "app", "data", "movies.json")


### Leer datos de movies.json
def cargar_movies():
    try:
        with open(movies_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return jsonify({"message": "Movies data file not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"message": "Error decoding movies data"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500


### Guardar datos de movies.json
def guardar_movies(movies):
    try:
        with open(movies_path, "w", encoding="utf-8") as f:
            json.dump(movies, f, indent=2)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Movies application!"})


@app.route("/movies")
def movies():
    movies = cargar_movies()

    title = request.args.get("title")
    if title:
        title = title.lower()
        movies = [m for m in movies if title in m.get("title", "").lower()]

    year = request.args.get("year")
    if year:
        year = int(year)
        movies = [m for m in movies if m.get("year") == year]

    if not movies:
        return jsonify({"message": "No movies found"}), 404

    return jsonify(movies), 200


@app.route("/movies/<int:id>", methods=["GET"])
def get_movie(id):
    for movie in cargar_movies():
        if movie.get("id") == id:
            return jsonify(movie), 200
    return jsonify({"message": "Movie not found"}), 404
    """ movie = next((m for m in cargar_movies() if m.get('id') == id), None)
    if not movie:
        return jsonify({"message": "Movie not found"}), 404
    return jsonify(movie), 200 """


@app.route("/movies", methods=["POST"])
def add_movie():
    movies = cargar_movies()
    new_movie = {
        **request.get_json(),
        "id": max(m.get("id", 0) for m in movies) + 1,
    }
    if not new_movie:
        return jsonify({"message": "Invalid movie data"}), 400

    movies.append(new_movie)
    guardar_movies(movies)
    return jsonify(new_movie), 201


@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    movies = cargar_movies()
    for movie in movies:
        if movie.get("id") == id:
            deleted_movie = movie
            movies.remove(movie)
            guardar_movies(movies)
            return (
                jsonify({"message": "Movie deleted", "deleted_movie": deleted_movie}),
                200,
            )
    return jsonify({"message": "Movie not found"}), 404


@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    movies = cargar_movies()
    for movie in movies:
        if movie.get("id") == id:
            updated_movie = {
                **movie,
                **request.get_json(),
            }
            if not updated_movie:
                return jsonify({"message": "Invalid movie data"}), 400

            movies.remove(movie)
            movies.append(updated_movie)
            guardar_movies(movies)
            return jsonify(updated_movie), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Page not found"}), 404
