# 📚 Clase 10: Flask + SQLAlchemy - ORMs y Relaciones

Bienvenido a la Clase 10 del curso de Python. En esta clase aprenderás a usar SQLAlchemy, un ORM (Object-Relational Mapping) poderoso que te permite trabajar con bases de datos usando objetos Python en lugar de escribir SQL directamente. También implementarás relaciones many-to-many entre entidades.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Entender qué es un ORM y sus ventajas
- ✅ Configurar SQLAlchemy con Flask
- ✅ Crear modelos de datos con SQLAlchemy
- ✅ Implementar relaciones many-to-many entre entidades
- ✅ Realizar operaciones CRUD usando el ORM
- ✅ Crear APIs REST complejas conectadas a bases de datos reales
- ✅ Manejar operaciones en bloque (bulk operations)
- ✅ Trabajar con relaciones entre tablas de forma eficiente

## 📋 Temas Cubiertos

### 1. ¿Qué es un ORM?

**ORM (Object-Relational Mapping)** es una técnica que permite mapear objetos de programación orientada a objetos a tablas de bases de datos relacionales.

**Ventajas de usar un ORM:**
- ✅ **Código más limpio**: No necesitas escribir SQL manualmente
- ✅ **Portabilidad**: Cambiar de base de datos es más fácil
- ✅ **Seguridad**: Previene SQL injection automáticamente
- ✅ **Productividad**: Menos código, más funcionalidad
- ✅ **Mantenibilidad**: Código más fácil de entender y mantener

**Desventajas:**
- ⚠️ Puede ser más lento que SQL puro en consultas complejas
- ⚠️ Curva de aprendizaje inicial

### 2. SQLAlchemy

SQLAlchemy es el ORM más popular para Python. Proporciona:
- Mapeo de clases Python a tablas de base de datos
- Sistema de consultas potente y expresivo
- Soporte para relaciones entre tablas
- Migraciones de esquema

**Instalación:**
```bash
pip install Flask-SQLAlchemy
```

### 3. Configuración de SQLAlchemy con Flask

**Configuración básica (Factory Pattern):**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )

    db.init_app(app)

    from app.routes import register_routes
    register_routes(app)

    return app
```

**Componentes importantes:**
- `SQLALCHEMY_DATABASE_URI`: String de conexión a la base de datos
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Desactivado para mejor rendimiento
- `db`: Instancia de SQLAlchemy que maneja todas las operaciones

### 4. Creación de Modelos

Los modelos son clases Python que representan tablas en la base de datos.

**Modelo Actor:**

```python
from app import db
from datetime import datetime

class Actor(db.Model):
    """Modelo para la tabla actor de la base de datos Sakila"""
    __tablename__ = 'actor'
    
    actor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relación many-to-many con Film a través de film_actor
    films = db.relationship(
        'Film', # 1. Modelo relacionado
        secondary='film_actor', # 2. Tabla intermedia
        back_populates='actors', # 3. Atributo de relación en el modelo relacionado
        lazy='dynamic' # 4. Lazy loading
    )
    
    def to_dict(self):
        """Convierte el objeto Actor a diccionario"""
        return {
            'actor_id': self.actor_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'last_update': self.last_update.isoformat() if self.last_update else None
        }
    
    def __repr__(self):
        return f'<Actor {self.first_name} {self.last_name}>'
