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

**Configuración básica:**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configurar la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)
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
    __tablename__ = 'actor'
    
    actor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relación many-to-many con Film
    films = db.relationship(
        'Film',
        secondary='film_actor',
        back_populates='actors',
        lazy='dynamic'
    )
    
    def to_dict(self):
        return {
            'actor_id': self.actor_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'last_update': self.last_update.isoformat() if self.last_update else None
        }
```

**Modelo Film:**

```python
class Film(db.Model):
    __tablename__ = 'film'
    
    film_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    release_year = db.Column(db.Integer)
    # ... otros campos
    
    # Relación many-to-many con Actor
    actors = db.relationship(
        'Actor',
        secondary='film_actor',
        back_populates='films',
        lazy='dynamic'
    )
    
    def to_dict(self):
        return {
            'film_id': self.film_id,
            'title': self.title,
            'description': self.description,
            'release_year': self.release_year
        }
```

**Tipos de columnas comunes:**
- `db.Integer`: Números enteros
- `db.String(length)`: Cadenas de texto con longitud máxima
- `db.Text`: Texto largo sin límite
- `db.DateTime`: Fechas y horas
- `db.Boolean`: Valores booleanos
- `db.Float`: Números decimales

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
    data = request.get_json()
    
    actor = Actor(
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    
    db.session.add(actor)
    db.session.commit()
    
    return jsonify(actor.to_dict()), 201
```

**Crear varios actores en bloque:**

```python
@app.route('/actors/bulk', methods=['POST'])
def create_actors_bulk():
    data = request.get_json()  # Lista de actores
    
    actors = []
    for actor_data in data:
        actor = Actor(
            first_name=actor_data['first_name'],
            last_name=actor_data['last_name']
        )
        actors.append(actor)
        db.session.add(actor)
    
    db.session.commit()
    
    return jsonify([actor.to_dict() for actor in actors]), 201
```

#### READ - Leer Registros

**Obtener todos los actores:**

```python
@app.route('/actors', methods=['GET'])
def get_actors():
    actors = Actor.query.all()
    return jsonify([actor.to_dict() for actor in actors]), 200
```

**Obtener un actor específico:**

```python
actor = Actor.query.get(actor_id)
# o
actor = Actor.query.filter_by(actor_id=actor_id).first()
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

#### UPDATE - Actualizar Registros

```python
@app.route('/films/<int:film_id>', methods=['PUT'])
def update_film(film_id):
    film = Film.query.get(film_id)
    
    if not film:
        return jsonify({'message': 'Film not found'}), 404
    
    data = request.get_json()
    
    film.title = data.get('title', film.title)
    film.description = data.get('description', film.description)
    film.release_year = data.get('release_year', film.release_year)
    
    db.session.commit()
    
    return jsonify(film.to_dict()), 200
```

#### DELETE - Eliminar Registros

```python
@app.route('/films/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    film = Film.query.get(film_id)
    
    if not film:
        return jsonify({'message': 'Film not found'}), 404
    
    db.session.delete(film)
    db.session.commit()
    
    return jsonify({'message': 'Film deleted'}), 200
```

### 7. Trabajar con Relaciones

**Asociar un actor a una película:**

```python
@app.route('/actors/<int:actor_id>/films/<int:film_id>', methods=['POST'])
def associate_actor_film(actor_id, film_id):
    actor = Actor.query.get(actor_id)
    film = Film.query.get(film_id)
    
    if not actor or not film:
        return jsonify({'message': 'Actor or Film not found'}), 404
    
    # Agregar la relación
    actor.films.append(film)
    db.session.commit()
    
    return jsonify({
        'message': 'Actor associated with film',
        'actor': actor.to_dict(),
        'film': film.to_dict()
    }), 200
```

**Obtener películas con sus actores:**

```python
@app.route('/films/actors', methods=['GET'])
def get_films_with_actors():
    films = Film.query.all()
    
    result = []
    for film in films:
        film_dict = film.to_dict()
        film_dict['actors'] = [actor.to_dict() for actor in film.actors.all()]
        result.append(film_dict)
    
    return jsonify(result), 200
```

**Obtener actores de una película específica:**

```python
@app.route('/films/<int:film_id>/actors', methods=['GET'])
def get_film_actors(film_id):
    film = Film.query.get(film_id)
    
    if not film:
        return jsonify({'message': 'Film not found'}), 404
    
    actors = [actor.to_dict() for actor in film.actors.all()]
    
    return jsonify({
        'film_id': film_id,
        'title': film.title,
        'actors': actors
    }), 200
```

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
- Usa `rollback()` en caso de error
- Maneja excepciones apropiadamente

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
| POST | `/actors` | Crear un nuevo actor |
| POST | `/actors/bulk` | Crear varios actores en bloque |

### Películas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/films` | Obtener todas las películas |
| POST | `/films` | Crear una nueva película |
| PUT | `/films/<id>` | Actualizar una película |
| DELETE | `/films/<id>` | Eliminar una película |

### Relaciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/actors/<actor_id>/films/<film_id>` | Asociar actor a película |
| GET | `/films/actors` | Obtener todas las películas con sus actores |
| GET | `/films/<film_id>/actors` | Obtener actores de una película |

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

### 3. Rendimiento
- ✅ Usa `lazy='dynamic'` para relaciones grandes
- ✅ Considera paginación para listas grandes
- ✅ Usa `query.filter()` en lugar de cargar todo y filtrar en Python

### 4. Código Limpio
- ✅ Usa métodos `to_dict()` en modelos para serialización
- ✅ Separa lógica de negocio de las rutas
- ✅ Usa nombres descriptivos para modelos y relaciones

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

