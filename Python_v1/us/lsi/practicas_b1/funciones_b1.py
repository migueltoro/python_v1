'''
Created on 29 sept 2025

@author: migueltoro
'''

# -*- coding: utf-8 -*-
from datetime import date, timedelta
from math import floor

# -----------------------------------------------------------------------------
# 1) NÚMEROS Y EXPRESIONES
# -----------------------------------------------------------------------------


def parte_fraccionaria(a: float) -> float:
    """Devuelve la parte fraccionaria de un número en [0,1).
    Idea: parte_fraccionaria = a - floor(a)
    Ejemplos:
        3.14 -> 0.14
       -3.25 -> 0.75  (porque floor(-3.25) = -4; -3.25 - (-4) = 0.75)
    """
    return a - floor(a)


def redondear_a_decimales(a: float, n: int) -> float:
    """Redondea 'a' a 'n' decimales usando round (suficiente para este bloque)."""
    return round(a, n)


# -----------------------------------------------------------------------------
# 2) CADENAS DE TEXTO
# -----------------------------------------------------------------------------


def limpiar_espacios(s: str) -> str:
    """Quita espacios al principio y al final y deja un solo espacio entre palabras.
    Estrategia: dividir por espacios (split sin argumentos) y volver a unir con ' '.
    """
    partes:list[str] = s.split()  # split() sin argumentos colapsa espacios múltiples
    resultado:str = " ".join(partes)
    return resultado


def _quitar_tildes_basico(s: str) -> str:
    """Quita tildes comunes de vocales.
    Nota: Para un tratamiento completo se podría usar 'unicodedata', pero aquí
    preferimos una sustitución directa y explícita.
    """
    reemplazos:dict[str,str] = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "a",
        "É": "e",
        "Í": "i",
        "Ó": "o",
        "Ú": "u",
    }
    salida:str = ""
    for ch in s:
        if ch in reemplazos:
            salida += reemplazos[ch]
        else:
            salida += ch
    return salida


def es_isograma(s: str) -> bool:
    """Devuelve True si s no contiene letras repetidas.
    - Ignora espacios y guiones.
    - Ignora tildes (á->a, etc.).
    - No diferencia mayúsculas/minúsculas.
    """
    # 1) Normalizamos la cadena:
    #    - pasamos a minúsculas
    #    - quitamos tildes comunes
    #    - eliminamos espacios y guiones
    s_normal:str = _quitar_tildes_basico(s.lower())
    sin_esp_ni_guion:str = ""
    for ch in s_normal:
        if ch != " " and ch != "-":
            sin_esp_ni_guion += ch

    # 2) Recorremos y comprobamos si aparece alguna letra repetida
    #    (guardamos las ya vistas en un conjunto)
    vistas:set[str] = set()
    for ch in sin_esp_ni_guion:
        if ch.isalpha():  # sólo consideramos letras
            if ch in vistas:
                return False
            vistas.add(ch)
    return True


def a_camel_case(s: str) -> str:
    """Convierte 'hola mundo feliz' -> 'holaMundoFeliz'.
    - Primera palabra en minúscula
    - Resto de palabras con primera letra en mayúscula y el resto tal cual
    """
    palabras:list[str] = s.split()  # divide por espacios y colapsa múltiples
    if len(palabras) == 0:
        return ""
    cabeza:str = palabras[0].lower()
    cola:str = ""
    for w in palabras[1:]:
        if len(w) > 0:
            cola += w[0].upper() + w[1:]
    return cabeza + cola


def invertir_cadena(s: str) -> str:
    """Devuelve la cadena invertida usando un método sencillo con acumulación."""
    rev:str = ""
    # Recorremos de atrás hacia delante con índices
    i:int = len(s) - 1
    while i >= 0:
        rev += s[i]
        i -= 1
    return rev


def reemplazar_vocales(s: str) -> str:
    """Sustituye todas las vocales (con y sin tilde) por guiones.
    Consideramos a, e, i, o, u y sus versiones acentuadas.
    """
    vocales:str = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    salida:str = ""
    for ch in s:
        if ch in vocales:
            salida += "-"
        else:
            salida += ch
    return salida


