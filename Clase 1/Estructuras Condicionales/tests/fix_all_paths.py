#!/usr/bin/env python
"""Script para actualizar las rutas en todos los tests"""

import os
import glob
import re

# Mapeo de nombres de archivos
EJERCICIOS = {
    'NumeroPositivoNegativo': 'NumeroPositivoNegativo.py',
    'InstitucionEducacion': 'InstitucionEducacion.py',
    'OrdenarValores': 'OrdenarValores.py',
    'TipoTriangulo': 'TipoTriangulo.py',
    'FechaNombreMes': 'FechaNombreMes.py',
    'SignoZodiacal': 'SignoZodiacal.py',
    'CostoInternacion': 'CostoInternacion.py',
    'TiendaDescuento': 'TiendaDescuento.py',
    'CalificacionEstudiante': 'CalificacionEstudiante.py'
}

def fix_test_file(filename):
    """Actualiza un archivo de test con la ruta correcta"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer el nombre del ejercicio
    for nombre_ejercicio, archivo_ejercicio in EJERCICIOS.items():
        if f'test_{nombre_ejercicio}.py' == os.path.basename(filename):
            break
    else:
        print(f'✗ No se pudo identificar el ejercicio en {filename}')
        return False
    
    # Verificar si ya tiene la función helper
    if 'def get_ejercicio_path' in content:
        print(f'✓ {filename} ya estaba actualizado')
        return False
    
    # Agregar la función helper después de los imports
    import_section = re.search(r'(import .*?\n)+', content)
    if not import_section:
        print(f'✗ No se encontraron imports en {filename}')
        return False
    
    import_end = import_section.end()
    
    helper_function = f'''
def get_ejercicio_path():
    """Obtiene la ruta al archivo de ejercicio"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ejercicios_dir = os.path.join(script_dir, '..', 'ejercicios')
    return os.path.join(ejercicios_dir, '{archivo_ejercicio}')

'''
    
    # Insertar la función helper
    new_content = content[:import_end] + helper_function + content[import_end:]
    
    # Reemplazar las rutas relativas
    old_pattern = f"'../ejercicios/{archivo_ejercicio}'"
    new_pattern = 'get_ejercicio_path()'
    new_content = new_content.replace(old_pattern, new_pattern)
    
    # Guardar
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'✓ {filename} actualizado')
    return True

def main():
    """Procesar todos los archivos de test"""
    test_files = sorted(glob.glob('test_*.py'))
    
    if not test_files:
        print('No se encontraron archivos de test')
        return
    
    print(f'Encontrados {len(test_files)} archivos de test')
    print('Actualizando...\n')
    
    updated = 0
    for test_file in test_files:
        if fix_test_file(test_file):
            updated += 1
    
    print(f'\n¡Listo! {updated} archivos actualizados')

if __name__ == '__main__':
    main()

