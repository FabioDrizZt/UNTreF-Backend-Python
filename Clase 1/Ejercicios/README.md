# 🐍 Actividades de Fundamentos de Python

Bienvenido/a a las actividades prácticas de Python. En este directorio encontrarás 10 ejercicios diseñados para practicar los fundamentos del lenguaje.

## 📝 Cómo Trabajar

### Paso 1: Completar el Ejercicio

Cada archivo `actividad_X.py` contiene:
- El enunciado del ejercicio (como comentario)
- Un espacio para que escribas tu código

**Tu tarea:** Escribe el código necesario para resolver cada ejercicio.

### Paso 2: Ejecutar tu Programa

```bash
# Desde la raíz de Ejercicios/
python actividades/actividad_1.py

# O entrando a la carpeta
cd actividades
python actividad_1.py
```

El programa te pedirá información y mostrará resultados.

### Paso 3: Verificar con Tests ✅

Una vez que tu programa funciona, verifica que esté correcto:

```bash
# Verificar una actividad específica
python run_all_tests.py 1

# O ejecutar todos los tests
python run_all_tests.py
```

Los tests te dirán automáticamente si tu solución es correcta. ¡Es como tener un profesor automático!

---

## 📋 Actividades Disponibles

| # | Actividad | Archivo | Conceptos Clave |
|---|-----------|---------|-----------------|
| 1 | Mensaje de Bienvenida | `actividad_1.py` | `input()`, `print()`, strings |
| 2 | Información Personal | `actividad_2.py` | múltiples `input()`, formateo |
| 3 | Operaciones Matemáticas | `actividad_3.py` | `float()`, operadores |
| 4 | Manipulación de Texto | `actividad_4.py` | `len()`, `.upper()`, `.lower()`, `.split()` |
| 5 | Año de Nacimiento | `actividad_5.py` | constantes, aritmética |
| 6 | Generador de Apodos | `actividad_6.py` | slicing `[:3]`, `.upper()` |
| 7 | Calculadora de Propinas | `actividad_7.py` | porcentajes, formato decimales |
| 8 | Módulo math | `actividad_8.py` | `import math`, `math.sqrt()`, `math.pi` |
| 9 | Tarjetas de Presentación | `actividad_9.py` | strings multilínea, saltos de línea |
| 10 | Limpieza de Pantalla | `actividad_10.py` | `import os`, `os.system()` |

---

## 🧪 Sistema de Validación Automática

### ¿Qué son los Tests?

Los tests son programas que **verifican automáticamente** si tu código funciona correctamente. 

**NO necesitas entender cómo funcionan los tests** - solo ejecutalos para verificar tu solución.

### Cómo Usar los Tests

#### Opción 1: Verificar UNA actividad

```bash
# Windows (Git Bash)
python -m unittest test_actividad_1.py -v

# También funciona:
python test_actividad_1.py
```

Verás algo como:

```
test_saludo_nombre_simple ... ok
test_saludo_nombre_compuesto ... ok
test_saludo_contiene_texto ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK ✅
```

#### Opción 2: Verificar TODAS las actividades

```bash
python run_all_tests.py
```

Este comando ejecutará los tests de las 10 actividades y te mostrará un resumen completo.

También puedes verificar solo una actividad específica:

```bash
python run_all_tests.py 1    # Solo actividad 1
python run_all_tests.py 5    # Solo actividad 5
```

### Interpretar los Resultados

✅ **OK** - ¡Perfecto! Tu código funciona correctamente.

```
Ran 3 tests in 0.001s
OK
```

❌ **FAIL** - Tu código tiene un problema. Lee el mensaje de error para ver qué falta o está mal.

```
FAIL: test_saludo_nombre_simple
AssertionError: 'Juan' not found in output
El saludo debe incluir el nombre ingresado
```

⚠️ **ERROR** - Tu código tiene un error de sintaxis o ejecución.

```
ERROR: test_saludo_nombre_simple
NameError: name 'nombre' is not defined
```

### Consejos para Pasar los Tests

