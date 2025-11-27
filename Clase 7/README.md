# 📚 Clase 7: Bases de Datos MySQL y Variables de Entorno

Bienvenido a la Clase 7 del curso de Python. En esta clase aprenderás a trabajar con bases de datos MySQL, gestionar variables de entorno de forma segura y ejecutar consultas SQL desde Python.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Conectar Python con bases de datos MySQL
- ✅ Ejecutar consultas SQL desde Python
- ✅ Manejar resultados de consultas como tuplas y diccionarios
- ✅ Gestionar variables de entorno con archivos `.env`
- ✅ Acceder a variables de entorno del sistema operativo
- ✅ Manejar errores y conexiones de bases de datos de forma segura
- ✅ Usar parámetros en consultas SQL para prevenir inyección SQL

## 📋 Temas Cubiertos

### 1. Variables de Entorno del Sistema Operativo

Las variables de entorno son valores que el sistema operativo proporciona a las aplicaciones. Python puede acceder a ellas mediante el módulo `os`.

**Conceptos clave:**
- Acceso a variables con `os.environ.get()`
- Información del sistema con `platform`
- Variables comunes: `USERNAME`, `PATH`, `TEMP`, etc.
- Diferencias entre Windows y Linux/Mac

**Ejemplo básico:**
```python
import os
import platform

# Obtener información del sistema
print(f"Usuario: {os.environ.get('USERNAME')}")
print(f"Sistema: {platform.system()}")
print(f"Versión: {platform.version()}")

# Acceder a variables específicas
path = os.environ.get('PATH')
print(f"Rutas en PATH: {len(path.split(os.pathsep))}")
```

### 2. Variables de Entorno con Archivo .env

Los archivos `.env` permiten almacenar configuración sensible (como credenciales) de forma segura sin hardcodearlas en el código.

**Ventajas:**
- Separación de configuración y código
- Seguridad: no se suben al repositorio (deben estar en `.gitignore`)
- Facilidad para diferentes entornos (desarrollo, producción)

**Uso con python-dotenv:**

```python
from dotenv import load_dotenv
import os

# Cargar variables desde archivo .env
load_dotenv()

# Acceder a las variables
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
```

**Estructura del archivo `.env`:**
```env
DB_HOST=localhost
DB_USER=usuario
DB_PASS=contraseña_segura
DB_NAME=nombre_base_datos
```

**⚠️ Importante:** 
- Nunca subas el archivo `.env` al repositorio
- Agrega `.env` a tu `.gitignore`
- Usa un archivo `.env.example` como plantilla

### 3. Conexión a Bases de Datos MySQL

Python se conecta a MySQL usando el conector oficial `mysql-connector-python`.

**Instalación:**
```bash
pip install mysql-connector-python
```

**Conexión básica:**
```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="contraseña",
        database="nombre_bd",
        charset="utf8mb4",
        autocommit=False,
        connect_timeout=10
    )
    
    if connection.is_connected():
        print("Conexión exitosa")
        
except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        connection.close()
```

**Parámetros importantes:**
- `host`: Dirección del servidor MySQL
- `user`: Usuario de la base de datos
- `password`: Contraseña del usuario
- `database`: Nombre de la base de datos
- `charset`: Codificación de caracteres (utf8mb4 para caracteres especiales)
- `autocommit`: Si es `False`, necesitas hacer commit manual
- `connect_timeout`: Tiempo máximo de espera para conectar

### 4. Ejecución de Consultas SQL

Una vez conectado, puedes ejecutar consultas SQL usando un cursor.

**Consulta básica:**
```python
cursor = connection.cursor()
query = "SELECT * FROM tabla LIMIT %s"
cursor.execute(query, (10,))  # El segundo parámetro son los valores
resultados = cursor.fetchall()
cursor.close()
```

**Tipos de cursor:**
- **Cursor estándar**: Retorna tuplas `(valor1, valor2, ...)`
- **Cursor con dictionary=True**: Retorna diccionarios `{"columna": valor}`

