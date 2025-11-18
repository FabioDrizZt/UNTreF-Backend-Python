# 📝 Código en Clase - Clase 3

Esta carpeta contiene los ejemplos prácticos y demostraciones del profesor durante la Clase 3. Estos archivos muestran cómo crear funciones, manejar errores y usar herramientas avanzadas de Python.

## 📄 Archivos Disponibles

### `functions.py`
**Tema**: Definición y uso de funciones

**Conceptos cubiertos**:
- Definición de funciones con `def`
- Parámetros de función
- Retorno de valores con `return`
- Parámetros por defecto
- Argumentos por posición y por nombre
- Operador `*args` para múltiples argumentos
- Operador `**kwargs` para argumentos con nombre
- Funciones lambda (funciones anónimas)
- Comparación con JavaScript (arrow functions)

**Ejemplo clave**:
```python
def saludo(nombre, edad=25):
    return f"Hola {nombre}, tienes {edad} años"

# Con *args
def sumar(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# Con **kwargs
def mostrar_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
saludar = lambda nombre: f"Hola {nombre}"
```

---

### `try-except.py`
**Tema**: Manejo de excepciones y errores

**Conceptos cubiertos**:
- Estructura `try-except`
- Múltiples bloques `except`
- Bloque `finally`
- Tipos de excepciones comunes:
  - `ZeroDivisionError`: División por cero
  - `TypeError`: Tipo de dato incorrecto
  - `NameError`: Variable no definida
  - `IndexError`: Índice fuera de rango
  - `FileNotFoundError`: Archivo no encontrado
  - `KeyboardInterrupt`: Interrupción del usuario
- Crear excepciones personalizadas con `raise`
- Manejo de excepciones en funciones

**Ejemplo clave**:
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Finalizado")

# Excepción personalizada
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
```

---

### `range.py`
**Tema**: Función `range()` para generar secuencias

**Conceptos cubiertos**:
- `range(stop)`: Genera números de 0 a stop-1
- `range(start, stop)`: Genera números de start a stop-1
- `range(start, stop, step)`: Genera números con incremento step
- Rangos descendentes (step negativo)
- Conversión a lista con `list(range())`
- Uso en bucles `for`

**Ejemplo clave**:
```python
range(10)        # 0, 1, 2, ..., 9
range(1, 11)     # 1, 2, 3, ..., 10
range(2, 11, 2)  # 2, 4, 6, 8, 10
range(10, 0, -1) # 10, 9, 8, ..., 1
```

---

### `Metodos.py`
**Tema**: Métodos útiles de Python

**Conceptos cubiertos**:
- Métodos integrados de Python
- Funciones útiles para diferentes tipos de datos
- Métodos de conversión y validación

**Nota**: Este archivo contiene ejemplos de métodos que pueden ser útiles en diferentes contextos.

---

### `Cast Functions.py`
**Tema**: Funciones de conversión de tipos

**Conceptos cubiertos**:
- `int()`: Conversión a entero
- `str()`: Conversión a string
- `float()`: Conversión a decimal
- `bool()`: Conversión a booleano
- Conversiones seguras con manejo de errores

**Ejemplo clave**:
```python
numero = int("100")
texto = str(100)
decimal = float("3.14")
```

---

## 🚀 Cómo Usar Estos Archivos

1. **Ejecuta cada archivo**:
   ```bash
   python functions.py
   python try-except.py
   python range.py
   python Metodos.py
   python "Cast Functions.py"
   ```

2. **Experimenta modificando**:
   - Crea tus propias funciones con diferentes parámetros
   - Prueba diferentes tipos de errores
   - Experimenta con `range()` y diferentes valores
   - Modifica las funciones lambda

3. **Combina conceptos**:
   - Usa manejo de errores en tus funciones
   - Combina `*args` y `**kwargs`
   - Crea funciones que usen `range()`

## 💡 Consejos de Estudio

- **Practica creando funciones**: Escribe funciones para resolver problemas comunes
- **Maneja errores proactivamente**: Siempre piensa qué puede salir mal
- **Experimenta con lambda**: Úsalas para operaciones simples y cortas
- **Lee los comentarios**: Muchos archivos tienen comparaciones con JavaScript
- **Prueba diferentes excepciones**: Intenta provocar diferentes tipos de errores

## 🔗 Relación con los Ejercicios

Estos ejemplos te preparan para resolver los ejercicios prácticos en [`../Ejercicios/`](../Ejercicios/README.md), donde aplicarás funciones y manejo de errores en problemas reales.

---

**📚 Siguiente paso**: Practica con los [Ejercicios de la Clase 3](../Ejercicios/README.md) para consolidar estos conceptos.