```

**Modelo Film:**

```python
class Film(db.Model):
    """Modelo para la tabla film de la base de datos Sakila"""
    __tablename__ = 'film'
    
    film_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    release_year = db.Column(db.Integer)
    language_id = db.Column(db.SmallInteger, nullable=False)
    original_language_id = db.Column(db.SmallInteger)
    rental_duration = db.Column(db.SmallInteger, nullable=False, default=3)
    rental_rate = db.Column(db.Numeric(4, 2), nullable=False, default=4.99)
    length = db.Column(db.SmallInteger)
    replacement_cost = db.Column(db.Numeric(5, 2), nullable=False, default=19.99)
    rating = db.Column(db.String(5), default='G')
    special_features = db.Column(db.String(54))
    last_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relación many-to-many con Actor a través de film_actor
    actors = db.relationship(
        'Actor',
        secondary='film_actor',
        back_populates='films',
        lazy='dynamic'
    )
    
    def to_dict(self):
        """Convierte el objeto Film a diccionario"""
        return {
            'film_id': self.film_id,
            'title': self.title,
            'description': self.description,
            'release_year': self.release_year,
            'language_id': self.language_id,
            'rental_duration': self.rental_duration,
            'rental_rate': float(self.rental_rate) if self.rental_rate else None,
            'length': self.length,
            'replacement_cost': float(self.replacement_cost) if self.replacement_cost else None,
            'rating': self.rating,
            'last_update': self.last_update.isoformat() if self.last_update else None
        }
    
    def __repr__(self):
        return f'<Film {self.title}>'
```

**Tipos de columnas comunes:**
- `db.Integer`: Números enteros
- `db.SmallInteger`: Números enteros pequeños
- `db.String(length)`: Cadenas de texto con longitud máxima
- `db.Text`: Texto largo sin límite
- `db.DateTime`: Fechas y horas
- `db.Boolean`: Valores booleanos
- `db.Numeric(precision, scale)`: Números decimales con precisión (ej: `db.Numeric(4, 2)` para 99.99)

**Métodos importantes en los modelos:**
- `to_dict()`: Convierte el objeto a diccionario para serialización JSON
- `__repr__()`: Representación legible del objeto para debugging (ej: `<Actor John Doe>`)

### 5. Relaciones Many-to-Many

Una relación many-to-many ocurre cuando múltiples registros de una tabla pueden relacionarse con múltiples registros de otra tabla.

**Ejemplo:** Un actor puede estar en muchas películas, y una película puede tener muchos actores.

**Tabla intermedia `film_actor`:**

```python
# SQLAlchemy crea automáticamente la relación usando la tabla intermedia
# La tabla film_actor ya existe en la base de datos Sakila
```

**Definir la relación:**

```python
# En el modelo Actor
films = db.relationship(
    'Film',
    secondary='film_actor',  # Nombre de la tabla intermedia
    back_populates='actors',  # Nombre de la relación en Film
    lazy='dynamic'           # Carga diferida (más eficiente)
)

