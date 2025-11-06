"""
Tests para Actividad 7: Calculadora de Propinas

Estos tests verifican que tu programa calcule correctamente
el 15% de propina y el total a pagar.
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_7.py')

from unittest.mock import patch
from io import StringIO

class TestActividad7(unittest.TestCase):
    """Tests para verificar la Actividad 7"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='100')
    def test_propina_monto_100(self, mock_input, mock_stdout):
        """Prueba con monto 100 -> propina 15, total 115"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar la propina (15)
            self.assertIn('15', output, "Debe mostrar la propina de 15 (15% de 100)")
            
            # Debe mostrar el total (115)
            self.assertIn('115', output, "Debe mostrar el total de 115 (100 + 15)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='200')
    def test_propina_monto_200(self, mock_input, mock_stdout):
        """Prueba con monto 200 -> propina 30, total 230"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar la propina (30)
            self.assertIn('30', output, "Debe mostrar la propina de 30 (15% de 200)")
            
            # Debe mostrar el total (230)
            self.assertIn('230', output, "Debe mostrar el total de 230 (200 + 30)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='50')
    def test_propina_monto_50(self, mock_input, mock_stdout):
        """Prueba con monto 50 -> propina 7.5, total 57.5"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar la propina (7.5)
            self.assertTrue('7.5' in output or '7,5' in output,
                          "Debe mostrar la propina de 7.5 (15% de 50)")
            
            # Debe mostrar el total (57.5)
            self.assertTrue('57.5' in output or '57,5' in output,
                          "Debe mostrar el total de 57.5 (50 + 7.5)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('builtins.input', return_value='80')
    def test_solicita_monto(self, mock_input):
        """Verifica que se solicite el monto"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            self.assertEqual(mock_input.call_count, 1, "Debe solicitar el monto de la cuenta")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='100')
    def test_muestra_propina_y_total(self, mock_input, mock_stdout):
        """Verifica que se muestren tanto la propina como el total"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            lines = output.strip().split('\n')
            
            # Debe haber al menos 2 líneas (propina y total)
            self.assertGreaterEqual(len(lines), 2,
                                  "Debe mostrar tanto el monto de la propina como el total a pagar")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 7: Calculadora de Propinas")
    print("=" * 60)
    unittest.main(verbosity=2)


