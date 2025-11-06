"""
Tests para Actividad 1: Mensaje de Bienvenida

Estos tests verifican que tu programa funcione correctamente.
Tu código debe ejecutarse sin errores cuando se le proporcione input.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_1.py')

class TestActividad1(unittest.TestCase):
    """Tests para verificar la Actividad 1"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Juan')
    def test_saludo_nombre_simple(self, mock_input, mock_stdout):
        """Prueba con el nombre 'Juan'"""
        # Ejecutar el código del alumno
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Verificar que el output contenga el nombre
            self.assertIn('Juan', output, "El saludo debe incluir el nombre ingresado")
            # Verificar que haya algún saludo
            self.assertTrue(len(output) > 0, "Debe haber alguna salida")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='María José')
    def test_saludo_nombre_compuesto(self, mock_input, mock_stdout):
        """Prueba con nombre compuesto 'María José'"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('María José', output, "El saludo debe incluir el nombre completo")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Ana')
    def test_saludo_contiene_texto(self, mock_input, mock_stdout):
        """Verifica que haya un saludo personalizado"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe contener el nombre
            self.assertIn('Ana', output, "El saludo debe incluir el nombre")
            # Debe tener más que solo el nombre (debe haber un saludo)
            self.assertGreater(len(output.strip()), 3, "Debe haber un mensaje de saludo, no solo el nombre")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 1: Mensaje de Bienvenida")
    print("=" * 60)
    unittest.main(verbosity=2)


