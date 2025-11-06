"""
Tests para Actividad 3: Operaciones Matemáticas Básicas

Estos tests verifican que tu programa realice suma, resta,
multiplicación y división con dos números decimales.
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_3.py')

from unittest.mock import patch
from io import StringIO

class TestActividad3(unittest.TestCase):
    """Tests para verificar la Actividad 3"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '5'])
    def test_operaciones_basicas(self, mock_input, mock_stdout):
        """Prueba con 10 y 5"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Verificar que contenga los resultados esperados
            self.assertIn('15', output, "Debe mostrar la suma (10 + 5 = 15)")
            self.assertIn('5', output, "Debe mostrar la resta (10 - 5 = 5)")
            self.assertIn('50', output, "Debe mostrar la multiplicación (10 * 5 = 50)")
            self.assertIn('2', output, "Debe mostrar la división (10 / 5 = 2)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['8.5', '2.5'])
    def test_operaciones_decimales(self, mock_input, mock_stdout):
        """Prueba con números decimales 8.5 y 2.5"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Verificar que contenga resultados
            self.assertIn('11', output, "Debe mostrar la suma (8.5 + 2.5 = 11)")
            self.assertIn('6', output, "Debe mostrar la resta (8.5 - 2.5 = 6)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('builtins.input', side_effect=['4', '2'])
    def test_solicita_dos_numeros(self, mock_input):
        """Verifica que se soliciten dos números"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            self.assertEqual(mock_input.call_count, 2, "Debe solicitar 2 números")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['6', '3'])
    def test_muestra_cuatro_operaciones(self, mock_input, mock_stdout):
        """Verifica que se muestren las 4 operaciones"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            lines = output.strip().split('\n')
            
            # Debe haber al menos 4 líneas (una para cada operación)
            self.assertGreaterEqual(len(lines), 4, "Debe mostrar 4 operaciones en líneas separadas")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 3: Operaciones Matemáticas Básicas")
    print("=" * 60)
    unittest.main(verbosity=2)


