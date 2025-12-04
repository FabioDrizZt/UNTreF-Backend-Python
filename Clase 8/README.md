# 📚 Clase 8: Flask - Introducción a APIs REST

Bienvenido a la Clase 8 del curso de Python. En esta clase aprenderás los fundamentos de Flask, un framework web ligero y poderoso para crear aplicaciones web y APIs REST en Python.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Crear una aplicación Flask básica
- ✅ Definir rutas y endpoints
- ✅ Usar Blueprints para organizar rutas
- ✅ Renderizar templates HTML con Jinja2
- ✅ Crear APIs REST que retornen JSON
- ✅ Integrar Flask con bases de datos MySQL
- ✅ Estructurar una aplicación Flask de forma profesional

## 📋 Temas Cubiertos

### 1. Introducción a Flask

Flask es un microframework web para Python que permite crear aplicaciones web de forma rápida y sencilla.

**Características principales:**
- Ligero y minimalista
- Flexible y extensible
- Ideal para APIs REST
- Gran comunidad y documentación

**Instalación:**
```bash
pip install Flask
```

### 2. Creación de una Aplicación Flask Básica

**Estructura mínima:**

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

**Ejecutar la aplicación:**
```bash
python run.py
```

La aplicación estará disponible en `http://localhost:5000`

### 3. Rutas y Endpoints

Las rutas definen las URLs que tu aplicación puede manejar.

**Rutas básicas:**

```python
@app.route("/")
def index():
    return "Página principal"

@app.route("/saludo/")
def saludo():
    return "¡Hola!"

@app.route("/saludo/<nombre>")
def saludo_personalizado(nombre):
    return f"¡Hola, {nombre}!"
```

**Parámetros en rutas:**
- `<nombre>`: String por defecto
- `<int:id>`: Entero
- `<float:precio>`: Decimal
- `<path:ruta>`: Ruta completa

### 4. Blueprints

Los Blueprints permiten organizar rutas en módulos separados, facilitando la estructura de aplicaciones grandes.

**Ventajas:**
- Organización modular
- Reutilización de código
- Facilita el mantenimiento
- Permite registrar rutas de forma centralizada

**Ejemplo de Blueprint:**

```python
from flask import Blueprint

# Crear el Blueprint
general_bp = Blueprint("general_bp", __name__)

# Definir rutas en el Blueprint
@general_bp.route("/")
def hello_world():
    return "Bienvenidos a Flask!!"

@general_bp.route("/saludo/<nombre>")
def saludo(nombre):
    return f"¡Hola, {nombre}!"
```

**Registrar Blueprint en la aplicación:**

```python
from flask import Flask
from app.general_routes import general_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(general_bp)
    return app
```

### 5. Estructura de Aplicación Flask

Una estructura profesional de Flask organiza el código en módulos:

```
app/
├── __init__.py          # Factory function para crear la app
├── routes.py            # Registro de todos los Blueprints
├── general_routes.py    # Blueprint de rutas generales
├── products_routes.py   # Blueprint de productos
├── actor_routes.py      # Blueprint de actores
├── actor_queries.py     # Funciones de consulta a BD
└── config/
    └── db_config.py     # Configuración de base de datos
```

**Factory Pattern:**

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes import register_routes
    register_routes(app)
    
    return app

app = create_app()
```

### 6. Retornar JSON

Para crear APIs REST, Flask permite retornar JSON fácilmente.

**Usando jsonify:**

```python
from flask import jsonify

@app.route("/api/productos")
def lista_productos():
    productos = ["iPhone", "MacBook Pro", "iPad"]
    return jsonify(productos), 200

@app.route("/api/productos_dict")
def lista_productos_dict():
    productos = [
        {"nombre": "iPhone", "precio": 1000},
        {"nombre": "MacBook Pro", "precio": 5000}
    ]
    return jsonify(productos), 200
```

**Códigos de estado HTTP comunes:**
- `200`: OK - Solicitud exitosa
- `201`: Created - Recurso creado exitosamente
- `400`: Bad Request - Solicitud inválida
- `404`: Not Found - Recurso no encontrado
- `500`: Internal Server Error - Error del servidor

### 7. Renderizado de Templates HTML

Flask usa Jinja2 como motor de templates para renderizar HTML.

**Estructura de templates:**

```
app/
└── templates/
    └── productos.html
