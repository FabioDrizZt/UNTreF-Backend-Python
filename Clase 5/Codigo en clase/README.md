# 📝 Código en Clase - Clase 5

Esta carpeta contiene los ejemplos prácticos y demostraciones del profesor durante la Clase 5. Estos archivos muestran cómo usar bucles `for` y `while` en Python, así como técnicas avanzadas de iteración.

## 📄 Archivos Disponibles

### `for.py`
**Tema**: Bucles `for` y técnicas de iteración

**Conceptos cubiertos**:
- Bucle `for` básico sobre listas y tuplas
- Bucle `for` con `range()`:
  - `range(stop)`: De 0 a stop-1
  - `range(start, stop)`: De start a stop-1
  - `range(start, stop, step)`: Con incremento step
  - Rangos descendentes (step negativo)
- Función `enumerate()`: Obtener índice y valor simultáneamente
- Función `zip()`: Iterar sobre múltiples listas en paralelo
- Control de flujo en bucles:
  - `break`: Salir del bucle completamente
  - `continue`: Saltar a la siguiente iteración
  - `else`: Ejecutar código si no hubo `break`
- List Comprehension (comprensión de listas):
  - Sintaxis básica: `[expresión for elemento in iterable]`
  - Con condición: `[expresión for elemento in iterable if condición]`
  - Con condición ternaria: `[valor1 if condición else valor2 for elemento in iterable]`
- Uso de `pass`: Placeholder para código futuro

**Ejemplo clave**:
```python
# Bucle básico
for fruta in frutas:
    print(fruta)

# Con enumerate
for i, fruta in enumerate(frutas, start=1):
    print(f"Posición {i}: {fruta}")

# Con zip
for producto, precio, stock in zip(productos, precios, stocks):
    print(f"{producto}: ${precio}, Stock: {stock}")

# List comprehension
cuadrados = [i**2 for i in range(10)]
pares = [i for i in range(10) if i % 2 == 0]
```

---

### `while.py`
**Tema**: Bucles `while` y repetición condicional

**Conceptos cubiertos**:
- Bucle `while` básico
- Control de contador manual
- Bucles con condiciones complejas
- Iterar sobre listas con `while`
- Comportamiento de pila: `pop()` sin índice
- Comportamiento de cola: `pop(0)`
- Emulación de `do-while` (bucle que se ejecuta al menos una vez)
- Bucles infinitos controlados con `break`
- Uso de `continue` en bucles `while`
- `else` en bucles `while`
- Ejemplo práctico: Juego de adivinación de números
- Uso de `random.randint()` para generar números aleatorios

**Ejemplo clave**:
```python
# Bucle básico
i = 0
while i < 10:
    print(i)
    i += 1

# Comportamiento de pila
while frutas:
    print(frutas.pop())

# Emulación de do-while
while True:
    print("Hola")
    if input("¿Continuar? ") == "No":
        break

# Juego de adivinación
numero_secreto = random.randint(1, 100)
while nro_intentos < 5:
    numero_ingresado = int(input("Dime el número: "))
    if numero_ingresado == numero_secreto:
        print("¡Has ganado!")
        break
```

---

## 🚀 Cómo Usar Estos Archivos

1. **Ejecuta cada archivo**:
   ```bash
   python for.py
   python while.py
   ```

2. **Experimenta modificando**:
   - Cambia los rangos y condiciones
   - Prueba diferentes estructuras de datos
   - Modifica las condiciones de `break` y `continue`
   - Crea tus propias list comprehensions

3. **Combina conceptos**:
   - Usa `enumerate()` con condiciones
   - Combina `zip()` con list comprehension
   - Crea bucles `while` que usen `for` internamente

## 💡 Consejos de Estudio

- **Memoriza la sintaxis**: `for elemento in iterable:` es fundamental
- **Practica `range()`**: Es muy usado y tiene múltiples formas
- **Entiende `break` vs `continue`**: 
  - `break`: Sale completamente del bucle
  - `continue`: Salta a la siguiente iteración
- **Aprende list comprehension**: Es una forma elegante y eficiente de crear listas
- **Cuándo usar `for` vs `while`**:
  - `for`: Cuando sabes cuántas veces iterar o tienes un iterable
  - `while`: Cuando la condición de parada es dinámica o desconocida
- **Cuidado con bucles infinitos**: Siempre asegúrate de que `while` tenga una condición de salida

## 🔗 Relación con los Ejercicios

Estos ejemplos te preparan para resolver los ejercicios prácticos en [`../Ejercicios/`](../Ejercicios/README.md), donde aplicarás bucles en problemas reales.

---

**📚 Siguiente paso**: Practica con los [Ejercicios de la Clase 5](../Ejercicios/README.md) para consolidar estos conceptos.

