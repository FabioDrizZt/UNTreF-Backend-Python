# 📝 Código en Clase - Clase 2

Esta carpeta contiene los ejemplos prácticos y demostraciones del profesor durante la Clase 2. Estos archivos muestran cómo usar control de flujo, operadores y manipulación de strings en Python.

## 📄 Archivos Disponibles

### `if.py`
**Tema**: Estructuras condicionales básicas

**Conceptos cubiertos**:
- Estructura `if` básica
- Condiciones con operadores de comparación
- Múltiples condiciones con `elif`
- Estructura `else`
- Comparaciones encadenadas (`a > b > c`)

**Ejemplo clave**:
```python
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

---

### `else.py`
**Tema**: Uso avanzado de `else` y `elif`

**Conceptos cubiertos**:
- Estructura completa `if-elif-else`
- Múltiples condiciones
- Lógica de decisión compleja

**Ejemplo clave**:
```python
if a > b > c or a > c > b:
    print("El mayor es a")
elif b > c:
    print("El mayor es b")
else:
    print("El mayor es c")
```

---

### `op_comparacion.py`
**Tema**: Operadores de comparación

**Conceptos cubiertos**:
- `==`: Igual a
- `!=`: Diferente de
- `>`: Mayor que
- `<`: Menor que
- `>=`: Mayor o igual que
- `<=`: Menor o igual que
- Comparaciones con strings
- Comparaciones con números

**Ejemplo clave**:
```python
print(5 == 5)    # True
print(5 != 3)    # True
print(5 > 3)     # True
print(5 < 10)    # True
```

---

### `op_logicos.py`
**Tema**: Operadores lógicos

**Conceptos cubiertos**:
- `and`: Operador lógico Y (&& en otros lenguajes)
- `or`: Operador lógico O (|| en otros lenguajes)
- `not`: Operador lógico NO (! en otros lenguajes)
- Operadores bitwise (avanzado): `<<`, `>>`, `&`, `|`, `^`, `~`

**Ejemplo clave**:
```python
print(True and True)   # True
print(True or False)   # True
print(not True)        # False
```

---

### `input.py`
**Tema**: Entrada de datos del usuario

**Conceptos cubiertos**:
- Función `input()` para capturar texto
- Conversión de entrada a diferentes tipos
- Validación básica de entrada
- Mensajes promocionales

**Ejemplo clave**:
```python
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print(f"Hola {nombre}, tienes {edad} años")
```

---

### `strings.py`
**Tema**: Manipulación de strings

**Conceptos cubiertos**:
- Método `strip()`: Elimina espacios al inicio y final
- Método `upper()`: Convierte a mayúsculas
- Método `lower()`: Convierte a minúsculas
- Método `split()`: Divide string en lista
- Método `replace()`: Reemplaza texto
- Método `join()`: Une lista en string
- Indexación de strings: `texto[0]`, `texto[-1]`
- Slicing: `texto[inicio:fin]`

**Ejemplo clave**:
```python
texto = "  Hola Mundo  "
texto.strip()        # "Hola Mundo"
texto.upper()        # "  HOLA MUNDO  "
texto[0:4]           # "  Ho"
```

---

### `functions.py`
**Tema**: Introducción básica a funciones

**Conceptos cubiertos**:
- Definición de funciones con `def`
- Parámetros de función
- Retorno de valores con `return`
- Llamadas a funciones

**Nota**: Este tema se profundiza en la Clase 3.

---

## 🚀 Cómo Usar Estos Archivos

1. **Ejecuta cada archivo**:
   ```bash
   python if.py
   python else.py
   python op_comparacion.py
   python op_logicos.py
   python input.py
   python strings.py
   python functions.py
   ```

2. **Experimenta modificando**:
   - Cambia los valores en las condiciones
   - Prueba diferentes operadores
   - Modifica los strings y observa los resultados

3. **Combina conceptos**:
   - Usa `input()` con condicionales
   - Aplica métodos de string en condiciones
   - Crea estructuras más complejas

## 💡 Consejos de Estudio

- **Practica las condiciones**: Escribe tus propias condiciones con diferentes valores
- **Experimenta con strings**: Prueba todos los métodos mencionados
- **Combina conceptos**: Usa `input()` con condicionales para crear programas interactivos
- **Lee los comentarios**: Muchos archivos tienen comparaciones con JavaScript para facilitar el aprendizaje

## 🔗 Relación con los Ejercicios

Estos ejemplos te preparan para resolver los ejercicios prácticos en [`../Ejercicios/`](../Ejercicios/README.md), donde aplicarás estos conceptos en problemas reales.

---

**📚 Siguiente paso**: Practica con los [Ejercicios de la Clase 2](../Ejercicios/README.md) para consolidar estos conceptos.