def contar_palabras(s: str) -> int:
    """Cuenta las palabras separadas por uno o más espacios."""
    partes:list[str] = s.split()  # split() sin argumentos ignora espacios extra
    return len(partes)


# -----------------------------------------------------------------------------
# 3) FECHAS
# -----------------------------------------------------------------------------


def _es_laborable(d: date, festivos: set[date]) -> bool:
    """Devuelve True si la fecha 'd' es de Lunes(0) a Viernes(4) y no es festivo."""
    return d.weekday() < 5 and d not in festivos


def dias_laborables_entre(a: date, b: date, festivos: set[date]) -> int:
    """Cuenta cuántos días laborables hay entre 'a' y 'b' (ambos inclusive)."""
    assert a <= b, "La fecha inicial debe ser <= que la final"
    cuenta:int = 0
    actual:date = a
    while actual <= b:
        if _es_laborable(actual, festivos):
            cuenta += 1
        actual = actual + timedelta(days=1)
    return cuenta


def siguiente_laborable(d: date, festivos: set[date]) -> date:
    """Devuelve la primera fecha laborable estrictamente posterior a 'd'."""
    actual:date = d + timedelta(days=1)
    while not _es_laborable(actual, festivos):
        actual = actual + timedelta(days=1)
    return actual


# -----------------------------------------------------------------------------
# 4) OPERACIONES BÁSICAS CON LISTAS
# -----------------------------------------------------------------------------


def suma_lista(xs: list[float]) -> float:
    """Suma todos los elementos usando un bucle for."""
    total:float = 0.0
    for x in xs:
        total += x
    return total


def media_lista(xs: list[float]) -> float:
    """Media aritmética: suma / número de elementos (asume xs no vacía)."""
    assert len(xs) > 0, "La lista no puede estar vacía"
    total:float = suma_lista(xs)
    return total / len(xs)


def maximo_lista(xs: list[int]) -> int:
    """Devuelve el máximo de forma iterativa (asume xs no vacía)."""
    assert len(xs) > 0, "La lista no puede estar vacía"
    m:int = xs[0]
    for i in range(1, len(xs)):
        if xs[i] > m:
            m = xs[i]
    return m


def minimo_lista(xs: list[int]) -> int:
    """Devuelve el mínimo de forma iterativa (asume xs no vacía)."""
    assert len(xs) > 0, "La lista no puede estar vacía"
    m :int = xs[0]
    for i in range(1, len(xs)):
        if xs[i] < m:
            m = xs[i]
    return m


# -----------------------------------------------------------------------------
# 5) TRANSFORMACIONES Y FILTRADOS
# -----------------------------------------------------------------------------


def diferencias_consecutivas(xs: list[int]) -> list[int]:
    """Devuelve las diferencias xs[i] - xs[i-1] para i=1..n-1."""
    res: list[int] = []
    i:int = 1
    while i < len(xs):
        diff = xs[i] - xs[i - 1]
        res.append(diff)
        i += 1
    return res


def pares_cuadrados(xs: list[int]) -> list[int]:
    """Devuelve los cuadrados de los números pares de la lista."""
    res: list[int] = []
    for x in xs:
        if x % 2 == 0:
            res.append(x * x)
    return res


def filtrar_mayores(xs: list[int], umbral: int) -> list[int]:
    """Devuelve los elementos de xs que son estrictamente mayores que 'umbral'."""
    res: list[int] = []
    for x in xs:
        if x > umbral:
            res.append(x)
    return res


# -----------------------------------------------------------------------------
# 6) BÚSQUEDA Y SELECCIÓN
# -----------------------------------------------------------------------------


def es_primo(n: int) -> bool:
    """Comprueba si n es primo mediante un método elemental.
    - n <= 1 -> no primo
    - probamos divisores desde 2 hasta sqrt(n) (i*i <= n)
    """
    if n <= 1:
        return False
    # 2 y 3 son primos
    if n == 2 or n == 3:
        return True
    # si es par y no es 2, no es primo
    if n % 2 == 0:
        return False
    # probamos divisores impares
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def divisores(n: int) -> list[int]:
    """Devuelve la lista de divisores de n en orden ascendente (método simple)."""
    assert n > 0, "n debe ser positivo"
    res: list[int] = []
    d:int = 1
    while d <= n:
        if n % d == 0:
            res.append(d)
        d += 1
    return res


