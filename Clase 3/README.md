# 📚 Clase 3: Funciones y Manejo de Errores

Esta clase profundiza en la creación y uso de funciones en Python, incluyendo parámetros avanzados, funciones lambda, y el manejo de excepciones con try-except.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Definir funciones con `def`
- ✅ Usar parámetros posicionales y por nombre
- ✅ Trabajar con parámetros por defecto
- ✅ Usar `*args` para múltiples argumentos
- ✅ Usar `**kwargs` para argumentos con nombre
- ✅ Crear funciones lambda
- ✅ Manejar excepciones con `try-except`
- ✅ Crear excepciones personalizadas con `raise`
- ✅ Usar `range()` para generar secuencias
- ✅ Aplicar métodos útiles de Python

## 📁 Contenido de la Clase

### [📝 Código en Clase](./Codigo%20en%20clase/README.md)

Ejemplos prácticos que cubren:

- **`functions.py`**: Definición de funciones, parámetros, `*args`, `**kwargs`, lambda
- **`try-except.py`**: Manejo de excepciones, tipos de errores, `raise`
- **`range.py`**: Función `range()` para generar secuencias numéricas
- **`Metodos.py`**: Métodos útiles de Python
- **`Cast Functions.py`**: Funciones de conversión de tipos

### [💪 Ejercicios](./Ejercicios/README.md)

10 ejercicios prácticos que aplican los conceptos aprendidos:

1. Calculadora Básica
2. Convertir Tipos de Datos
3. Función con Valor por Defecto
4. Funciones Lambda
5. Función Saludo
6. Generar Secuencia de Números
7. Manejo de Excepciones en División
8. Manipular Texto
9. Sumar Múltiples Números
10. Validar Índice de Lista

## 🔑 Conceptos Clave

### Definición de Funciones

```python
def saludo(nombre):
    return f"Hola {nombre}"

print(saludo("D'artagnan"))
```

### Parámetros por Defecto

```python
def saludo(nombre, edad=25):
    return f"Hola {nombre}, tienes {edad} años"

saludo("Juan")  # Usa edad=25 por defecto
saludo("Juan", 30)  # Sobrescribe el valor por defecto
```

### Argumentos por Nombre

```python
def saludo(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años"

saludo(edad=21, nombre="D'artagnan")  # Orden no importa
```

### `*args` - Múltiples Argumentos

```python
def sumar(*args):
    total = 0
    for arg in args:
        total += arg
    return total

sumar(1, 2, 3, 4, 5)  # 15
```

### `**kwargs` - Argumentos con Nombre

```python
def mostrar_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mostrar_info(nombre="Juan", edad=25, ciudad="Buenos Aires")
```

### Funciones Lambda

```python
saludar = lambda nombre: f"Hola {nombre}"
sumar = lambda a, b: a + b

print(saludar("Juan"))  # "Hola Juan"
print(sumar(5, 3))      # 8
```

### Manejo de Excepciones

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Finalizado")
```

### Crear Excepciones Personalizadas

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
```

### Función `range()`

```python
range(10)        # 0 a 9
range(1, 11)     # 1 a 10
range(2, 11, 2)  # 2, 4, 6, 8, 10 (pares)
range(10, 0, -1) # 10 a 1 (descendente)
```

## 📖 Recursos Adicionales

- [Documentación: Definición de funciones](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions)
- [Documentación: Manejo de excepciones](https://docs.python.org/es/3/tutorial/errors.html)
- [PEP 8 - Guía de estilo para código Python](https://peps.python.org/pep-0008/)

## ➡️ Siguiente Paso

Una vez que domines estos conceptos, continúa con [Clase 4: Listas y Tuplas](../Clase%204/README.md) para aprender sobre estructuras de datos.

---

**💡 Tip**: Las funciones son fundamentales para organizar código. Practica creando funciones reutilizables y manejando errores adecuadamente.

