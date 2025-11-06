#!/usr/bin/env python
"""Script para actualizar las rutas en todos los tests"""

import os
import glob
import re

def fix_test_file(filename):
    """Actualiza un archivo de test con la ruta correcta"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer el número de actividad
    match = re.search(r'test_actividad_(\d+)\.py', filename)
    if not match:
        return False
    
    actividad_num = match.group(1)
    
    # Verificar si ya tiene la función helper
    if 'def get_actividad_path' in content:
        print(f'✓ {filename} ya estaba actualizado')
        return False
    
    # Agregar la función helper después de los imports
    import_section = re.search(r'(import .*?\n)+', content)
    if not import_section:
        print(f'✗ No se encontraron imports en {filename}')
        return False
    
    import_end = import_section.end()
    
    helper_function = f'''
def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_{actividad_num}.py')

'''
    
    # Insertar la función helper
    new_content = content[:import_end] + helper_function + content[import_end:]
    
    # Reemplazar las rutas relativas
    old_pattern = f"'../actividades/actividad_{actividad_num}.py'"
    new_pattern = 'get_actividad_path()'
    new_content = new_content.replace(old_pattern, new_pattern)
    
    # Guardar
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'✓ {filename} actualizado')
    return True

def main():
    """Procesar todos los archivos de test"""
    test_files = sorted(glob.glob('test_actividad_*.py'))
    
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