def cadena_mas_larga(xs: list[str]) -> str:
    """Devuelve la cadena de mayor longitud (si hay empate, la primera)."""
    assert len(xs) > 0, "La lista no puede estar vacía"
    pos_max:int = 0
    i:int = 1
    while i < len(xs):
        if len(xs[i]) > len(xs[pos_max]):
            pos_max = i
        i += 1
    return xs[pos_max]


# -----------------------------------------------------------------------------
# 7) CONJUNTOS Y COLECCIONES (sin 'set' para practicar lógica básica)
# -----------------------------------------------------------------------------


def union_listas(xs: list[int], ys: list[int]) -> list[int]:
    """Devuelve xs ∪ ys sin repetidos manteniendo orden relativo simple.
    Implementación básica sin usar 'set', para practicar:
      - añadimos todos los de xs que no estén aún
      - añadimos todos los de ys que no estén aún
    (Luego ordenamos numéricamente para que sea estable en los tests.)
    """
    res: list[int] = []
    # añadir xs
    for x in xs:
        if x not in res:
            res.append(x)
    # añadir ys
    for y in ys:
        if y not in res:
            res.append(y)
    # para comparaciones típicas, devolvemos ordenada (requisito de tests)
    res_ordenada: list[int] = sorted(res)
    return res_ordenada


def interseccion_listas(xs: list[int], ys: list[int]) -> list[int]:
    """Elementos comunes a xs e ys (sin repetidos)."""
    res: list[int] = []
    for x in xs:
        # aparece en xs y en ys y todavía no lo hemos añadido
        if (x in ys) and (x not in res):
            res.append(x)
    return sorted(res)


def diferencia_listas(xs: list[int], ys: list[int]) -> list[int]:
    """Elementos de xs que NO están en ys (sin repetidos)."""
    res: list[int] = []
    for x in xs:
        if (x not in ys) and (x not in res):
            res.append(x)
    return sorted(res)



# ---------------------------------------------------------------------
# Funciones adicionales
# ---------------------------------------------------------------------


def producto_rango(n: int, k: int) -> int:
    """
    Calcula el producto de todos los enteros i en el rango [k, n], con n >= k.

    Ejemplos:
        producto_rango(5, 3) = 3 * 4 * 5 = 60
        producto_rango(4, 4) = 4
    """
    assert n >= k
    prod:int = 1
    i:int = k
    while i <= n:
        prod = prod * i
        i += 1
    return prod


def capitalizar_palabras(s: str) -> str:
    """
    Dada una cadena en MAYÚSCULAS, devuelve otra con:
      - Primera letra de cada palabra en mayúscula
      - Resto de letras en minúscula

    Estrategia:
      1) Dividir por espacios (split) para obtener palabras.
      2) Para cada palabra:
         - si está vacía, saltar
         - construir palabra como word[0].upper() + word[1:].lower()
      3) Unir con un espacio.

    Ejemplos:
        capitalizar_palabras("HOLA MUNDO FELIZ") -> "Hola Mundo Feliz"
        capitalizar_palabras("PYTHON ES GENIAL") -> "Python Es Genial"
    """
    partes:list[str] = s.split()
    resultado:str = ""
    i:int = 0
    while i < len(partes):
        w:str = partes[i]
        if len(w) > 0:
            nueva:str = w[0].upper() + w[1:].lower()
            if resultado == "":
                resultado = nueva
            else:
                resultado = resultado + " " + nueva
        i += 1
    return resultado


# -----------------------------------------------------------------------------
# 8) FICHEROS DE TEXTO Y CSV (básico)
# -----------------------------------------------------------------------------


def crear_fichero_texto(nombre: str, texto: str) -> bool:
    """Crea un fichero de texto con 'texto'. Devuelve True si todo va bien."""
    try:
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(texto)
            f.close()
            return True
    except Exception:
        return False


