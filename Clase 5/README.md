# 📚 Clase 5: Bucles

Esta clase introduce los bucles en Python: `for` y `while`. Aprenderás a iterar sobre estructuras de datos, controlar el flujo de los bucles, y usar técnicas avanzadas como list comprehension.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Usar bucles `for` para iterar sobre listas, tuplas y strings
- ✅ Usar la función `range()` en bucles
- ✅ Usar `enumerate()` para obtener índice y valor
- ✅ Usar `zip()` para iterar sobre múltiples listas
- ✅ Usar bucles `while` para repetición condicional
- ✅ Controlar bucles con `break` y `continue`
- ✅ Usar `else` en bucles
- ✅ Crear list comprehension (comprensión de listas)
- ✅ Entender cuándo usar `for` vs `while`

## 📁 Contenido de la Clase

### [📝 Código en Clase](./Codigo%20en%20clase/README.md)

Ejemplos prácticos que cubren:

- **`for.py`**: Bucles `for`, `range()`, `enumerate()`, `zip()`, `break`, `continue`, list comprehension
- **`while.py`**: Bucles `while`, control de flujo, emulación de `do-while`

### [💪 Ejercicios](./Ejercicios/README.md)

4 ejercicios prácticos que aplican los conceptos aprendidos:

1. Trabajo con Listas
2. Uso de `range()`
3. Bucles `for`
4. Bucles `while`

## 🔑 Conceptos Clave

### Bucle `for` Básico

```python
frutas = ["manzana", "pera", "plátano"]
for fruta in frutas:
    print(fruta)
```

### Bucle `for` con `range()`

```python
for i in range(10):        # 0 a 9
    print(i)

for i in range(1, 11):     # 1 a 10
    print(i)

for i in range(2, 11, 2):  # 2, 4, 6, 8, 10 (pares)
    print(i)
```

### `enumerate()` - Índice y Valor

```python
frutas = ["manzana", "pera", "plátano"]
for i, fruta in enumerate(frutas, start=1):
    print(f"Posición {i}: {fruta}")
```

### `zip()` - Múltiples Listas

```python
productos = ["Laptop", "Mouse", "Teclado"]
precios = [1000, 25, 75]

for producto, precio in zip(productos, precios):
    print(f"{producto}: ${precio}")
```

### Bucle `while`

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### Control de Flujo: `break` y `continue`

```python
for n in numeros:
    if n == 0:
        break      # Sale del bucle completamente
    if n < 0:
        continue   # Salta a la siguiente iteración
    print(n)
```

### `else` en Bucles

```python
for n in numeros:
    if n == 0:
        break
else:
    # Se ejecuta solo si NO hubo break
    print("No se encontró un 0")
```

### List Comprehension

```python
# Forma tradicional
cuadrados = []
for i in range(10):
    cuadrados.append(i**2)

# List comprehension
cuadrados = [i**2 for i in range(10)]

# Con condición
pares = [i for i in range(10) if i % 2 == 0]
```

## 📊 Comparación: `for` vs `while`

| Característica | `for` | `while` |
|---------------|-------|---------|
| Uso | Iterar sobre secuencias conocidas | Repetir mientras condición sea verdadera |
| Control | Automático (itera sobre elementos) | Manual (debes incrementar contador) |
| Cuándo usar | Listas, rangos, iterables | Condiciones dinámicas, bucles infinitos |

## 📖 Recursos Adicionales

- [Documentación: Más sobre bucles](https://docs.python.org/es/3/tutorial/controlflow.html#for-statements)
- [Documentación: List Comprehension](https://docs.python.org/es/3/tutorial/datastructures.html#list-comprehensions)

## ➡️ Próximos Temas

Una vez que domines los bucles, estarás listo para temas más avanzados como:
- Diccionarios
- Sets
- Programación orientada a objetos
- Módulos y paquetes

---

**💡 Tip**: Los bucles son fundamentales en programación. Practica creando diferentes tipos de bucles y experimenta con `break`, `continue` y `else`.