```

**Ejemplo de template:**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Productos</title>
</head>
<body>
    <h1>Listado de productos</h1>
    <ul>
        {% for producto in productos %}
        <li>{{ producto }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Renderizar template desde Flask:**

```python
from flask import render_template

@app.route("/productos")
def productos():
    lista_productos = ["iPhone", "MacBook Pro", "iPad"]
    return render_template("productos.html", productos=lista_productos)
```

**Sintaxis Jinja2 básica:**
- `{{ variable }}`: Mostrar variable
- `{% for item in items %}`: Bucle for
- `{% if condition %}`: Condicional
- `{% block content %}`: Bloques (herencia)

### 8. Integración con Bases de Datos

Flask puede integrarse fácilmente con MySQL usando las funciones de consulta creadas anteriormente.

**Ejemplo:**

```python
from flask import Blueprint, jsonify
from app.actor_queries import get_actors_dict

actor_bp = Blueprint("actor", __name__)

@actor_bp.route("/actores")
def actores():
    actores = get_actors_dict(limit=25)
    return jsonify(actores), 200
```

### 9. Manejo de Errores

Flask permite definir manejadores de errores personalizados.

```python
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Recurso no encontrado"), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Error interno del servidor"), 500
```

## 📁 Estructura del Proyecto

```
Clase 8/
├── app/
│   ├── __init__.py              # Factory function
│   ├── routes.py                 # Registro de Blueprints
│   ├── general_routes.py         # Rutas generales
│   ├── products_routes.py        # Rutas de productos
│   ├── actor_routes.py           # Rutas de actores
│   ├── actor_queries.py          # Consultas a BD
│   ├── config/
│   │   └── db_config.py          # Configuración BD
│   └── templates/
│       └── productos.html       # Template HTML
├── run.py                        # Punto de entrada
└── requirements.txt             # Dependencias
```

## 🚀 Configuración Inicial

### Paso 1: Crear Entorno Virtual

```bash
cd "Clase 8"
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

### Paso 3: Configurar Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

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

La aplicación estará disponible en `http://localhost:5000`

## 🔍 Endpoints Disponibles

### Rutas Generales
- `GET /` - Página de bienvenida
- `GET /saludo/` - Saludo genérico
- `GET /saludo/<nombre>` - Saludo personalizado

### Rutas de Productos
- `GET /productos` - Vista HTML de productos
- `GET /api/lista_productos` - API JSON de productos
- `GET /api/lista_dict_productos` - API JSON de productos (diccionarios)

### Rutas de Actores
- `GET /actores` - Lista de actores desde BD
- `GET /api/lista_actores` - API de actores
- `GET /api/lista_films_actor/<actor_id>` - Películas de un actor

## 💡 Conceptos Clave

### Decoradores
Los decoradores `@app.route()` y `@blueprint.route()` asocian funciones con URLs.

### Request y Response
- **Request**: Datos que llegan al servidor
- **Response**: Datos que el servidor retorna

### JSON vs HTML
- **JSON**: Para APIs REST (comunicación entre aplicaciones)
- **HTML**: Para páginas web (interfaz de usuario)

### Modo Debug
`app.run(debug=True)` activa:
- Recarga automática al cambiar código
- Mensajes de error detallados
- Debugger interactivo

## 📚 Recursos Adicionales

- [Documentación oficial de Flask](https://flask.palletsprojects.com/)
- [Jinja2 Template Designer Documentation](https://jinja.palletsprojects.com/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [REST API Tutorial](https://restfulapi.net/)

## ⚠️ Errores Comunes

1. **No activar el entorno virtual**: Activa venv antes de instalar Flask
2. **Rutas duplicadas**: No definas la misma ruta dos veces
3. **Templates no encontrados**: Asegúrate de que la carpeta `templates/` exista
4. **Importaciones circulares**: Evita importar entre módulos de forma circular
5. **Olvidar registrar Blueprints**: Usa `app.register_blueprint()`

## 🎓 Siguiente Paso

Una vez que domines estos conceptos, estarás listo para:
- Implementar operaciones CRUD completas (Clase 9)
- Manejar métodos HTTP (GET, POST, PUT, DELETE)
- Trabajar con query parameters
- Validar datos de entrada
- Implementar autenticación y autorización

---

**¡Sigue practicando y creando tus propias rutas!** 🚀

*Recuerda: Flask es un framework minimalista pero poderoso. Empieza simple y ve agregando complejidad gradualmente.*