def leer_fichero_texto(nombre: str) -> None:
    """Muestra por pantalla el contenido completo del fichero 'nombre'."""
    with open(nombre, "r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido, end="")


def contar_lineas_no_vacias(ruta: str) -> int:
    """Cuenta cuántas líneas no están vacías (tienen algún carácter no espacio)."""
    contador:int = 0
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip() != "":
                contador += 1
    return contador


def num_palabras(fichero: str) -> int:
    """
    Devuelve el número de palabras que contiene el fichero de texto
    pasado como parámetro de entrada.

    Estrategia:
      1) Abrir el fichero en modo lectura.
      2) Recorrer todas sus líneas.
      3) Dividir cada línea en palabras usando split() (ignora espacios extra).
      4) Acumular el número de palabras encontradas.
      5) Devolver el total.

    Ejemplo:
        Si el fichero contiene:
            "Hola mundo\n
             Esto es una prueba"
        Entonces:
            numPalabras("fichero.txt") -> 5
    """
    total:int = 0
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            palabras:list[str] = linea.split()
            total = total + len(palabras)
    return total


def num_repeticiones_palabras(fichero: str, palabra: str) -> int:
    """
    Devuelve el número de veces que aparece la palabra dada en el fichero.

    Estrategia:
      1) Abrir el fichero en modo lectura.
      2) Leer línea a línea.
      3) Pasar a minúsculas tanto la línea como la palabra buscada
         (para que la comparación no dependa de mayúsculas/minúsculas).
      4) Dividir la línea en palabras usando split().
      5) Contar cuántas veces aparece la palabra en la lista de palabras.
      6) Acumular el resultado y devolverlo.

    Parámetros:
      - fichero: ruta del fichero de texto a analizar.
      - palabra: palabra que se desea contar.

    Ejemplo:
        Contenido del fichero:
            "Hola mundo\n
             Hola de nuevo mundo"
        numRepeticionesPalabras("fichero.txt", "hola") -> 2
        numRepeticionesPalabras("fichero.txt", "mundo") -> 2
    """
    total:int = 0
    palabra = palabra.lower()
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            palabras_linea:list[str] = linea.lower().split()
            total = total + palabras_linea.count(palabra)
    return total


def palabras_mas_frecuentes(ruta: str, k: int) -> list[tuple[str, int]]:
    """Devuelve las k palabras más frecuentes (minúsculas, separadas por espacios).
    No se usan estructuras avanzadas. Contamos con un diccionario clásico.
    """
    frecuencias: dict[str, int] = {}
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            # Pasamos a minúsculas y separamos por espacios simples
            trozos:list[str] = linea.lower().split(" ")
            for w in trozos:
                palabra:str = w.strip()
                if palabra != "":
                    if palabra in frecuencias:
                        frecuencias[palabra] += 1
                    else:
                        frecuencias[palabra] = 1

    # Convertimos el diccionario en lista de pares (palabra, frecuencia)
    items:list[tuple[str,int]] = []
    for p, c in frecuencias.items():
        items.append((p, c))

    # Ordenamos por: frecuencia descendente y palabra ascendente (para estabilidad)
    # Implementamos una ordenación sencilla usando 'sorted' con key.
    items_ordenados:list[tuple[str,int]] = sorted(items, key=lambda par: (-par[1], par[0]))

    # Tomamos los k primeros (si hay menos de k, devuelve los que haya)
    resultado:list[tuple[str,int]] = items_ordenados[:k]
    return resultado


def crear_fichero_csv(nombre: str, texto: str) -> bool:
    """Crea un fichero CSV (texto) tal cual, sin librería 'csv'.
    El separador lo decidirá quien lo lea (por ejemplo '|').
    """
    try:
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(texto)
            return True
    except Exception:
        return False


def leer_fichero_csv(nombre: str, delimitador: str) -> None:
    """Lee un CSV sencillo y muestra cada línea de forma directa.
    (Usamos split con el delimitador dado; no hacemos parsing avanzado.)
    """
    with open(nombre, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.rstrip("\n")
            if linea != "":
                campos:list[str] = linea.split(delimitador)
                # Volvemos a unir para mostrar claramente qué delimitador se usa
                print(delimitador.join(campos))


def num_filas_csv(ficheroCSV: str) -> int:
    """Cuenta cuántas líneas no vacías tiene un CSV."""
    contador:int = 0
    with open(ficheroCSV, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip() != "":
                contador += 1
    return contador


if __name__ == '__main__':
    pass