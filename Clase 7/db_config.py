from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

# Cargar variables de entorno desde archivo .env
load_dotenv()


def connect_to_db():
    # Buena practica: validar que las variables existan antes de usarlas
    required_vars = ["DB_HOST", "DB_USER", "DB_PASS", "DB_NAME"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"Faltan variables de entorno: {', '.join(missing_vars)}")
        return None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            charset="utf8mb4",  # Permite usar caracteres especiales en MySQL
            autocommit=False,  # No aplica automáticamente los cambios a la base de datos
            connect_timeout=10,  # Tiempo de espera máximo para la conexión (en segundos)
        )
        if connection.is_connected():
            print("Conexión a la base de datos establecida exitosamente.")
            return connection
        else:
            print("Error al conectar a la base de datos.")
            return None

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        print(f"Código de error: {e.errno}")
        print(f"Mensaje de error: {e.msg}")
        return None
    except Exception as e:
        print(f"Error inesperado al conectar a la base de datos: {e}")
        return None


if __name__ == "__main__":
    connect_to_db()
