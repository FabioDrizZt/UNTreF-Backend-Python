# 📚 Clase 2: Control de Flujo y Strings

Esta clase introduce el control de flujo en Python mediante condicionales, operadores lógicos y de comparación, además de profundizar en el manejo de strings.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Usar condicionales `if`, `elif` y `else`
- ✅ Aplicar operadores de comparación (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- ✅ Usar operadores lógicos (`and`, `or`, `not`)
- ✅ Trabajar con entrada de datos usando `input()`
- ✅ Manipular strings con métodos integrados
- ✅ Usar indexación y slicing en strings

## 📁 Contenido de la Clase

### [📝 Código en Clase](./Codigo%20en%20clase/README.md)

Ejemplos prácticos que cubren:

- **`if.py`**: Estructuras condicionales básicas y anidadas
- **`else.py`**: Uso de `else` y `elif` para múltiples condiciones
- **`op_comparacion.py`**: Operadores de comparación
- **`op_logicos.py`**: Operadores lógicos (`and`, `or`, `not`)
- **`input.py`**: Captura de entrada del usuario
- **`strings.py`**: Métodos y operaciones con strings
- **`functions.py`**: Introducción básica a funciones

### [💪 Ejercicios](./Ejercicios/README.md)

9 ejercicios prácticos que aplican los conceptos aprendidos:

1. Calificación de Estudiante
2. Costo de Internación
3. Fecha y Nombre del Mes
4. Institución de Educación
5. Número Positivo o Negativo
6. Ordenar Valores
7. Signo Zodiacal
8. Tienda con Descuento
9. Tipo de Triángulo

## 🔑 Conceptos Clave

### Condicionales

```python
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

### Operadores de Comparación

- `==`: Igual a
- `!=`: Diferente de
- `>`: Mayor que
- `<`: Menor que
- `>=`: Mayor o igual que
- `<=`: Menor o igual que

### Operadores Lógicos

```python
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")

if es_fin_de_semana or es_feriado:
    print("No hay clases")
```

### Entrada de Datos

```python
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
```

### Métodos de Strings

```python
texto = "  Hola Mundo  "
texto.strip()      # Elimina espacios al inicio y final
texto.upper()      # Convierte a mayúsculas
texto.lower()      # Convierte a minúsculas
texto.split()      # Divide en lista de palabras
```

### Indexación y Slicing

```python
texto = "Python"
texto[0]      # 'P' (primer carácter)
texto[-1]     # 'n' (último carácter)
texto[0:3]    # 'Pyt' (slicing)
texto[:3]     # 'Pyt' (desde el inicio)
texto[3:]     # 'hon' (hasta el final)
```

## 📖 Recursos Adicionales

- [Documentación: Operadores](https://docs.python.org/es/3/library/operator.html)
- [Documentación: Métodos de String](https://docs.python.org/es/3/library/stdtypes.html#string-methods)

## ➡️ Siguiente Paso

Una vez que domines estos conceptos, continúa con [Clase 3: Funciones y Manejo de Errores](../Clase%203/README.md) para aprender a crear funciones y manejar excepciones.

---

**💡 Tip**: Los condicionales son fundamentales en programación. Practica creando diferentes escenarios y condiciones.

