'''
Created on 29 sept 2025

@author: migueltoro
'''

# -*- coding: utf-8 -*-
"""
IMPORTANCIA DE USAR DIFERENTES VALORES EN LOS TESTS
- Incluimos para cada función valores típicos y **valores límite** (listas/cadenas vacías,
  n==k, etc.).
- Variar entradas ayuda a descubrir errores (off-by-one, mayúsculas/minúsculas, huecos, etc.).
- En funciones de ficheros usamos carpetas temporales y captura de stdout para no
  depender del entorno.
"""
import unittest


# Intentar importar como paquete (es/funciones.py), y si falla, como módulo plano
import us.lsi.practicas_b1.funciones_b1 as func

class TestFuncionesBloque1V2(unittest.TestCase):

    def test_parte_fraccionaria(self):
        # positivos, cero y negativos
        self.assertAlmostEqual(func.parte_fraccionaria(12.345), 0.345, places=6)
        self.assertAlmostEqual(func.parte_fraccionaria(0.0), 0.0, places=6)
        self.assertAlmostEqual(func.parte_fraccionaria(-3.25), 0.75, places=6)
        # valores enteros
        self.assertAlmostEqual(func.parte_fraccionaria(5.0), 0.0, places=6)

    def test_redondear_a_decimales(self):
        # redondeos típicos
        self.assertEqual(func.redondear_a_decimales(12.3456, 2), 12.35)
        self.assertEqual(func.redondear_a_decimales(1.2349, 3), 1.235)
        # negativos
        self.assertEqual(func.redondear_a_decimales(-1.2349, 3), -1.235)
        # cero decimales
        self.assertEqual(func.redondear_a_decimales(9.9, 0), 10.0)

    def test_limpiar_espacios(self):
        self.assertEqual(func.limpiar_espacios("  hola   mundo  "), "hola mundo")
        self.assertEqual(func.limpiar_espacios(""), "")
        self.assertEqual(func.limpiar_espacios(" a  b   c "), "a b c")

    def test_es_isograma(self):
        self.assertTrue(func.es_isograma("murciélago"))
        self.assertFalse(func.es_isograma("isogram-a"))
        self.assertFalse(func.es_isograma("casa"))
        self.assertTrue(func.es_isograma("  "))

    def test_a_camel_case(self):
        self.assertEqual(func.a_camel_case("hola mundo feliz"), "holaMundoFeliz")
        self.assertEqual(func.a_camel_case("Hola"), "hola")
        self.assertEqual(func.a_camel_case("   "), "")
        self.assertEqual(func.a_camel_case("uno   dos"), "unoDos")

    def test_invertir_cadena(self):
        self.assertEqual(func.invertir_cadena("Hola"), "aloH")
        self.assertEqual(func.invertir_cadena(""), "")
        self.assertEqual(func.invertir_cadena("a"), "a")

    def test_reemplazar_vocales(self):
        self.assertEqual(func.reemplazar_vocales("murciélago"), "m-rc--l-g-")
        self.assertEqual(func.reemplazar_vocales("AEIOU"), "-----")
        self.assertEqual(func.reemplazar_vocales("xyz"), "xyz")

    def test_contar_palabras(self):
        self.assertEqual(func.contar_palabras("hola mundo feliz"), 3)
        self.assertEqual(func.contar_palabras("  uno   dos  "), 2)
        self.assertEqual(func.contar_palabras(""), 0)

    def test_dias_laborables_entre(self):
        from datetime import date
        fest = {date(2025, 9, 16)}
        a = date(2025, 9, 15)  # lunes
        b = date(2025, 9, 19)  # viernes
        self.assertEqual(func.dias_laborables_entre(a, b, set()), 5)
        self.assertEqual(func.dias_laborables_entre(a, b, fest), 4)

    def test_siguiente_laborable(self):
        from datetime import date
        # 20/09/2025 es sábado -> siguiente laborable: lunes 22/09/2025
        self.assertEqual(func.siguiente_laborable(date(2025,9,20), set()), date(2025,9,22))

    def test_suma_lista(self):
        self.assertEqual(func.suma_lista([1.0,2.0,3.0]), 6.0)
        self.assertEqual(func.suma_lista([]), 0.0)
        self.assertAlmostEqual(func.suma_lista([0.1,0.2]), 0.3, places=7)

    def test_media_lista(self):
        self.assertEqual(func.media_lista([1.0,2.0,3.0]), 2.0)
        with self.assertRaises(AssertionError):
            func.media_lista([])

    def test_maximo_lista(self):
        self.assertEqual(func.maximo_lista([3,7,2]), 7)
        with self.assertRaises(AssertionError):
            func.maximo_lista([])

    def test_minimo_lista(self):
        self.assertEqual(func.minimo_lista([3,7,2]), 2)
        with self.assertRaises(AssertionError):
            func.minimo_lista([])

    def test_diferencias_consecutivas(self):
        self.assertEqual(func.diferencias_consecutivas([5,7,10]), [2,3])
        # bordes
        self.assertEqual(func.diferencias_consecutivas([]), [])
        self.assertEqual(func.diferencias_consecutivas([42]), [])
        self.assertEqual(func.diferencias_consecutivas([0,0,0]), [0,0])

    def test_pares_cuadrados(self):
        self.assertEqual(func.pares_cuadrados([1,2,3,4]), [4,16])
        self.assertEqual(func.pares_cuadrados([]), [])
        self.assertEqual(func.pares_cuadrados([1,3,5]), [])

    def test_filtrar_mayores(self):
        self.assertEqual(func.filtrar_mayores([1,5,7,2], 4), [5,7])
        self.assertEqual(func.filtrar_mayores([], 10), [])
        self.assertEqual(func.filtrar_mayores([4,4,5], 4), [5])

    def test_es_primo(self):
        # límites y varios casos
        self.assertFalse(func.es_primo(1))
        self.assertTrue(func.es_primo(2))
        self.assertTrue(func.es_primo(3))
        self.assertFalse(func.es_primo(9))
        self.assertTrue(func.es_primo(29))
        self.assertFalse(func.es_primo(100))

    def test_divisores(self):
        self.assertEqual(func.divisores(12), [1,2,3,4,6,12])
        self.assertEqual(func.divisores(13), [1,13])
        self.assertEqual(func.divisores(2), [1,2])

    def test_cadena_mas_larga(self):
        self.assertEqual(func.cadena_mas_larga(["hola","adiós","murciélago"]), "murciélago")
        self.assertEqual(func.cadena_mas_larga(["solo"]), "solo")

    def test_union_listas(self):
        self.assertEqual(func.union_listas([1,2,3],[3,4]), [1,2,3,4])
        self.assertEqual(func.union_listas([], [1,1]), [1])

    def test_interseccion_listas(self):
        self.assertEqual(func.interseccion_listas([1,2,3],[2,3,4]), [2,3])
        self.assertEqual(func.interseccion_listas([1],[2]), [])

    def test_diferencia_listas(self):
        self.assertEqual(func.diferencia_listas([1,2,3],[2,3]), [1])
        self.assertEqual(func.diferencia_listas([], [1,2]), [])

    def test_producto_rango(self):
        self.assertEqual(func.producto_rango(4,4), 4)   # n==k
        self.assertEqual(func.producto_rango(5,3), 60)
        self.assertEqual(func.producto_rango(1,1), 1)

    def test_capitalizar_palabras(self):
        self.assertEqual(func.capitalizar_palabras("HOLA MUNDO FELIZ"), "Hola Mundo Feliz")
        self.assertEqual(func.capitalizar_palabras("PYTHON"), "Python")
        self.assertEqual(func.capitalizar_palabras(""), "")
        self.assertEqual(func.capitalizar_palabras("HOLA   DEL   MUNDO"), "Hola Del Mundo")

    def test_crear_fichero_texto(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "f.txt")
            self.assertTrue(func.crear_fichero_texto(p, "hola"))
            self.assertTrue(os.path.exists(p))

    def test_leer_fichero_texto(self):
        import tempfile, os, io, contextlib
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "f.txt")
            func.crear_fichero_texto(p, "hola\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                func.leer_fichero_texto(p)
            self.assertEqual(buf.getvalue(), "hola\n")

    def test_contar_lineas_no_vacias(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "f.txt")
            func.crear_fichero_texto(p, "uno\n\n dos\n\n\n")
            self.assertEqual(func.contar_lineas_no_vacias(p), 2)

    def test_num_palabras(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "t.txt")
            with open(p, "w", encoding="utf-8") as f:
                f.write("Hola mundo\nEsto es una prueba")
            self.assertEqual(func.num_palabras(p), 6)
            # fichero vacío
            p2 = os.path.join(td, "vacio.txt")
            with open(p2, "w", encoding="utf-8") as f:
                f.write("")
            self.assertEqual(func.num_palabras(p2), 0)

    def test_num_repeticiones_palabras(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "t.txt")
            with open(p, "w", encoding="utf-8") as f:
                f.write("Hola mundo\nHola de nuevo mundo")
            self.assertEqual(func.num_repeticiones_palabras(p, "hola"), 2)
            self.assertEqual(func.num_repeticiones_palabras(p, "mundo"), 2)
            self.assertEqual(func.num_repeticiones_palabras(p, "adios"), 0)

    def test_palabras_mas_frecuentes(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "f.txt")
            func.crear_fichero_texto(p, "uno dos dos\nTRES tres tres\n")
            top2 = func.palabras_mas_frecuentes(p, 2)
            self.assertEqual(top2[0], ("tres", 3))
            self.assertEqual(top2[1], ("dos", 2))
            top5 = func.palabras_mas_frecuentes(p, 5)  # más que distintas
            self.assertGreaterEqual(len(top5), 2)

    def test_crear_fichero_csv(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "provincias.csv")
            self.assertTrue(func.crear_fichero_csv(p, "Sevilla|Andalucía\n"))
            self.assertTrue(os.path.exists(p))

    def test_leer_fichero_csv(self):
        import tempfile, os, io, contextlib
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "provincias.csv")
            func.crear_fichero_csv(p, "Sevilla|Andalucía\nGranada|Andalucía\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                func.leer_fichero_csv(p, "|")
            out = buf.getvalue()
            self.assertIn("Sevilla|Andalucía", out)
            self.assertIn("Granada|Andalucía", out)

    def test_num_filas_csv(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "provincias.csv")
            func.crear_fichero_csv(p, "A|B\nC|D\n")
            self.assertEqual(func.num_filas_csv(p), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
