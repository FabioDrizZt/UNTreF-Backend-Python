# 📝 Código en Clase - Clase 4

Esta carpeta contiene los ejemplos prácticos y demostraciones del profesor durante la Clase 4. Los archivos están organizados numéricamente para seguir un orden lógico de aprendizaje sobre listas y tuplas.

## 📄 Archivos Disponibles (en orden de estudio)

### `1_creacion_acceso_listas.py`
**Tema**: Creación y acceso a listas

**Conceptos cubiertos**:
- Creación de listas homogéneas y heterogéneas
- Acceso a elementos por índice positivo (`lista[0]`)
- Acceso a elementos por índice negativo (`lista[-1]`)
- Slicing (rebanado) de listas: `lista[inicio:fin]`
- Función `len()` para obtener la longitud
- Manejo de errores con `IndexError`
- Listas vacías

**Ejemplo clave**:
```python
paises = ["Argentina", "Brasil", "Chile", "Uruguay"]
print(paises[0])      # "Argentina"
print(paises[-1])      # "Uruguay"
print(paises[1:3])     # ["Brasil", "Chile"]
print(len(paises))     # 4
```

---

### `2_agregar_elementos.py`
**Tema**: Agregar elementos a listas

**Conceptos cubiertos**:
- `append(elemento)`: Agrega al final de la lista
- `insert(indice, elemento)`: Inserta en una posición específica
- `extend(iterable)`: Extiende la lista con otra lista o iterable
- Diferencias entre `append` y `extend`
- Uso de `input()` para agregar elementos dinámicamente

**Ejemplo clave**:
```python
lista = [1, 2, 3]
lista.append(4)        # [1, 2, 3, 4]
lista.insert(1, 5)     # [1, 5, 2, 3, 4]
lista.extend([6, 7])   # [1, 5, 2, 3, 4, 6, 7]
```

---

### `3_quitar_elementos.py`
**Tema**: Eliminar elementos de listas

**Conceptos cubiertos**:
- `remove(valor)`: Elimina la primera ocurrencia del valor
- `pop()`: Elimina y retorna el último elemento
- `pop(indice)`: Elimina y retorna el elemento en el índice
- `del lista[indice]`: Elimina elemento por índice
- `clear()`: Vacía toda la lista
- Manejo de errores al eliminar elementos

**Ejemplo clave**:
```python
lista = [1, 2, 3, 4, 5]
lista.remove(3)        # Elimina el valor 3
ultimo = lista.pop()   # Elimina y retorna 5
del lista[0]           # Elimina el elemento en índice 0
```

---

### `4_otros_metodos.py`
**Tema**: Otros métodos útiles de listas

**Conceptos cubiertos**:
- `sort()`: Ordena la lista (modifica la lista original)
- `reverse()`: Invierte el orden de la lista
- `count(valor)`: Cuenta ocurrencias de un valor
- `index(valor)`: Encuentra el índice de un valor
- `copy()`: Crea una copia de la lista
- `sorted()`: Función que retorna una lista ordenada (no modifica la original)

**Ejemplo clave**:
```python
lista = [3, 1, 4, 1, 5]
lista.sort()           # [1, 1, 3, 4, 5]
lista.reverse()        # [5, 4, 3, 1, 1]
lista.count(1)         # 2
lista.index(4)         # 1
```

---

### `5_creacion_acceso_tuplas.py`
**Tema**: Creación y acceso a tuplas

**Conceptos cubiertos**:
- Creación de tuplas con paréntesis `()`
- Tuplas de un solo elemento (requiere coma)
- Acceso a elementos por índice (igual que listas)
- Slicing en tuplas
- Inmutabilidad de tuplas
- Tuplas vacías

**Ejemplo clave**:
```python
coordenadas = (10, 20)
punto = (5, 3, 2)
tupla_un_elemento = (42,)  # ¡Importante la coma!

print(coordenadas[0])  # 10
print(coordenadas[1:])  # (20,)
```

---

### `6_union_tuplas.py`
**Tema**: Operaciones con tuplas

**Conceptos cubiertos**:
- Concatenación de tuplas con `+`
- Repetición de tuplas con `*`
- Operaciones que no modifican la tupla original (son inmutables)
- Comparación de tuplas

**Ejemplo clave**:
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5)
union = tupla1 + tupla2     # (1, 2, 3, 4, 5)
repetida = tupla1 * 2       # (1, 2, 3, 1, 2, 3)
```

---

### `7_conversiones_tupla_lista.py`
**Tema**: Conversión entre listas y tuplas

**Conceptos cubiertos**:
- `tuple(lista)`: Convierte lista a tupla
- `list(tupla)`: Convierte tupla a lista
- Cuándo usar cada conversión
- Casos de uso prácticos

**Ejemplo clave**:
```python
lista = [1, 2, 3]
tupla = tuple(lista)   # (1, 2, 3)

tupla = (1, 2, 3)
lista = list(tupla)    # [1, 2, 3]
```

---

## 🚀 Cómo Usar Estos Archivos

1. **Sigue el orden numérico**: Los archivos están numerados para seguir una progresión lógica
   ```bash
   python 1_creacion_acceso_listas.py
   python 2_agregar_elementos.py
   python 3_quitar_elementos.py
   # ... y así sucesivamente
   ```

2. **Experimenta modificando**:
   - Crea tus propias listas y tuplas
   - Prueba diferentes operaciones
   - Intenta combinar métodos

3. **Practica los conceptos**:
   - Crea listas con diferentes tipos de datos
   - Prueba todos los métodos mostrados
   - Compara el comportamiento de listas vs tuplas

## 💡 Consejos de Estudio

- **Memoriza los métodos principales**: `append`, `insert`, `remove`, `pop` son los más usados
- **Entiende la diferencia**: Listas son mutables, tuplas son inmutables
- **Practica el slicing**: Es muy útil y se usa constantemente
- **Experimenta con índices negativos**: Te permiten acceder desde el final
- **Nota las diferencias**: `append` vs `extend`, `remove` vs `pop` vs `del`

## 🔗 Relación con los Ejercicios

Estos ejemplos te preparan para resolver los ejercicios prácticos en [`../Ejercicios/`](../Ejercicios/README.md), donde aplicarás estas operaciones en problemas reales.

---

**📚 Siguiente paso**: Una vez que domines estas operaciones, continúa con [Clase 5: Bucles](../Clase%205/README.md) para aprender a iterar sobre listas.

