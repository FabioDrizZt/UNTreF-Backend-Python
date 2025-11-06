"""
Tests para Actividad 2: Información Personal

Estos tests verifican que tu programa solicite nombre, edad y ciudad,
y luego muestre la información en una oración.
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_2.py')

from unittest.mock import patch
from io import StringIO

class TestActividad2(unittest.TestCase):
    """Tests para verificar la Actividad 2"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Carlos', '30', 'Buenos Aires'])
    def test_informacion_completa(self, mock_input, mock_stdout):
        """Prueba con nombre, edad y ciudad"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Verificar que contenga todos los datos
            self.assertIn('Carlos', output, "La salida debe incluir el nombre")
            self.assertIn('30', output, "La salida debe incluir la edad")
            self.assertIn('Buenos Aires', output, "La salida debe incluir la ciudad")
            
            # Verificar que sea una oración (más de una palabra)
            palabras = output.split()
            self.assertGreater(len(palabras), 3, "Debe mostrar la información en una oración completa")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Ana', '25', 'Madrid'])
    def test_diferentes_datos(self, mock_input, mock_stdout):
        """Prueba con diferentes datos de entrada"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('Ana', output)
            self.assertIn('25', output)
            self.assertIn('Madrid', output)
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('builtins.input', side_effect=['Pedro', '40', 'Lima'])
    def test_solicita_tres_inputs(self, mock_input):
        """Verifica que se soliciten tres datos (nombre, edad, ciudad)"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            # Verificar que se llamó input() 3 veces
            self.assertEqual(mock_input.call_count, 3, "Debe solicitar 3 datos: nombre, edad y ciudad")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 2: Información Personal")
    print("=" * 60)
    unittest.main(verbosity=2)


