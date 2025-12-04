# 📚 Clase 9: Flask - Operaciones CRUD Completas

Bienvenido a la Clase 9 del curso de Python. En esta clase profundizarás en Flask aprendiendo a implementar operaciones CRUD completas (Create, Read, Update, Delete) y a trabajar con query parameters para crear APIs REST funcionales.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Implementar operaciones CRUD completas en Flask
- ✅ Manejar diferentes métodos HTTP (GET, POST, PUT, DELETE)
- ✅ Trabajar con query parameters para filtrado y búsqueda
- ✅ Leer y escribir datos en archivos JSON
- ✅ Validar datos de entrada en APIs
- ✅ Manejar errores y códigos de estado HTTP apropiados
- ✅ Crear APIs REST funcionales y bien estructuradas

## 📋 Temas Cubiertos

### 1. Operaciones CRUD

CRUD son las operaciones básicas de cualquier API:
- **Create** (Crear): Agregar nuevos recursos
- **Read** (Leer): Obtener recursos existentes
- **Update** (Actualizar): Modificar recursos existentes
- **Delete** (Eliminar): Eliminar recursos

### 2. Métodos HTTP

Cada operación CRUD corresponde a un método HTTP específico:

| Operación | Método HTTP | Descripción |
|-----------|-------------|------------|
| Create | POST | Crear un nuevo recurso |
| Read | GET | Obtener uno o varios recursos |
| Update | PUT/PATCH | Actualizar un recurso existente |
| Delete | DELETE | Eliminar un recurso |

### 3. GET - Leer Recursos

**Obtener todos los recursos:**

```python
@app.route("/movies", methods=["GET"])
def movies():
    movies = cargar_movies()
    return jsonify(movies), 200
```

**Obtener un recurso específico:**

```python
@app.route("/movies/<int:id>", methods=["GET"])
def get_movie(id):
    movies = cargar_movies()
    for movie in movies:
        if movie.get("id") == id:
            return jsonify(movie), 200
    return jsonify({"message": "Movie not found"}), 404
```

**Usando query parameters para filtrado:**

```python
@app.route("/movies", methods=["GET"])
def movies():
    movies = cargar_movies()
    
    # Filtrar por título
    title = request.args.get("title")
    if title:
        title = title.lower()
        movies = [m for m in movies if title in m.get("title", "").lower()]
    
    # Filtrar por año
    year = request.args.get("year")
    if year:
        year = int(year)
        movies = [m for m in movies if m.get("year") == year]
    
    if not movies:
        return jsonify({"message": "No movies found"}), 404
    
    return jsonify(movies), 200
```

**Ejemplos de uso:**
- `GET /movies` - Obtener todas las películas
- `GET /movies?title=matrix` - Filtrar por título
- `GET /movies?year=1999` - Filtrar por año
- `GET /movies?title=matrix&year=1999` - Múltiples filtros

### 4. POST - Crear Recursos

**Crear un nuevo recurso:**

```python
@app.route("/movies", methods=["POST"])
def add_movie():
    movies = cargar_movies()
    
    # Obtener datos del request
    new_movie = request.get_json()
    
    # Validar datos
    if not new_movie:
        return jsonify({"message": "Invalid movie data"}), 400
    
    # Generar ID automático
    new_movie["id"] = max(m.get("id", 0) for m in movies) + 1
    
    # Agregar a la lista
    movies.append(new_movie)
    
    # Guardar en archivo
    guardar_movies(movies)
    
    return jsonify(new_movie), 201
```

**Ejemplo de request:**
```json
POST /movies
Content-Type: application/json

{
  "title": "Nueva Película",
  "year": 2024,
  "genre": "Acción"
}
```

### 5. PUT - Actualizar Recursos

**Actualizar un recurso existente:**

```python
@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    movies = cargar_movies()
    
    for movie in movies:
        if movie.get("id") == id:
            # Obtener datos actualizados
            updated_data = request.get_json()
            
            if not updated_data:
                return jsonify({"message": "Invalid movie data"}), 400
            
            # Combinar datos existentes con nuevos
            updated_movie = {
                **movie,           # Datos existentes
                **updated_data,    # Nuevos datos
            }
            
            # Reemplazar en la lista
            movies.remove(movie)
            movies.append(updated_movie)
            
            # Guardar cambios
            guardar_movies(movies)
            
            return jsonify(updated_movie), 200
    
    return jsonify({"message": "Movie not found"}), 404
```

**Operador de desempaquetado (`**`):**
- `**movie`: Desempaqueta el diccionario existente
- `**updated_data`: Desempaqueta los nuevos datos
- Los nuevos datos sobrescriben los existentes

### 6. DELETE - Eliminar Recursos

**Eliminar un recurso:**

```python
@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    movies = cargar_movies()
    
    for movie in movies:
        if movie.get("id") == id:
            deleted_movie = movie
            movies.remove(movie)
            guardar_movies(movies)
            return jsonify({
                "message": "Movie deleted",
                "deleted_movie": deleted_movie
            }), 200
    
    return jsonify({"message": "Movie not found"}), 404
```

### 7. Trabajo con Archivos JSON

**Leer datos desde JSON:**

```python
import json
import os

def cargar_movies():
    movies_path = os.path.join(os.getcwd(), "app", "data", "movies.json")
    
    try:
        with open(movies_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
```

**Guardar datos en JSON:**

```python
def guardar_movies(movies):
    movies_path = os.path.join(os.getcwd(), "app", "data", "movies.json")
    
    try:
        with open(movies_path, "w", encoding="utf-8") as f:
            json.dump(movies, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error guardando: {e}")
```

