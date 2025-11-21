# 📚 Clase 6: Diccionarios, Entornos Virtuales e Importaciones

Bienvenido a la Clase 6 del curso de Python. En esta clase aprenderás sobre diccionarios, una estructura de datos fundamental en Python, así como sobre la gestión de entornos virtuales y el uso de módulos.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Crear y manipular diccionarios en Python
- ✅ Trabajar con listas de diccionarios
- ✅ Crear y gestionar entornos virtuales (venv)
- ✅ Importar y usar módulos propios y externos
- ✅ Trabajar con archivos JSON para almacenar y leer datos
- ✅ Usar librerías externas como `tabulate` para formatear datos

## 📋 Temas Cubiertos

### 1. Diccionarios

Los diccionarios son estructuras de datos que almacenan pares clave-valor. Son muy útiles para representar datos estructurados.

**Conceptos clave:**
- Creación de diccionarios
- Acceso a valores mediante claves
- Modificación de elementos
- Eliminación de elementos con `del`
- Métodos: `keys()`, `values()`, `items()`
- Iteración sobre diccionarios

**Ejemplo básico:**
```python
producto = {
    'nombre': 'iPhone',
    'precio': 1000.52,
    'stock': 15,
    'wifi': True
}

# Acceder a valores
print(producto['nombre'])  # iPhone
print(producto['precio'])  # 1000.52

# Modificar valores
producto['precio'] = 1200.00

# Iterar sobre el diccionario
for clave, valor in producto.items():
    print(f'{clave}: {valor}')
```

### 2. Listas de Diccionarios

Combinar listas con diccionarios permite trabajar con colecciones de objetos estructurados.

**Uso común:**
- Representar múltiples registros de datos
- Almacenar información estructurada de manera organizada
- Procesar datos en formato tabular

### 3. Entornos Virtuales (venv)

Los entornos virtuales permiten aislar las dependencias de un proyecto, evitando conflictos entre diferentes proyectos.

**Comandos principales:**

```bash
# Crear un entorno virtual
python -m venv nombre_entorno

# Activar entorno virtual (Windows)
nombre_entorno\Scripts\activate

# Activar entorno virtual (Linux/Mac)
source nombre_entorno/bin/activate

# Desactivar entorno virtual
deactivate

# Instalar paquetes
pip install nombre_paquete

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

**Ventajas:**
- Aislamiento de dependencias entre proyectos
- Control de versiones de paquetes
- Facilita la colaboración y despliegue
- Evita conflictos con el sistema

### 4. Importaciones de Módulos

Python permite importar código de otros archivos o módulos externos.

**Formas de importar:**

```python
# Importar un módulo completo
import json
import productos

# Importar funciones específicas
from productos import productos_apple, productos_google

# Importar con alias
from productos import productos_apple as apple

# Importar todo (no recomendado)
from productos import *
```

**Módulos estándar vs externos:**
- **Módulos estándar**: Vienen con Python (ej: `json`, `os`, `sys`)
- **Módulos externos**: Se instalan con `pip` (ej: `tabulate`, `requests`)

### 5. Trabajo con JSON

JSON (JavaScript Object Notation) es un formato común para intercambiar datos. Python tiene soporte nativo para trabajar con JSON.

**Operaciones principales:**

```python
import json

# Escribir datos a un archivo JSON
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=4)

# Leer datos desde un archivo JSON
with open("datos.json", "r") as f:
    datos = json.load(f)
```

**Casos de uso:**
- Almacenar configuración
- Intercambiar datos entre aplicaciones
- Persistir información estructurada
- APIs y servicios web

### 6. Librerías Externas: Tabulate

`tabulate` es una librería que permite formatear datos en tablas de manera elegante.

**Instalación:**
```bash
pip install tabulate
```

**Uso básico:**
```python
from tabulate import tabulate

datos = [["Manzana", 10], ["Pera", 5]]
encabezados = ["Fruta", "Cantidad"]

