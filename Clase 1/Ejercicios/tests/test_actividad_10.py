"""
Tests para Actividad 10: Limpieza de Pantalla con el Módulo os

Estos tests verifican que tu programa:
- Importe el módulo os
- Limpie la pantalla
- Salude al usuario
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_10.py')

from unittest.mock import patch, MagicMock
from io import StringIO

class TestActividad10(unittest.TestCase):
    """Tests para verificar la Actividad 10"""
    
    def test_importa_modulo_os(self):
        """Verifica que se importe el módulo os"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            
            self.assertIn('import os', code, "Debe importar el módulo os")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('os.system')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Juan')
    def test_limpia_pantalla_y_saluda(self, mock_input, mock_stdout, mock_os_system):
        """Verifica que limpie la pantalla y salude"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            # Verificar que se llamó a os.system (para limpiar)
            self.assertTrue(mock_os_system.called,
                          "Debe llamar a os.system() para limpiar la pantalla")
            
            # Verificar que el comando de limpieza sea correcto
            llamadas = [str(call) for call in mock_os_system.call_args_list]
            comando_limpieza = any('cls' in str(c) or 'clear' in str(c) for c in llamadas)
            self.assertTrue(comando_limpieza,
                          "Debe usar 'cls' (Windows) o 'clear' (Linux/Mac) para limpiar")
            
            # Verificar que contenga el saludo
            output = mock_stdout.getvalue()
            self.assertIn('Juan', output, "Debe saludar al usuario con su nombre")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('os.system')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Maria')
    def test_saludo_con_nombre(self, mock_input, mock_stdout, mock_os_system):
        """Verifica que el saludo incluya el nombre ingresado"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            output = mock_stdout.getvalue()
            self.assertIn('Maria', output,
                        "El saludo debe incluir el nombre ingresado por el usuario")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('os.system')
    @patch('builtins.input', return_value='Pedro')
    def test_solicita_nombre(self, mock_input, mock_os_system):
        """Verifica que se solicite el nombre del usuario"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            self.assertEqual(mock_input.call_count, 1,
                           "Debe solicitar el nombre del usuario")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('os.system')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Carlos')
    def test_limpia_antes_de_solicitar(self, mock_input, mock_stdout, mock_os_system):
        """Verifica que limpie la pantalla (idealmente antes de solicitar el nombre)"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            # Simplemente verificar que se haya limpiado
            self.assertTrue(mock_os_system.called,
                          "Debe limpiar la terminal usando os.system()")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 10: Limpieza de Pantalla con Módulo os")
    print("=" * 60)
    unittest.main(verbosity=2)