**Ejemplo con tuplas:**
```python
cursor = connection.cursor()
cursor.execute("SELECT actor_id, first_name, last_name FROM actor LIMIT 5")
actores = cursor.fetchall()  # [(1, 'PENELOPE', 'GUINESS'), ...]

for actor in actores:
    actor_id, nombre, apellido = actor
    print(f"{actor_id}: {nombre} {apellido}")
```

**Ejemplo con diccionarios:**
```python
cursor = connection.cursor(dictionary=True)
cursor.execute("SELECT * FROM actor LIMIT 5")
actores = cursor.fetchall()  # [{'actor_id': 1, 'first_name': 'PENELOPE', ...}, ...]

for actor in actores:
    print(f"{actor['actor_id']}: {actor['first_name']} {actor['last_name']}")
```

### 5. Consultas con Parámetros (Prevención de SQL Injection)

**⚠️ NUNCA concatenes valores directamente en consultas SQL**

**❌ Incorrecto (vulnerable a SQL Injection):**
```python
query = f"SELECT * FROM actor WHERE actor_id = {actor_id}"
cursor.execute(query)
```

**✅ Correcto (usando parámetros):**
```python
query = "SELECT * FROM actor WHERE actor_id = %s"
cursor.execute(query, (actor_id,))
```

**Ventajas:**
- Previene inyección SQL
- Mejor rendimiento (el servidor puede cachear el plan de ejecución)
- Manejo automático de tipos y caracteres especiales

### 6. Consultas JOIN

Las consultas JOIN permiten combinar datos de múltiples tablas.

**Ejemplo:**
```python
query = """
    SELECT f.title 
    FROM film f
    INNER JOIN film_actor fa ON f.film_id = fa.film_id
    WHERE fa.actor_id = %s
    ORDER BY f.title
"""
cursor.execute(query, (actor_id,))
peliculas = cursor.fetchall()
```

### 7. Manejo de Errores

Es crucial manejar errores adecuadamente al trabajar con bases de datos.

**Buenas prácticas:**
- Usar `try-except` específicos para `Error` de MySQL
- Cerrar cursor y conexión en bloque `finally`
- Validar que las variables de entorno existan antes de usarlas

**Ejemplo completo:**
```python
def get_actors(limit=25):
    cursor = None
    db = None
    try:
        db = connect_to_db()
        if db is None:
            return None
        
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM actor LIMIT %s"
        cursor.execute(query, (limit,))
        actors = cursor.fetchall()
        return actors
        
    except Error as e:
        print(f"Error SQL: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()
```

## 📁 Archivos de la Clase

Esta clase contiene los siguientes archivos:

- **`variables_de_entorno_del_SO.py`**: Ejemplos de acceso a variables de entorno del sistema operativo
- **`db_config.py`**: Configuración de conexión a MySQL usando variables de entorno desde `.env`
- **`actor_queries.py`**: Funciones para consultar actores y películas de la base de datos
- **`index.py`**: Archivo principal que integra todos los conceptos
- **`requirements.txt`**: Dependencias necesarias para la clase

## 🚀 Configuración Inicial

### Paso 1: Crear Entorno Virtual

```bash
# Navegar a la carpeta de la clase
cd "Clase 7"

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual (Windows)
.venv\Scripts\activate

# Activar entorno virtual (Linux/Mac)
source .venv/bin/activate
```

### Paso 2: Instalar Dependencias

```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# O instalar manualmente:
pip install mysql-connector-python python-dotenv tabulate
```

### Paso 3: Configurar Base de Datos