print(tabulate(datos, headers=encabezados, tablefmt="fancy_grid"))
```

**Formatos disponibles:**
- `plain`: Tabla simple
- `grid`: Tabla con bordes
- `fancy_grid`: Tabla con bordes decorativos
- `html`: Formato HTML
- `latex`: Formato LaTeX
- `github`: Estilo GitHub

## 📁 Archivos de la Clase

Esta clase contiene los siguientes archivos de ejemplo:

- **`diccionarios.py`**: Ejemplos básicos de creación y manipulación de diccionarios
- **`lista de diccionarios.py`**: Trabajo con colecciones de diccionarios usando tabulate
- **`productos.py`**: Módulo con datos de ejemplo (productos de Apple y Google)
- **`ejemplo json.py`**: Ejemplos de lectura y escritura de archivos JSON
- **`ejemplo tabulate.py`**: Demostración de diferentes formatos de tablas

## 🚀 Cómo Usar los Ejemplos

### Paso 1: Crear un Entorno Virtual

```bash
# Navegar a la carpeta de la clase
cd "Clase 6"

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (Linux/Mac)
source venv/bin/activate
```

### Paso 2: Instalar Dependencias

```bash
# Instalar tabulate
pip install tabulate
```

### Paso 3: Ejecutar los Ejemplos

```bash
# Ejecutar ejemplo de diccionarios
python diccionarios.py

# Ejecutar ejemplo con JSON
python ejemplo\ json.py

# Ejecutar ejemplo con tabulate
python ejemplo\ tabulate.py

# Ejecutar ejemplo de lista de diccionarios
python lista\ de\ diccionarios.py
```

## 💡 Ejercicios Prácticos Sugeridos

1. **Crear un diccionario de estudiante** con nombre, edad, calificaciones y materias
2. **Crear una lista de estudiantes** y mostrar los datos en una tabla usando `tabulate`
3. **Guardar y cargar datos** de estudiantes desde un archivo JSON
4. **Crear un módulo propio** con funciones útiles y importarlo en otro archivo
5. **Experimentar con diferentes formatos** de tablas en `tabulate`

## 🔍 Conceptos Clave a Recordar

- **Diccionarios**: Estructura clave-valor, muy útil para datos estructurados
- **Entornos virtuales**: Aíslan dependencias por proyecto
- **Importaciones**: Permiten reutilizar código y usar librerías externas
- **JSON**: Formato estándar para intercambio de datos
- **pip**: Herramienta para instalar paquetes de Python

## 📚 Recursos Adicionales

- [Documentación de diccionarios en Python](https://docs.python.org/es/3/tutorial/datastructures.html#dictionaries)
- [Guía de módulos y paquetes](https://docs.python.org/es/3/tutorial/modules.html)
- [Documentación de venv](https://docs.python.org/es/3/library/venv.html)
- [Documentación de json](https://docs.python.org/es/3/library/json.html)
- [Documentación de tabulate](https://pypi.org/project/tabulate/)

## ⚠️ Errores Comunes

1. **Olvidar activar el entorno virtual**: Asegúrate de activar `venv` antes de instalar paquetes
2. **Importar módulos no instalados**: Verifica que el módulo esté instalado con `pip list`
3. **Claves inexistentes**: Usa `.get()` o verifica la existencia de claves antes de acceder
4. **Rutas de archivos**: En Windows, usa barras invertidas o rutas raw strings

## 🎓 Siguiente Paso

Una vez que domines estos conceptos, estarás listo para:
- Trabajar con APIs y servicios web
- Construir aplicaciones más complejas
- Gestionar proyectos con múltiples dependencias
- Integrar diferentes fuentes de datos

---

**¡Sigue practicando y experimentando con los ejemplos!** 🚀

*Recuerda: La mejor forma de aprender es haciendo. Modifica los ejemplos, crea tus propios diccionarios y experimenta con diferentes módulos.*

