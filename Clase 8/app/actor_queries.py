from app.config.db_config import connect_to_db
from mysql.connector import Error


def get_actors(limit=25):
    cursor = None
    db = None
    try:
        db = connect_to_db()
        if db is None:
            print("Error al conectar a la base de datos.")
            return None

        cursor = db.cursor()

        query = "SELECT * FROM actor LIMIT %s"
        cursor.execute(query, (limit,))

        actors = cursor.fetchall()

        return actors

    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


def get_actors_dict(limit=25):
    cursor = None
    db = None
    try:
        db = connect_to_db()
        if db is None:
            print("Error al conectar a la base de datos.")
            return None

        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM actor LIMIT %s"
        cursor.execute(query, (limit,))

        actors = cursor.fetchall()

        return actors

    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


def get_actor_films(actor_id):
    cursor = None
    db = None
    try:
        db = connect_to_db()
        if db is None:
            print("Error al conectar a la base de datos.")
            return None

        cursor = db.cursor(dictionary=True)

        query = """ 
            SELECT f.title 
            FROM film f
            INNER JOIN film_actor fa ON f.film_id = fa.film_id
            WHERE fa.actor_id = %s
            ORDER BY f.title 
            """
        cursor.execute(query, (actor_id,))

        films = cursor.fetchall()

        return films

    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()



if __name__ == "__main__":
    actors = get_actors(limit=10)
    for actor in actors:
        print(actor)
