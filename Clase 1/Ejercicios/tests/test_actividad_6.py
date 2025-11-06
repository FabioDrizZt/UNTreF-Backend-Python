"""
Tests para Actividad 6: Generador de Apodos

Estos tests verifican que tu programa genere un apodo
con las primeras 3 letras del nombre y apellido en mayúsculas.
"""

import unittest

def get_actividad_path():
    """Obtiene la ruta al archivo de actividad"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    actividades_dir = os.path.join(script_dir, '..', 'actividades')
    return os.path.join(actividades_dir, 'actividad_6.py')

from unittest.mock import patch
from io import StringIO

class TestActividad6(unittest.TestCase):
    """Tests para verificar la Actividad 6"""
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Carlos', 'Garcia'])
    def test_apodo_nombres_normales(self, mock_input, mock_stdout):
        """Prueba con Carlos Garcia -> CARGAR"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe contener CARGAR (3 letras de Carlos + 3 de Garcia)
            self.assertIn('CARGAR', output.upper(), 
                         "El apodo debe ser CARGAR (CAR de Carlos + GAR de Garcia)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Ana', 'Lopez'])
    def test_apodo_ana_lopez(self, mock_input, mock_stdout):
        """Prueba con Ana Lopez -> ANALOP"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Debe contener ANALOP o ANALÓP
            output_upper = output.upper()
            self.assertTrue('ANALOP' in output_upper or 'ANALÓP' in output_upper,
                          "El apodo debe ser ANALOP (ANA + LOP)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['Pedro', 'Martinez'])
    def test_apodo_pedro_martinez(self, mock_input, mock_stdout):
        """Prueba con Pedro Martinez -> PEDMAR"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            self.assertIn('PEDMAR', output.upper(),
                         "El apodo debe ser PEDMAR (PED + MAR)")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('builtins.input', side_effect=['Juan', 'Perez'])
    def test_solicita_nombre_y_apellido(self, mock_input):
        """Verifica que se soliciten nombre y apellido"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            
            self.assertEqual(mock_input.call_count, 2, 
                           "Debe solicitar 2 datos: nombre y apellido")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['maria', 'fernandez'])
    def test_apodo_en_mayusculas(self, mock_input, mock_stdout):
        """Verifica que el apodo esté en mayúsculas"""
        try:
            with open(get_actividad_path(), 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            output = mock_stdout.getvalue()
            
            # Buscar el apodo en la salida
            tiene_mayusculas = 'MARFER' in output or 'MARFÉR' in output
            self.assertTrue(tiene_mayusculas,
                          "El apodo debe estar en MAYÚSCULAS")
        except Exception as e:
            self.fail(f"El código generó un error: {e}")


if __name__ == '__main__':
    print("=" * 60)
    print("TESTS PARA ACTIVIDAD 6: Generador de Apodos")
    print("=" * 60)
    unittest.main(verbosity=2)