**Buenas prácticas:**
- Usar `encoding="utf-8"` para caracteres especiales
- Usar `indent=2` para formato legible
- Manejar excepciones apropiadamente
- Validar estructura JSON antes de guardar

### 8. Query Parameters

Los query parameters permiten filtrar y buscar datos sin modificar la estructura de la URL.

**Acceder a query parameters:**

```python
from flask import request

# Obtener un parámetro
title = request.args.get("title")

# Obtener con valor por defecto
limit = request.args.get("limit", default=10, type=int)

# Obtener múltiples valores
tags = request.args.getlist("tag")
```

**Ejemplos de URLs con query parameters:**
- `/movies?title=matrix`
- `/movies?year=1999&genre=action`
- `/movies?limit=10&offset=20`

### 9. Validación de Datos

Es importante validar los datos antes de procesarlos.

**Validación básica:**

```python
@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    
    # Validar que existan datos
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    # Validar campos requeridos
    required_fields = ["title", "year"]
    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"Missing required field: {field}"
            }), 400
    
    # Validar tipos de datos
    if not isinstance(data.get("year"), int):
        return jsonify({"message": "Year must be an integer"}), 400
    
    # Continuar con la creación...
```

### 10. Manejo de Errores

Flask permite manejar errores de forma centralizada.

**Manejador de errores 404:**

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Page not found"}), 404
```

**Códigos de estado HTTP comunes:**

| Código | Significado | Uso |
|--------|-------------|-----|
| 200 | OK | Operación exitosa |
| 201 | Created | Recurso creado exitosamente |
| 400 | Bad Request | Datos inválidos |
| 404 | Not Found | Recurso no encontrado |
| 500 | Internal Server Error | Error del servidor |

## 📁 Estructura del Proyecto

```
Clase 9/
├── app/
│   ├── __init__.py              # Configuración de Flask
│   ├── routes.py                 # Todas las rutas CRUD
│   └── data/
│       └── movies.json          # Archivo de datos JSON
├── run.py                        # Punto de entrada
└── requirements.txt              # Dependencias
```

## 🚀 Configuración Inicial

### Paso 1: Crear Entorno Virtual

```bash
cd "Clase 9"
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Activar (Linux/Mac)
source .venv/bin/activate
```

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar la Aplicación

```bash
python run.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🔍 Endpoints Disponibles

### Operaciones CRUD

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/movies` | Obtener todas las películas |
| GET | `/movies?title=<título>` | Filtrar por título |
| GET | `/movies?year=<año>` | Filtrar por año |
| GET | `/movies/<id>` | Obtener película por ID |
| POST | `/movies` | Crear nueva película |
| PUT | `/movies/<id>` | Actualizar película |
| DELETE | `/movies/<id>` | Eliminar película |

## 💡 Ejemplos de Uso

### Crear una película

```bash
curl -X POST http://localhost:5000/movies \
  -H "Content-Type: application/json" \
  -d '{"title": "Matrix", "year": 1999, "genre": "Sci-Fi"}'
```

### Obtener todas las películas

```bash
curl http://localhost:5000/movies
```

### Filtrar por título

```bash
curl http://localhost:5000/movies?title=matrix
```

### Actualizar una película

```bash
curl -X PUT http://localhost:5000/movies/1 \
  -H "Content-Type: application/json" \
  -d '{"year": 2000}'
```

### Eliminar una película

```bash
curl -X DELETE http://localhost:5000/movies/1
```

## 🔒 Buenas Prácticas

### 1. Validación de Datos
- ✅ Siempre valida datos de entrada
- ✅ Usa códigos de estado HTTP apropiados
- ✅ Retorna mensajes de error claros

### 2. Manejo de Archivos
- ✅ Usa rutas absolutas con `os.path.join()`
- ✅ Maneja excepciones al leer/escribir archivos
- ✅ Valida estructura JSON antes de guardar

### 3. Códigos de Estado
- ✅ 200: Operación exitosa
- ✅ 201: Recurso creado
- ✅ 400: Error del cliente (datos inválidos)
- ✅ 404: Recurso no encontrado
- ✅ 500: Error del servidor

### 4. Estructura de Respuestas
- ✅ Mantén consistencia en el formato JSON
- ✅ Incluye mensajes descriptivos
- ✅ Retorna el recurso creado/actualizado

## 📚 Recursos Adicionales

- [Flask Request Object](https://flask.palletsprojects.com/en/latest/api/#flask.Request)
- [HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [REST API Best Practices](https://restfulapi.net/)
- [JSON Schema Validation](https://json-schema.org/)

## ⚠️ Errores Comunes

1. **Olvidar especificar métodos HTTP**: Usa `methods=["GET", "POST"]`
2. **No validar datos**: Siempre valida antes de procesar
3. **Rutas duplicadas**: No definas la misma ruta con diferentes métodos sin especificarlos
4. **No manejar archivos**: Valida existencia y estructura de archivos JSON
5. **Códigos de estado incorrectos**: Usa los códigos apropiados para cada situación

## 🎓 Siguiente Paso

Una vez que domines estos conceptos, estarás listo para:
- Conectar APIs con bases de datos reales
- Implementar autenticación y autorización
- Usar ORMs como SQLAlchemy
- Crear APIs más complejas con relaciones
- Implementar paginación y ordenamiento
- Agregar tests automatizados

---

**¡Sigue practicando y creando tus propias APIs REST!** 🚀

*Recuerda: Una buena API es consistente, bien documentada y maneja errores apropiadamente.*