# En el modelo Film
actors = db.relationship(
    'Actor',
    secondary='film_actor',
    back_populates='films',
    lazy='dynamic'
)
```

**Parámetros importantes:**
- `secondary`: Nombre de la tabla intermedia
- `back_populates`: Nombre de la relación inversa
- `lazy`: Estrategia de carga ('dynamic', 'select', 'joined', etc.)

### 6. Operaciones CRUD con SQLAlchemy

#### CREATE - Crear Registros

**Crear un actor:**

```python
@app.route('/actors', methods=['POST'])
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
```

**Crear varios actores en bloque:**

```python
@app.route('/actors/bulk', methods=['POST'])
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
```

#### READ - Leer Registros

**Obtener todos los actores:**

```python
@app.route('/actors', methods=['GET'])
def get_actors():
    try:
        actors = Actor.query.all()
        return jsonify([actor.to_dict() for actor in actors]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

**Obtener un actor específico:**

```python
@app.route('/actors/<int:actor_id>', methods=['GET'])
def get_actor(actor_id):
    try:
        actor = Actor.query.get(actor_id)
        if not actor:
            return jsonify({"error": "Actor not found"}), 404
        return jsonify(actor.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

**Filtros comunes:**

```python
# Filtrar por nombre
actors = Actor.query.filter_by(first_name='Tom').all()

# Filtrar con condiciones
actors = Actor.query.filter(Actor.first_name.like('%Tom%')).all()

# Ordenar
actors = Actor.query.order_by(Actor.last_name).all()

# Limitar resultados
actors = Actor.query.limit(10).all()
```

**Obtener películas con paginación:**

```python
@app.route('/films', methods=['GET'])
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
```

**Obtener una película específica:**

```python
@app.route('/films/<int:film_id>', methods=['GET'])
def get_film(film_id):
    try:
        film = Film.query.get(film_id)
        if not film:
            return jsonify({"error": "Film not found"}), 404
        return jsonify(film.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

**Crear una película:**

```python
@app.route('/films', methods=['POST'])
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
```

#### UPDATE - Actualizar Registros

```python
@app.route('/films/<int:film_id>', methods=['PUT'])
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
```

#### DELETE - Eliminar Registros

**Eliminar un actor:**

```python
@app.route('/actors/<int:actor_id>', methods=['DELETE'])
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
```

**Eliminar una película:**

```python
@app.route('/films/<int:film_id>', methods=['DELETE'])
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
```

### 7. Trabajar con Relaciones

Las relaciones many-to-many están definidas en los modelos usando `db.relationship()` con `lazy='dynamic'`. Esto permite acceder a las relaciones de forma eficiente:

**Acceder a películas de un actor:**

```python
actor = Actor.query.get(actor_id)
films = actor.films.all()  # Obtiene todas las películas del actor
```

**Acceder a actores de una película:**

```python
film = Film.query.get(film_id)
actors = film.actors.all()  # Obtiene todos los actores de la película
```

**Nota:** Las rutas para asociar/desasociar actores y películas no están implementadas en la versión actual, pero pueden agregarse fácilmente usando los métodos `.append()` y `.remove()` en las relaciones.

### 8. Sesiones y Transacciones

SQLAlchemy usa sesiones para gestionar transacciones:

```python
# Agregar objetos a la sesión
db.session.add(objeto)

# Confirmar cambios (commit)
db.session.commit()

# Deshacer cambios (rollback)
db.session.rollback()

# Cerrar sesión
db.session.close()
```

**Buenas prácticas:**
- Siempre haz `commit()` después de cambios
- Usa `rollback()` en bloques `try-except` para revertir transacciones fallidas
- Maneja excepciones apropiadamente
- Valida datos antes de crear/actualizar registros
- Retorna códigos de estado HTTP apropiados (200, 201, 400, 404, 500)

### 9. Consultas Avanzadas

**Joins implícitos (usando relaciones):**

```python
# Obtener actores de una película
film = Film.query.get(film_id)
actors = film.actors.all()
```

**Joins explícitos:**

```python
from sqlalchemy import join

result = db.session.query(Actor, Film).join(
    film_actor
).join(
    Film
).filter(
    Film.film_id == film_id
).all()
```

**Consultas con agregación:**

```python
from sqlalchemy import func

# Contar actores por película
count = db.session.query(
    func.count(Actor.actor_id)
).join(
    film_actor
).filter(
    film_actor.c.film_id == film_id
).scalar()
```

## 📁 Estructura del Proyecto

```
Clase 10/
├── app/
│   ├── __init__.py              # Configuración Flask y SQLAlchemy
│   ├── models.py                # Modelos Actor y Film
│   └── routes.py                # Rutas de la API
├── db_config.py                 # Configuración de conexión (legacy)
├── api.http                     # Archivo de pruebas HTTP
├── .env                         # Variables de entorno
├── .gitignore                   # Archivos ignorados
└── requirements.txt             # Dependencias
```

## 🚀 Configuración Inicial

### Paso 1: Crear Entorno Virtual

```bash
cd "Clase 10"
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Activar (Linux/Mac)
source .venv/bin/activate
```

### Paso 2: Instalar Dependencias

```bash
pip install Flask Flask-SQLAlchemy pymysql python-dotenv
```

O crear `requirements.txt`:

```txt
Flask>=3.0.0
Flask-SQLAlchemy>=3.0.0
pymysql>=1.0.0
python-dotenv>=1.0.0
```

### Paso 3: Configurar Variables de Entorno

Crear archivo `.env`:

```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASS=tu_contraseña
DB_NAME=sakila
```

### Paso 4: Ejecutar la Aplicación

```bash
python run.py
```

La aplicación estará disponible en `http://localhost:3000`

## 🔍 Endpoints Disponibles

### Actores

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/actors` | Obtener todos los actores |
| GET | `/actors/<actor_id>` | Obtener un actor específico |
| POST | `/actors` | Crear un nuevo actor (nombres se convierten a mayúsculas) |
| POST | `/actors/bulk` | Crear varios actores en bloque |
| DELETE | `/actors/<actor_id>` | Eliminar un actor |

### Películas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/films` | Obtener películas con paginación (`?limit=10&offset=0`) |
| GET | `/films/<film_id>` | Obtener una película específica |
| POST | `/films` | Crear una nueva película |
| PUT | `/films/<film_id>` | Actualizar una película |
| DELETE | `/films/<film_id>` | Eliminar una película |

### General

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Mensaje de bienvenida de la API |

## 💡 Ejemplos de Uso con api.http

El archivo `api.http` contiene ejemplos de todas las peticiones. Puedes usarlo con extensiones como REST Client en VS Code.

**Ejemplo de creación de actor:**

```http
POST http://localhost:3000/actors
Content-Type: application/json

{
  "first_name": "Tom",
  "last_name": "Hanks"
}
```

**Ejemplo de creación en bloque:**

```http
POST http://localhost:3000/actors/bulk
Content-Type: application/json

[
  {
    "first_name": "Scarlett",
    "last_name": "Johansson"
  },
  {
    "first_name": "Ricardo",
    "last_name": "Darín"
  }
]
```

## 🔒 Buenas Prácticas

### 1. Manejo de Sesiones
- ✅ Siempre haz `commit()` después de cambios
- ✅ Usa `rollback()` en bloques try-except
- ✅ Cierra sesiones apropiadamente

### 2. Validación de Datos
- ✅ Valida datos antes de crear/actualizar
- ✅ Maneja casos donde no se encuentra el recurso (404)
- ✅ Retorna mensajes de error claros
- ✅ Convierte nombres a mayúsculas automáticamente en creación de actores
- ✅ Valida formato de datos (listas vs objetos) en operaciones bulk

### 3. Rendimiento
- ✅ Usa `lazy='dynamic'` para relaciones grandes
- ✅ Implementa paginación para listas grandes (ej: `/films?limit=10&offset=0`)
- ✅ Limita el máximo de resultados por petición (ej: máximo 100 películas)
- ✅ Usa `query.filter()` en lugar de cargar todo y filtrar en Python
- ✅ Usa `offset()` y `limit()` para paginación eficiente

### 4. Código Limpio
- ✅ Usa métodos `to_dict()` en modelos para serialización
- ✅ Implementa `__repr__()` para debugging y representación legible
- ✅ Separa lógica de negocio de las rutas usando `register_routes()`
- ✅ Usa nombres descriptivos para modelos y relaciones
- ✅ Usa Factory Pattern (`create_app()`) para mejor organización
- ✅ Maneja errores con try-except y rollback en todas las operaciones de escritura

## 📚 Recursos Adicionales

- [Documentación oficial de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [SQLAlchemy Relationships](https://docs.sqlalchemy.org/en/latest/orm/relationships.html)
- [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)

## ⚠️ Errores Comunes

1. **Olvidar hacer commit**: Los cambios no se guardan sin `db.session.commit()`
2. **Relaciones circulares**: Asegúrate de importar modelos correctamente
3. **Lazy loading**: Entiende cuándo usar `lazy='dynamic'` vs `lazy='select'`
4. **N+1 queries**: Usa `joinedload()` o `selectinload()` para optimizar
5. **Tipos de datos incorrectos**: Verifica que los tipos coincidan con la BD

## 🎓 Siguiente Paso

Una vez que domines estos conceptos, estarás listo para:
- Implementar autenticación y autorización
- Crear migraciones de base de datos con Alembic
- Optimizar consultas complejas
- Implementar paginación y filtrado avanzado
- Crear APIs más complejas con múltiples relaciones

---

**¡Sigue practicando y creando tus propios modelos y relaciones!** 🚀

*Recuerda: SQLAlchemy es una herramienta poderosa. Tómate el tiempo de entender cómo funcionan las relaciones y las consultas para aprovechar todo su potencial.*

