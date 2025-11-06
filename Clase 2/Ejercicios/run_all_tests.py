"""
Script para ejecutar todos los tests de Estructuras Condicionales
===================================================================

Este script ejecuta automáticamente todos los tests para los 9 ejercicios.
Los alumnos pueden usar este script para verificar todas sus soluciones de una vez.

Uso:
    python run_all_tests.py              # Ejecutar todos los tests
    python run_all_tests.py 1            # Ejecutar solo el ejercicio 1
    python run_all_tests.py 5            # Ejecutar solo el ejercicio 5
"""

import unittest
import sys
import os

# Mapeo de números a nombres de archivos
EJERCICIOS = {
    1: 'NumeroPositivoNegativo',
    2: 'InstitucionEducacion',
    3: 'OrdenarValores',
    4: 'TipoTriangulo',
    5: 'FechaNombreMes',
    6: 'SignoZodiacal',
    7: 'CostoInternacion',
    8: 'TiendaDescuento',
    9: 'CalificacionEstudiante'
}

def run_all_tests():
    """Ejecuta todos los tests de los ejercicios."""
    
    print("=" * 70)
    print("EJECUTANDO TODOS LOS TESTS DE ESTRUCTURAS CONDICIONALES")
    print("=" * 70)
    print()
    
    # Asegurar que estamos en el directorio correcto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Agregar las carpetas al path
    sys.path.insert(0, os.path.join(script_dir, 'ejercicios'))
    sys.path.insert(0, os.path.join(script_dir, 'tests'))
    
    # Descubrir todos los tests en la carpeta tests
    loader = unittest.TestLoader()
    start_dir = 'tests'
    pattern = 'test_*.py'
    
    suite = loader.discover(start_dir, pattern=pattern)
    
    # Ejecutar los tests con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Mostrar resumen
    print()
    print("=" * 70)
    print("RESUMEN DE RESULTADOS")
    print("=" * 70)
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Tests exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests fallidos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    print()
    
    if result.wasSuccessful():
        print("✅ ¡FELICITACIONES! Todos los tests pasaron correctamente.")
        print("   Has completado exitosamente todos los ejercicios de")
        print("   Estructuras Condicionales.")
    else:
        print("⚠️  Algunos tests no pasaron.")
        print("   Revisa los mensajes de error arriba para ver qué necesitas corregir.")
        print()
        if result.failures:
            print(f"   Ejercicios con tests fallidos: {len(result.failures)}")
        if result.errors:
            print(f"   Ejercicios con errores: {len(result.errors)}")
    
    print("=" * 70)
    print()
    
    # Retornar código de salida apropiado
    return 0 if result.wasSuccessful() else 1


def run_specific_test(exercise_number):
    """Ejecuta el test de un ejercicio específico."""
    
    if exercise_number not in EJERCICIOS:
        print(f"❌ Error: El número de ejercicio debe estar entre 1 y {len(EJERCICIOS)}")
        print("Ejercicios disponibles:")
        for num, nombre in EJERCICIOS.items():
            print(f"  {num}. {nombre}")
        return 1
    
    exercise_name = EJERCICIOS[exercise_number]
    test_file = f'test_{exercise_name}.py'
    test_path = os.path.join('tests', test_file)
    
    if not os.path.exists(test_path):
        print(f"❌ Error: No se encontró el archivo {test_file} en la carpeta tests/")
        return 1
    
    print("=" * 70)
    print(f"EJECUTANDO TESTS PARA EJERCICIO {exercise_number}: {exercise_name}")
    print("=" * 70)
    print()
    
    # Agregar las carpetas al path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(script_dir, 'ejercicios'))
    sys.path.insert(0, os.path.join(script_dir, 'tests'))
    
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern=test_file)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    if result.wasSuccessful():
        print(f"✅ ¡Bien hecho! El ejercicio {exercise_number} pasó todos los tests.")
    else:
        print(f"⚠️  El ejercicio {exercise_number} tiene tests que no pasaron.")
        print("   Revisa los mensajes de error arriba.")
    print()
    
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    # Si se proporciona un número de ejercicio, ejecutar solo ese test
    if len(sys.argv) > 1:
        try:
            exercise_num = int(sys.argv[1])
            sys.exit(run_specific_test(exercise_num))
        except ValueError:
            print("❌ Error: Debes proporcionar un número válido")
            print(f"Uso: python run_all_tests.py [1-{len(EJERCICIOS)}]")
            print("Ejemplo: python run_all_tests.py 1")
            sys.exit(1)
    else:
        # Ejecutar todos los tests
        sys.exit(run_all_tests())
