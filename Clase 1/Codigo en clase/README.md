# 📝 Código en Clase - Clase 1

Esta carpeta contiene los ejemplos prácticos y demostraciones del profesor durante la Clase 1. Estos archivos muestran los conceptos fundamentales de Python de manera práctica.

## 📄 Archivos Disponibles

### `index.py`
**Tema**: Introducción a `print()` y manejo de texto

**Conceptos cubiertos**:
- Uso de `print()` para mostrar información
- Comillas simples (`'`) y dobles (`"`)
- Strings multilínea con triple comillas (`"""`)
- Escapado de caracteres (`\"`, `\'`)
- Parámetros `sep` y `end` en `print()`
- Comentarios de una línea (`#`) y multilínea (`"""`)

**Ejemplo clave**:
```python
print("Hola", "D'artagnan", sep="-", end="\n")
```

---

### `variables.py`
**Tema**: Variables y asignación

**Conceptos cubiertos**:
- Declaración de variables
- Tipos de datos básicos (str, int, float, bool)
- Verificación de tipos con `type()`
- F-strings para formateo de texto
- Asignación múltiple de variables
- Intercambio de valores entre variables
- Convención para constantes (MAYÚSCULAS)

**Ejemplo clave**:
```python
nombre = "D'artagnan"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Asignación múltiple
a, b, c = 1, 2, 3
```

---

### `types.py`
**Tema**: Tipos de datos en Python

**Conceptos cubiertos**:
- Identificación de tipos con `type()`
- Verificación de tipos con `isinstance()`
- Tipos numéricos: `int`, `float`, `complex`
- Tipos booleanos: `bool`
- Tipos de texto: `str`
- Tipo especial: `NoneType`
- Tipos compuestos: `list`, `tuple`, `dict`, `set`

**Ejemplo clave**:
```python
print(type(1))        # <class 'int'>
print(type(1.0))      # <class 'float'>
print(isinstance(1, int))  # True
```

---

### `cast.py`
**Tema**: Conversión de tipos (casting)

**Conceptos cubiertos**:
- Conversión de string a entero: `int()`
- Conversión de número a string: `str()`
- Conversión a float: `float()`
- Conversión a bool: `bool()`

**Ejemplo clave**:
```python
print(int("100") + 2)      # 102
print("100" + str(2))      # "1002"
```

## 🚀 Cómo Usar Estos Archivos

1. **Lee el código**: Abre cada archivo y lee los comentarios
2. **Ejecuta el código**: Corre cada archivo para ver la salida
   ```bash
   python index.py
   python variables.py
   python types.py
   python cast.py
   ```
3. **Experimenta**: Modifica los valores y observa qué pasa
4. **Practica**: Intenta escribir tus propios ejemplos similares

## 💡 Consejos de Estudio

- **No copies y pegues**: Escribe el código tú mismo para memorizarlo mejor
- **Modifica los ejemplos**: Cambia valores y observa los resultados
- **Lee los comentarios**: Contienen información valiosa sobre cada concepto
- **Experimenta con errores**: Intenta hacer cosas incorrectas para entender los límites

## 🔗 Relación con los Ejercicios

Estos ejemplos te preparan para los ejercicios en [`../Ejercicios/`](../Ejercicios/README.md). Los conceptos mostrados aquí son la base para resolver las actividades prácticas.

---

**📚 Siguiente paso**: Una vez que entiendas estos conceptos, practica con los [Ejercicios de la Clase 1](../Ejercicios/README.md).

