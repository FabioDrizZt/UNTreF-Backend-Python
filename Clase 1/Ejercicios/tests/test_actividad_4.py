"""
Tests para Actividad 4: Manipulación de Texto

Estos tests verifican que tu programa muestre:
- Cantidad de caracteres
- Oración en mayúsculas
- Oración en minúsculas
- Primera palabra
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_4.py')

from unittest.mock import patch
from io import StringIO

class TestActividad4(unittest.TestCase):
    """Tests para verificar la Actividad 4"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Hola mundo')
    def test_manipulacion_texto_simple(self, mock_input, mock_stdout):
        """Prueba con 'Hola mundo'"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar el total de caracteres (10)
            self.assertIn('10', output, "Debe mostrar que 'Hola mundo' tiene 10 caracteres")
            
            # Debe mostrar en mayúsculas
            self.assertIn('HOLA MUNDO', output, "Debe mostrar la oración en mayúsculas")
            
            # Debe mostrar en minúsculas
            self.assertIn('hola mundo', output, "Debe mostrar la oración en minúsculas")
            
            # Debe mostrar la primera palabra
            self.assertIn('Hola', output, "Debe mostrar la primera palabra")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Python es genial')
    def test_manipulacion_texto_largo(self, mock_input, mock_stdout):
        """Prueba con 'Python es genial'"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Total de caracteres: 16
            self.assertIn('16', output, "Debe mostrar que tiene 16 caracteres")
            
            # Mayúsculas
            self.assertIn('PYTHON ES GENIAL', output, "Debe mostrar en mayúsculas")
            
            # Minúsculas
            self.assertIn('python es genial', output, "Debe mostrar en minúsculas")
            
            # Primera palabra
            output_lower = output.lower()
            self.assertTrue('python' in output_lower, "Debe mostrar 'Python' como primera palabra")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='Test')
    def test_una_palabra(self, mock_input, mock_stdout):
        """Prueba con una sola palabra 'Test'"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('4', output, "Debe mostrar que 'Test' tiene 4 caracteres")
            self.assertIn('TEST', output, "Debe mostrar en mayúsculas")
            self.assertIn('test', output, "Debe mostrar en minúsculas")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 4: Manipulación de Texto")
    print("=" * 60)
    unittest.main(verbosity=2)


