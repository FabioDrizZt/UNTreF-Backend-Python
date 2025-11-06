"""
Tests para Actividad 5: Cálculo de Año de Nacimiento

Estos tests verifican que tu programa calcule correctamente
el año de nacimiento basado en la edad ingresada.
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_5.py')

from unittest.mock import patch
from io import StringIO
import datetime

class TestActividad5(unittest.TestCase):
    """Tests para verificar la Actividad 5"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='30')
    def test_calculo_edad_30(self, mock_input, mock_stdout):
        """Prueba con edad 30"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # El año actual es 2025, así que 2025 - 30 = 1995
            # Pero también puede ser 2024 si usan otro año
            # Verificamos que haya un año de 4 dígitos cerca
            año_esperado_1 = str(2025 - 30)  # 1995
            año_esperado_2 = str(2024 - 30)  # 1994
            
            tiene_calculo = año_esperado_1 in output or año_esperado_2 in output
            self.assertTrue(tiene_calculo, 
                          f"Debe mostrar el año de nacimiento calculado (esperado {año_esperado_1} o similar)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='20')
    def test_calculo_edad_20(self, mock_input, mock_stdout):
        """Prueba con edad 20"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Buscar años cercanos al resultado esperado
            posibles_años = ['2005', '2004', '2003']
            tiene_año = any(año in output for año in posibles_años)
            self.assertTrue(tiene_año, "Debe mostrar el año de nacimiento calculado")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='0')
    def test_edad_cero(self, mock_input, mock_stdout):
        """Prueba con edad 0 (recién nacido)"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe mostrar el año actual
            posibles_años = ['2025', '2024']
            tiene_año_actual = any(año in output for año in posibles_años)
            self.assertTrue(tiene_año_actual, "Con edad 0 debe mostrar el año actual")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('builtins.input', return_value='25')
    def test_solicita_edad(self, mock_input):
        """Verifica que se solicite la edad"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            self.assertEqual(mock_input.call_count, 1, "Debe solicitar la edad")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 5: Cálculo de Año de Nacimiento")
    print("=" * 60)
    unittest.main(verbosity=2)


