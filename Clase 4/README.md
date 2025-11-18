# 📚 Clase 4: Listas y Tuplas

Esta clase introduce las estructuras de datos fundamentales en Python: listas y tuplas. Aprenderás a crear, acceder, modificar y trabajar con estas estructuras.

## 🎯 Objetivos de Aprendizaje

Al completar esta clase, serás capaz de:

- ✅ Crear y acceder a listas y tuplas
- ✅ Usar índices positivos y negativos
- ✅ Realizar slicing (rebanado) de listas
- ✅ Agregar elementos a listas (`append`, `insert`, `extend`)
- ✅ Eliminar elementos de listas (`remove`, `pop`, `del`)
- ✅ Usar métodos útiles de listas (`sort`, `reverse`, `count`, `index`)
- ✅ Crear y trabajar con tuplas
- ✅ Convertir entre listas y tuplas
- ✅ Entender las diferencias entre listas y tuplas

## 📁 Contenido de la Clase

### [📝 Código en Clase](./Codigo%20en%20clase/README.md)

Ejemplos prácticos organizados en archivos numerados:

1. **`1_creacion_acceso_listas.py`**: Creación y acceso a listas, índices, slicing
2. **`2_agregar_elementos.py`**: Agregar elementos (`append`, `insert`, `extend`)
3. **`3_quitar_elementos.py`**: Eliminar elementos (`remove`, `pop`, `del`)
4. **`4_otros_metodos.py`**: Otros métodos útiles de listas
5. **`5_creacion_acceso_tuplas.py`**: Creación y acceso a tuplas
6. **`6_union_tuplas.py`**: Operaciones con tuplas
7. **`7_conversiones_tupla_lista.py`**: Conversión entre listas y tuplas

### [💪 Ejercicios](./Ejercicios/README.md)

*Los ejercicios de esta clase están en desarrollo.*

## 🔑 Conceptos Clave

### Creación de Listas

```python
# Lista homogénea
paises = ["Argentina", "Brasil", "Chile", "Uruguay"]

# Lista heterogénea
datos = [23, "Hola", 3.14, True, [1, 2, 3]]
```

### Acceso a Elementos

```python
paises = ["Argentina", "Brasil", "Chile", "Uruguay"]
# Índices:     0           1        2         3
# Negativos:  -4          -3       -2        -1

paises[0]    # "Argentina" (primer elemento)
paises[-1]   # "Uruguay" (último elemento)
paises[1:3]  # ["Brasil", "Chile"] (slicing)
```

### Agregar Elementos

```python
lista = [1, 2, 3]
lista.append(4)        # [1, 2, 3, 4]
lista.insert(1, 5)     # [1, 5, 2, 3, 4]
lista.extend([6, 7])   # [1, 5, 2, 3, 4, 6, 7]
```

### Eliminar Elementos

```python
lista = [1, 2, 3, 4, 5]
lista.remove(3)        # Elimina el valor 3
lista.pop()            # Elimina y retorna el último elemento
lista.pop(0)           # Elimina y retorna el elemento en índice 0
del lista[1]          # Elimina el elemento en índice 1
```

### Tuplas

```python
# Las tuplas son inmutables (no se pueden modificar)
coordenadas = (10, 20)
punto = (5, 3, 2)

# Acceso similar a listas
coordenadas[0]  # 10
coordenadas[1]  # 20
```

### Conversión entre Listas y Tuplas

```python
lista = [1, 2, 3]
tupla = tuple(lista)   # (1, 2, 3)

tupla = (1, 2, 3)
lista = list(tupla)    # [1, 2, 3]
```

## 📊 Diferencias: Listas vs Tuplas

| Característica | Lista | Tupla |
|---------------|-------|-------|
| Mutabilidad | ✅ Mutable | ❌ Inmutable |
| Sintaxis | `[1, 2, 3]` | `(1, 2, 3)` |
| Uso | Datos que cambian | Datos fijos |
| Rendimiento | Más lento | Más rápido |
| Memoria | Más espacio | Menos espacio |

## 📖 Recursos Adicionales

- [Documentación: Tipos de secuencia](https://docs.python.org/es/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [Documentación: Métodos de lista](https://docs.python.org/es/3/tutorial/datastructures.html#more-on-lists)

## ➡️ Siguiente Paso

Una vez que domines estos conceptos, continúa con [Clase 5: Bucles](../Clase%205/README.md) para aprender a iterar sobre listas y otras estructuras.

---

**💡 Tip**: Las listas son una de las estructuras de datos más usadas en Python. Practica manipulándolas hasta que te sientas cómodo.