1. **Instalar MySQL** (si no lo tienes):
   - [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
   - O usar [XAMPP](https://www.apachefriends.org/) que incluye MySQL

2. **Crear base de datos de ejemplo:**
   - Descargar [Sakila Sample Database](https://dev.mysql.com/doc/index-other.html)
   - Importar el esquema y datos

3. **Crear archivo `.env`:**
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASS=tu_contraseña
   DB_NAME=sakila
   ```

### Paso 4: Ejecutar los Ejemplos

```bash
# Ver variables de entorno del sistema
python variables_de_entorno_del_SO.py

# Probar conexión a la base de datos
python db_config.py

# Ejecutar consultas de actores
python actor_queries.py

# Ejecutar ejemplo completo
python index.py
```

## 🔒 Seguridad y Buenas Prácticas

### 1. Variables de Entorno

- ✅ **Usa archivos `.env`** para configuración sensible
- ✅ **Agrega `.env` a `.gitignore`**
- ✅ **Valida que las variables existan** antes de usarlas
- ❌ **Nunca hardcodees credenciales** en el código

### 2. Consultas SQL

- ✅ **Usa parámetros** en todas las consultas
- ✅ **Valida datos de entrada** antes de ejecutar consultas
- ❌ **Nunca concatenes valores** directamente en SQL

### 3. Gestión de Conexiones

- ✅ **Cierra cursor y conexión** en bloque `finally`
- ✅ **Verifica que la conexión esté activa** antes de usar
- ✅ **Maneja errores** específicos de MySQL
- ❌ **No dejes conexiones abiertas** innecesariamente

### 4. Manejo de Errores

- ✅ **Usa try-except específicos** para diferentes tipos de errores
- ✅ **Proporciona mensajes de error claros**
- ✅ **Registra errores** para debugging (en producción)

## 💡 Ejercicios Prácticos Sugeridos

1. **Crear función para obtener películas por categoría**
   - Usar JOIN entre `film`, `film_category` y `category`
   - Retornar resultados como diccionarios

2. **Implementar búsqueda de actores por nombre**
   - Usar `LIKE` con parámetros
   - Manejar búsquedas parciales

3. **Crear función para obtener estadísticas**
   - Contar películas por categoría
   - Mostrar resultados con `tabulate`

4. **Mejorar manejo de errores**
   - Crear función que valide conexión antes de consultar
   - Implementar reintentos en caso de fallo de conexión

5. **Crear módulo de configuración**
   - Centralizar validación de variables de entorno
   - Proporcionar valores por defecto

## 🔍 Conceptos Clave a Recordar

- **Variables de entorno**: Configuración externa al código
- **Archivo .env**: Almacena configuración sensible de forma segura
- **Cursor**: Objeto para ejecutar consultas SQL
- **Parámetros en SQL**: Previenen inyección SQL y mejoran rendimiento
- **Manejo de conexiones**: Siempre cerrar en `finally`
- **Resultados como diccionarios**: Más legibles que tuplas

## 📚 Recursos Adicionales

- [Documentación de mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)
- [Documentación de python-dotenv](https://pypi.org/project/python-dotenv/)
- [Documentación de os.environ](https://docs.python.org/es/3/library/os.html#os.environ)
- [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)
- [SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)

## ⚠️ Errores Comunes

1. **No cerrar conexiones**: Siempre usa `finally` para cerrar
2. **Hardcodear credenciales**: Usa variables de entorno siempre
3. **SQL Injection**: Nunca concatenes valores en consultas
4. **Olvidar activar venv**: Activa el entorno antes de instalar paquetes
5. **No validar variables**: Verifica que las variables de entorno existan
6. **Cursor sin dictionary=True**: Si necesitas diccionarios, especifícalo

## 🎓 Siguiente Paso

Una vez que domines estos conceptos, estarás listo para:
- Construir APIs REST que interactúen con bases de datos
- Implementar operaciones CRUD completas
- Trabajar con ORMs como SQLAlchemy
- Gestionar transacciones y operaciones complejas
- Optimizar consultas y mejorar rendimiento

---

**¡Sigue practicando y experimentando con las bases de datos!** 🚀

*Recuerda: La seguridad es fundamental. Siempre usa parámetros en tus consultas SQL y nunca expongas credenciales en el código.*

