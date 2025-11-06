# 🔀 Estructuras Condicionales en Python

Bienvenido/a a los ejercicios de Estructuras Condicionales. En este directorio encontrarás 9 ejercicios diseñados para practicar `if`, `elif` y `else` en Python.

## 📝 Cómo Trabajar

### Paso 1: Completar el Ejercicio

Cada archivo contiene:
- El enunciado del ejercicio (en un docstring al inicio)
- Un espacio para que escribas tu código

**Tu tarea:** Escribe el código necesario para resolver cada ejercicio usando estructuras condicionales.

### Paso 2: Ejecutar tu Programa

```bash
# Desde la raíz de Estructuras Condicionales/
python ejercicios/NumeroPositivoNegativo.py

# O entrando a la carpeta
cd ejercicios
python NumeroPositivoNegativo.py
```

El programa te pedirá información y mostrará resultados.

### Paso 3: Verificar con Tests ✅

Una vez que tu programa funciona, verifica que esté correcto:

```bash
# Verificar un ejercicio específico
python test_NumeroPositivoNegativo.py

# O ejecutar todos los tests
python run_all_tests.py
```

Los tests te dirán automáticamente si tu solución es correcta.

---

## 📋 Ejercicios Disponibles

| # | Ejercicio | Archivo | Dificultad | Conceptos |
|---|-----------|---------|------------|-----------|
| 1 | Número Positivo o Negativo | `NumeroPositivoNegativo.py` | ⭐ Fácil | `if/else`, operador `%` |
| 2 | Institución de Educación | `InstitucionEducacion.py` | ⭐⭐ Media | `if/elif/else` anidados |
| 3 | Ordenar Valores | `OrdenarValores.py` | ⭐⭐ Media | comparaciones múltiples |
| 4 | Tipo de Triángulo | `TipoTriangulo.py` | ⭐⭐ Media | validaciones, comparaciones |
| 5 | Fecha con Nombre del Mes | `FechaNombreMes.py` | ⭐ Fácil | `if/elif` múltiple |
| 6 | Signo Zodiacal | `SignoZodiacal.py` | ⭐⭐⭐ Difícil | lógica compleja de fechas |
| 7 | Costo de Internación | `CostoInternacion.py` | ⭐⭐⭐ Difícil | múltiples condiciones, cálculos |
| 8 | Tienda de Descuento | `TiendaDescuento.py` | ⭐⭐ Media | `if/elif`, cálculos con % |
| 9 | Calificación de Estudiante | `CalificacionEstudiante.py` | ⭐ Fácil | rangos numéricos |

### Descripción Breve de Cada Ejercicio

**1. Número Positivo o Negativo**  
Determina si un número es positivo, negativo o cero, y si es par o impar.

**2. Institución de Educación**  
Determina el estado de un estudiante (Aprobado/Reprobado/Recuperación) según su nota y carrera.

**3. Ordenar Valores**  
Recibe tres números y los muestra ordenados de menor a mayor.

**4. Tipo de Triángulo**  
Determina si un triángulo es equilátero, isósceles o escaleno (verificando primero si es válido).

**5. Fecha con Nombre del Mes**  
Convierte una fecha numérica (15/3/2023) a formato con nombre del mes (15 de marzo de 2023).

**6. Signo Zodiacal**  
Determina el signo zodiacal según el día y mes de nacimiento.

**7. Costo de Internación**  
Calcula el costo de internación hospitalaria según el tipo de enfermedad, edad y días.

**8. Tienda de Descuento**  
Calcula el monto final según el color de bolita (cada color tiene un descuento diferente).

**9. Calificación de Estudiante**  
Asigna una letra (A, B, C, D, F) según la nota del examen, o indica si la nota es inválida.

---

## 🧪 Sistema de Validación Automática

### Cómo Usar los Tests

#### Opción 1: Verificar UN ejercicio

```bash
python test_NumeroPositivoNegativo.py
python test_InstitucionEducacion.py
# ... etc
```

#### Opción 2: Verificar TODOS los ejercicios

```bash
python run_all_tests.py
```

También puedes verificar solo un ejercicio específico por número:

```bash
python run_all_tests.py 1    # Solo ejercicio 1
python run_all_tests.py 5    # Solo ejercicio 5
```

### Interpretar los Resultados

✅ **OK** - ¡Perfecto! Tu código funciona correctamente.

```
Ran 5 tests in 0.002s
OK
```

❌ **FAIL** - Tu código tiene un problema. Lee el mensaje de error.

```
FAIL: test_numero_positivo_par
AssertionError: Debe identificar que 4 es positivo
```

⚠️ **ERROR** - Tu código tiene un error de sintaxis o ejecución.

```
ERROR: test_numero_positivo_par
NameError: name 'numero' is not defined
```

---

## 💡 Flujo de Trabajo Recomendado

