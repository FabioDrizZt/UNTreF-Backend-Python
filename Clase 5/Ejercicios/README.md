# 💪 Ejercicios - Clase 5

Esta carpeta contiene los ejercicios prácticos para la Clase 5 sobre Bucles (`for` y `while`). Los ejercicios están diseñados para practicar estructuras repetitivas y manipulación de listas.

## 📋 Ejercicios Disponibles

### `01_list.py` - Manipulación de Listas
Ejercicios de manipulación de listas usando slicing y otros operadores.

1. **El mensaje secreto**: Extrae una sublista usando slicing
2. **Intercambio de posiciones**: Intercambia elementos de una lista
3. **El sándwich de listas**: Concatena varias listas
4. **Duplicando la lista**: Repite los elementos de una lista
5. **Extrayendo el centro**: Encuentra el elemento central de una lista
6. **Reversa parcial**: Invierte una parte de una lista usando slicing

**Conceptos practicados**: Slicing, índices, concatenación, repetición

---

### `02_range.py` - Uso de `range()`
Ejercicios para practicar el uso de `range()` en bucles `for`.

1. **Imprimir números del 1 al 10**: Usa `range()` para imprimir números
2. **Imprimir números impares**: Usa `range()` con un paso para imprimir impares
3. **Imprimir múltiplos de 5**: Usa `range()` para imprimir múltiplos de un número
4. **Imprimir en orden inverso**: Usa `range()` para contar hacia atrás
5. **Suma de números en un rango**: Suma los números en un rango grande
6. **Tabla de multiplicar**: Genera una tabla de multiplicar con `range()`

**Conceptos practicados**: `range()`, bucles `for`, pasos en rangos, rangos descendentes

---

### `03_for.py` - Bucles `for`
Ejercicios para practicar el uso del bucle `for` con iterables.

1. **Imprimir números pares**: Imprime los números pares del 2 al 20
2. **Calcular la media**: Calcula la media de una lista de números
3. **Buscar el máximo**: Encuentra el número máximo en una lista
4. **Filtrar cadenas por longitud**: Filtra una lista de palabras por su longitud
5. **Contar palabras que empiezan con una letra**: Cuenta palabras que empiezan por una letra dada

**Conceptos practicados**: Bucles `for`, iteración sobre listas, condiciones en bucles, acumuladores

---

### `04_while.py` - Bucles `while`
Ejercicios para practicar el uso del bucle `while`.

1. **Cuenta atrás**: Imprime los números del 10 al 1
2. **Suma de números pares**: Calcula la suma de los números pares entre 1 y 20
3. **Factorial de un número**: Calcula el factorial de un número introducido
4. **Validación de contraseña**: Pide una contraseña hasta que cumpla los requisitos de longitud
5. **Tabla de multiplicar**: Imprime la tabla de multiplicar de un número
6. **Números primos hasta N**: Imprime los números primos hasta un número N

**Conceptos practicados**: Bucles `while`, condiciones dinámicas, validación de entrada, algoritmos matemáticos

---

## 🚀 Cómo Trabajar con los Ejercicios

### Paso 1: Revisar el Código en Clase

Antes de comenzar, asegúrate de haber revisado los ejemplos en [`../Codigo en clase/`](../Codigo%20en%20clase/README.md).

### Paso 2: Leer el Enunciado

Cada archivo contiene:
- Un enunciado del problema como comentario al inicio de cada ejercicio
- Una función que debes completar
- Instrucciones específicas sobre qué debe hacer la función

### Paso 3: Escribir tu Solución

Abre cada archivo (`01_list.py`, `02_range.py`, etc.) y completa las funciones siguiendo las instrucciones.

**Ejemplo de estructura**:
```python
def ejercicio_1(lista):
    """
    Enunciado: Extrae una sublista usando slicing
    """
    # Tu código aquí
    return resultado
```

### Paso 4: Ejecutar los Tests

Para verificar tus soluciones, ejecuta los tests:

```bash
# Ejecutar todos los tests
python -m pytest -v

# Ejecutar tests de un archivo específico
pytest tests/test_01_list.py
pytest tests/test_02_range.py
pytest tests/test_03_for.py
pytest tests/test_04_while.py
```

### Paso 5: Interpretar los Resultados

- ✅ **PASSED**: Tu solución es correcta
- ❌ **FAILED**: Tu solución tiene errores. Lee los mensajes de error para entender qué está fallando

**Ejemplo de salida exitosa**:
```
============================= test session starts ==============================
collected 6 items

tests/test_01_list.py ...... [100%]

============================== 6 passed in 0.03s ===============================
```

## 💡 Consejos para Resolver los Ejercicios

1. **Lee cuidadosamente**: El enunciado contiene toda la información necesaria
2. **Planifica primero**: Piensa en la solución antes de escribir código
3. **Usa las herramientas adecuadas**:
   - `for` cuando sabes cuántas veces iterar o tienes un iterable
   - `while` cuando la condición de parada es dinámica
   - `range()` para generar secuencias numéricas
4. **No modifiques la estructura**: Solo completa las funciones, no cambies los nombres ni parámetros
5. **Ejecuta tests frecuentemente**: Verifica tu progreso paso a paso
6. **Consulta la documentación**: Si tienes dudas sobre métodos o funciones

## 🎯 Objetivos de Aprendizaje

Al completar estos ejercicios, habrás practicado:

- ✅ Manipulación avanzada de listas con slicing
- ✅ Uso de `range()` en diferentes contextos
- ✅ Iteración con bucles `for` sobre diferentes estructuras
- ✅ Control de flujo con bucles `while`
- ✅ Resolución de problemas algorítmicos
- ✅ Validación de entrada de datos
- ✅ Cálculos matemáticos (factorial, primos, promedios)

## 🔗 Recursos Relacionados

- [Código en Clase - Clase 5](../Codigo%20en%20clase/README.md)
- [Documentación: Bucles `for`](https://docs.python.org/es/3/tutorial/controlflow.html#for-statements)
- [Documentación: Bucles `while`](https://docs.python.org/es/3/tutorial/controlflow.html#while-statements)
- [Documentación: `range()`](https://docs.python.org/es/3/library/stdtypes.html#range)

---

**💡 Tip**: Empieza con los ejercicios más simples y avanza gradualmente. No tengas miedo de experimentar y probar diferentes enfoques.

**¡Buena suerte con los ejercicios! 🎓**
