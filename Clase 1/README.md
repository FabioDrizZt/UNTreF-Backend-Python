# 📚 Clase 1: Fundamentos de Python

Esta clase introduce los conceptos fundamentales de Python: variables, tipos de datos, operaciones básicas y cómo trabajar con ellos.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Declarar y usar variables en Python
- ✅ Identificar y trabajar con diferentes tipos de datos (int, float, str, bool)
- ✅ Realizar operaciones matemáticas básicas
- ✅ Convertir entre tipos de datos (casting)
- ✅ Usar f-strings para formatear texto
- ✅ Entender el tipado fuerte de Python

## 📁 Contenido de la Clase

### [📝 Código en Clase](./Codigo%20en%20clase/README.md)

Ejemplos prácticos y demostraciones que cubren:

- **`index.py`**: Introducción a `print()`, comillas simples y dobles, comentarios
- **`variables.py`**: Declaración de variables, tipos, f-strings, asignación múltiple
- **`types.py`**: Identificación de tipos de datos con `type()` e `isinstance()`
- **`cast.py`**: Conversión entre tipos de datos (int, str, float)

### [💪 Ejercicios](./Ejercicios/README.md)

10 actividades prácticas que refuerzan los conceptos aprendidos:

1. Mensaje de Bienvenida
2. Información Personal
3. Operaciones Matemáticas
4. Manipulación de Texto
5. Año de Nacimiento
6. Generador de Apodos
7. Calculadora de Propinas
8. Módulo math
9. Tarjetas de Presentación
10. Limpieza de Pantalla

## 🔑 Conceptos Clave

### Variables

En Python, las variables se crean simplemente asignando un valor:

```python
nombre = "D'artagnan"
edad = 25
```

### Tipos de Datos Principales

- **`int`**: Números enteros (1, 0, -5)
- **`float`**: Números decimales (1.0, 3.14, -5.5)
- **`str`**: Cadenas de texto ("Hola", 'Mundo')
- **`bool`**: Valores booleanos (True, False)
- **`NoneType`**: Valor nulo (None)

### F-strings (Formateo de Texto)

```python
nombre = "D'artagnan"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años")
```

### Tipado Fuerte

Python tiene tipado fuerte, lo que significa que no realiza conversiones automáticas:

```python
# Esto causará un error:
# print(10 + "2")  # TypeError

# Debes convertir explícitamente:
print(10 + int("2"))  # ✅ Correcto
```

## 📖 Recursos Adicionales

- [Documentación oficial: Tipos de datos](https://docs.python.org/es/3/library/stdtypes.html)
- [PEP 498 - Literal String Interpolation (f-strings)](https://peps.python.org/pep-0498/)

## ➡️ Siguiente Paso

Una vez que domines estos conceptos, continúa con [Clase 2: Control de Flujo](../Clase%202/README.md) para aprender sobre condicionales y operadores.

---

**💡 Tip**: Practica escribiendo código tú mismo. No solo leas los ejemplos, ¡escríbelos y modifícalos!

