"""
Tests para Actividad 8: Explorando el Módulo math

Estos tests verifican que tu programa use el módulo math para:
- Calcular la raíz cuadrada
- Multiplicar por pi
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_8.py')

from unittest.mock import patch
from io import StringIO
import math

class TestActividad8(unittest.TestCase):
    """Tests para verificar la Actividad 8"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['16', '2'])
    def test_raiz_y_pi(self, mock_input, mock_stdout):
        """Prueba con raíz de 16 y 2*pi"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Raíz cuadrada de 16 = 4
            self.assertIn('4', output, "Debe mostrar que la raíz cuadrada de 16 es 4")
            
            # 2 * pi ≈ 6.28
            tiene_pi = '6.28' in output or '6,28' in output or '6.2' in output
            self.assertTrue(tiene_pi, "Debe mostrar el resultado de 2 * pi (aprox 6.28)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['9', '1'])
    def test_raiz_9_y_1pi(self, mock_input, mock_stdout):
        """Prueba con raíz de 9 y 1*pi"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Raíz cuadrada de 9 = 3
            self.assertIn('3', output, "Debe mostrar que la raíz cuadrada de 9 es 3")
            
            # 1 * pi ≈ 3.14
            tiene_pi = '3.14' in output or '3,14' in output
            self.assertTrue(tiene_pi, "Debe mostrar el valor de pi (aprox 3.14)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['25', '3'])
    def test_raiz_25_y_3pi(self, mock_input, mock_stdout):
        """Prueba con raíz de 25 y 3*pi"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Raíz cuadrada de 25 = 5
            self.assertIn('5', output, "Debe mostrar que la raíz cuadrada de 25 es 5")
            
            # 3 * pi ≈ 9.42
            tiene_resultado = '9.4' in output or '9,4' in output or '9.42' in output
            self.assertTrue(tiene_resultado, "Debe mostrar el resultado de 3 * pi (aprox 9.42)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('builtins.input', side_effect=['4', '2'])
    def test_solicita_dos_numeros(self, mock_input):
        """Verifica que se soliciten dos números"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            self.assertEqual(mock_input.call_count, 2,
                           "Debe solicitar 2 números: uno para raíz cuadrada y otro para multiplicar por pi")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    def test_importa_modulo_math(self):
        """Verifica que se importe el módulo math"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            
            self.assertIn('import math', code, "Debe importar el módulo math")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 8: Explorando el Módulo math")
    print("=" * 60)
    unittest.main(verbosity=2)