1. **Lee bien el enunciado**: Los tests verifican que hagas exactamente lo que pide el ejercicio
2. **Ejecuta tu programa primero**: Asegúrate de que funcione manualmente antes de hacer tests
3. **Lee los mensajes de error**: Los tests te dicen exactamente qué falta
4. **Un paso a la vez**: Si un test falla, arréglalo antes de continuar

---

## 📁 Estructura del Proyecto

```
Ejercicios/
├── actividad_1.py           # Ejercicio 1 (tú lo completas)
├── test_actividad_1.py      # Tests para verificar ejercicio 1
├── actividad_2.py           # Ejercicio 2 (tú lo completas)
├── test_actividad_2.py      # Tests para verificar ejercicio 2
├── ...                      # Ejercicios 3-10 con sus tests
├── run_all_tests.py         # Script para ejecutar todos los tests
└── README.md                # Este archivo
```

---

## 💡 Flujo de Trabajo Recomendado

1. **Lee el enunciado** en el archivo `actividad_X.py`
2. **Escribe tu código** en ese mismo archivo
3. **Ejecuta tu programa** para probarlo manualmente
   ```bash
   python actividades/actividad_1.py
   ```
4. **Si funciona bien**, verifica con los tests:
   ```bash
   python run_all_tests.py 1
   ```
5. **Si los tests fallan**, lee el mensaje de error y corrige
6. **Repite** hasta que todos los tests pasen ✅
7. **Continúa** con la siguiente actividad

---

## ❓ Preguntas Frecuentes

**P: ¿Debo modificar los archivos de tests?**  
R: No. Solo debes modificar los archivos en la carpeta `actividades/`. Los tests en la carpeta `tests/` ya están listos para usarse.

**P: ¿Es obligatorio pasar los tests?**  
R: Depende de tu profesor. Los tests son una herramienta para verificar que tu código es correcto. Si tu programa funciona bien manualmente y pasa los tests, ¡estás seguro de que está correcto!

**P: Mi programa funciona pero los tests fallan. ¿Por qué?**  
R: Los tests verifican detalles específicos. Lee el mensaje de error del test - te dirá exactamente qué espera y qué recibió. Quizás olvidaste mostrar algo o el formato no es el esperado.

**P: ¿Cómo sé qué debe hacer mi programa exactamente?**  
R: Lee el enunciado en el archivo de la actividad. Los tests verifican que hagas lo que pide el enunciado.

**P: ¿Puedo ver el código de los tests?**  
R: Sí, pero no es necesario. Los archivos `test_actividad_X.py` contienen el código de los tests, pero están hechos para ser ejecutados, no para ser modificados.

**P: Los tests mencionan "mock" y cosas raras. ¿Qué es eso?**  
R: No te preocupes por eso. Son técnicas avanzadas de testing. Solo ejecuta los tests y lee los mensajes de error, eso es todo lo que necesitas.

---

## 🎯 Objetivos de Aprendizaje

Al completar estas actividades, habrás practicado:

- ✅ Entrada y salida de datos (`input()`, `print()`)
- ✅ Tipos de datos (strings, números)
- ✅ Operaciones matemáticas y con texto
- ✅ Uso de módulos (`math`, `os`)
- ✅ Formateo de salida
- ✅ Validación de código con tests

---

## 🚀 ¡Comienza Ahora!

```bash
# 1. Abre actividades/actividad_1.py y escribe tu código

# 2. Ejecuta tu programa
python actividades/actividad_1.py

# 3. Verifica que esté correcto
python run_all_tests.py 1

# 4. ¡Continúa con la siguiente!
```

---

## 📞 ¿Necesitas Ayuda?

- **Documentación de Python:** https://docs.python.org/es/3/
- **Consulta con tu profesor** si tienes dudas sobre los ejercicios
- **Lee los mensajes de error** - generalmente te dicen exactamente qué está mal

---

¡Buena suerte con tus ejercicios! 🎓

Recuerda: la programación se aprende haciendo. No te preocupes si cometes errores, ¡es parte del aprendizaje!
