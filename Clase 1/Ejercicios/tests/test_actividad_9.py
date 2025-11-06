"""
Tests para Actividad 9: Generador de Tarjetas de Presentación

Estos tests verifican que tu programa genere una tarjeta
de presentación con formato multilínea.
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_9.py')

from unittest.mock import patch
from io import StringIO

class TestActividad9(unittest.TestCase):
    """Tests para verificar la Actividad 9"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Juan Perez', 'Desarrollador', 'Buenos Aires'])
    def test_tarjeta_completa(self, mock_input, mock_stdout):
        """Prueba con datos completos"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe contener todos los datos
            self.assertIn('Juan Perez', output, "La tarjeta debe incluir el nombre")
            self.assertIn('Desarrollador', output, "La tarjeta debe incluir la profesión")
            self.assertIn('Buenos Aires', output, "La tarjeta debe incluir la ciudad")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Ana Lopez', 'Diseñadora', 'Madrid'])
    def test_tarjeta_diferentes_datos(self, mock_input, mock_stdout):
        """Prueba con diferentes datos"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Ana Lopez', output)
            self.assertIn('Diseñadora', output)
            self.assertIn('Madrid', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('builtins.input', side_effect=['Carlos', 'Ingeniero', 'Lima'])
    def test_solicita_tres_datos(self, mock_input):
        """Verifica que se soliciten tres datos"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            self.assertEqual(mock_input.call_count, 3,
                           "Debe solicitar 3 datos: nombre, profesión y ciudad")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Pedro', 'Doctor', 'Bogotá'])
    def test_formato_multilinea(self, mock_input, mock_stdout):
        """Verifica que la tarjeta tenga formato con varias líneas"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            lines = output.strip().split('\n')
            
            # La tarjeta debe tener múltiples líneas
            self.assertGreater(len(lines), 1,
                             "La tarjeta debe tener formato con varias líneas (saltos de línea)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Maria', 'Arquitecta', 'Santiago'])
    def test_tarjeta_simulada(self, mock_input, mock_stdout):
        """Verifica que simule una tarjeta (con algún formato visual)"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Verificar que tenga al menos 3 líneas y todos los datos
            lines = [l for l in output.split('\n') if l.strip()]
            self.assertGreaterEqual(len(lines), 3,
                                  "La tarjeta debe organizar la información en múltiples líneas")
            
            # Verificar que contenga los datos
            self.assertIn('Maria', output)
            self.assertIn('Arquitecta', output)
            self.assertIn('Santiago', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 9: Generador de Tarjetas de Presentación")
    print("=" * 60)
    unittest.main(verbosity=2)