1. **Lee el enunciado** completo en el archivo `.py`
2. **Piensa en la lógica** antes de escribir código
3. **Escribe tu código** usando `if`, `elif` y `else`
4. **Ejecuta tu programa** manualmente varias veces con diferentes datos
5. **Verifica con tests** para asegurar que funcione en todos los casos
6. **Corrige errores** si los tests fallan
7. **Continúa** con el siguiente ejercicio

---

## 📚 Conceptos Clave de Estructuras Condicionales

### if / elif / else

```python
if condicion1:
    # código si condicion1 es True
elif condicion2:
    # código si condicion2 es True
else:
    # código si ninguna condición es True
```

### Operadores de Comparación

- `==` : igual a
- `!=` : diferente de
- `>` : mayor que
- `<` : menor que
- `>=` : mayor o igual que
- `<=` : menor o igual que

### Operadores Lógicos

- `and` : ambas condiciones deben ser True
- `or` : al menos una condición debe ser True
- `not` : invierte el valor de verdad

### Ejemplos

```python
# Ejemplo simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Múltiples condiciones
nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")

# Condiciones complejas
edad = 20
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")
```

---

## 📁 Estructura del Proyecto

```
Estructuras Condicionales/
├── ejercicios/                    # 📝 Tus ejercicios aquí
│   ├── NumeroPositivoNegativo.py
│   ├── InstitucionEducacion.py
│   └── ...                        # (ejercicios 3-9)
├── tests/                         # ✅ Tests de validación
│   ├── test_NumeroPositivoNegativo.py
│   ├── test_InstitucionEducacion.py
│   └── ...                        # (tests 3-9)
├── run_all_tests.py               # Script ejecutor
└── README.md                      # Este archivo
```

---

## 💡 Consejos para Resolver los Ejercicios

1. **Lee bien el enunciado**: Presta atención a los rangos y casos especiales
2. **Dibuja un diagrama**: A veces ayuda dibujar el flujo de decisiones
3. **Prueba casos extremos**: Prueba con valores límite (0, números negativos, etc.)
4. **Usa comentarios**: Explica tu lógica con comentarios en el código
5. **Un paso a la vez**: Si un ejercicio es complejo, divídelo en partes
6. **Revisa los tests**: Los mensajes de error te dicen exactamente qué esperar

### Errores Comunes a Evitar

❌ **Mal:**
```python
if nota > 90:  # Falta el caso cuando nota == 90
    print("A")
```

✅ **Bien:**
```python
if nota >= 90:  # Incluye el 90
    print("A")
```

❌ **Mal:**
```python
if numero % 2 == 0:
    print("par")
# Falta el else para impar
```

✅ **Bien:**
```python
if numero % 2 == 0:
    print("par")
else:
    print("impar")
```

---

## ❓ Preguntas Frecuentes

**P: ¿Debo usar funciones o puedo escribir código directo?**  
R: Puedes escribir código directo con `input()` y `print()`. No es necesario crear funciones para estos ejercicios.

**P: ¿En qué orden debo hacer los ejercicios?**  
R: Se recomienda hacerlos en orden (1-9) ya que aumentan progresivamente en dificultad.

**P: Mi programa funciona pero los tests fallan. ¿Por qué?**  
R: Los tests verifican detalles específicos. Lee el mensaje de error - te dirá qué espera exactamente. Quizás falta un caso especial o el formato no es el correcto.

**P: ¿Puedo usar otras estructuras como loops?**  
R: Para estos ejercicios, concéntrate en usar solo estructuras condicionales (`if/elif/else`). Los loops se verán en otra sección.

**P: El ejercicio del signo zodiacal es muy difícil. ¿Hay algún consejo?**  
R: Divide el problema: primero verifica el mes, luego verifica el día. Recuerda que algunos signos abarcan dos meses.

---

## 🎯 Objetivos de Aprendizaje

Al completar estas actividades, habrás practicado:

- ✅ Uso de `if`, `elif` y `else`
- ✅ Operadores de comparación (`<`, `>`, `==`, etc.)
- ✅ Operadores lógicos (`and`, `or`, `not`)
- ✅ Condiciones anidadas
- ✅ Validación de datos
- ✅ Lógica condicional compleja
- ✅ Rangos numéricos
- ✅ Comparación de múltiples variables

---

## 🚀 ¡Comienza Ahora!

```bash
# 1. Abre ejercicios/NumeroPositivoNegativo.py y escribe tu código

# 2. Ejecuta tu programa
python ejercicios/NumeroPositivoNegativo.py

# 3. Verifica que esté correcto
python run_all_tests.py 1

# 4. ¡Continúa con el siguiente!
```

---

## 📞 ¿Necesitas Ayuda?

- **Documentación de Python:** https://docs.python.org/es/3/tutorial/controlflow.html
- **Consulta con tu profesor** si tienes dudas sobre la lógica
- **Lee los mensajes de error** de los tests - te guían hacia la solución

---

¡Buena suerte con tus ejercicios! 🎓

Recuerda: las estructuras condicionales son fundamentales en programación. Practica hasta que te sientas cómodo/a con ellas.

