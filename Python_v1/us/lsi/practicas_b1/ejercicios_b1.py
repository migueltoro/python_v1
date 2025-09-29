'''
Created on 29 sept 2025

@author: migueltoro
'''


from us.lsi.practicas_b1.funciones_b1 import *
from us.lsi.tools.File import absolute_path

def main()->None:
    # Números
    print(parte_fraccionaria(3.14))            # 0.14
    print(redondear_a_decimales(12.3456, 2))   # 12.35

    # Cadenas
    print(limpiar_espacios('  hola   mundo  '))         # 'hola mundo'
    print(es_isograma('murciélago'))                    # True
    print(a_camel_case('hola mundo feliz'))             # 'holaMundoFeliz'
    print(invertir_cadena('Hola'))                      # 'aloH'
    print(reemplazar_vocales('murciélago'))             # 'm-rc---l-g-'
    print(contar_palabras('hola   mundo  feliz'))       # 3

    # Fechas
    fest:set[date] = {date(2023,5,1)}
    print(dias_laborables_entre(date(2023,5,1), date(2023,5,5), fest))  # 4
    print(siguiente_laborable(date(2023,5,6), fest))                    # 2023-05-09

    # Ficheros (se crean en el directorio actual)
    crear_fichero_texto(absolute_path('datos/practicas_b1/refran.txt'), 'No por mucho madrugar\namanece más temprano\n\nfin')
    leer_fichero_texto(absolute_path('datos/practicas_b1/refran.txt'))
    print()
    print(contar_lineas_no_vacias(absolute_path('datos/practicas_b1/refran.txt')))
    print(palabras_mas_frecuentes(absolute_path('datos/practicas_b1/refran.txt'), 2))

    # CSV
    crear_fichero_csv(absolute_path('datos/practicas_b1/provincias.csv'), 'Sevilla|Andalucía\nGranada|Andalucía\n')
    leer_fichero_csv(absolute_path('datos/practicas_b1/provincias.csv'), '|')
    print(num_filas_csv(absolute_path('datos/practicas_b1/provincias.csv')))

    # Listas / Conjuntos
    print(suma_lista([1,2,3]))
    print(media_lista([1,2,3]))
    print(maximo_lista([3,7,2]))
    print(minimo_lista([3,7,2]))
    print(diferencias_consecutivas([5,7,10]))
    print(pares_cuadrados([1,2,3,4]))
    print(filtrar_mayores([1,5,7,2], 4))
    print(es_primo(29))
    print(divisores(12))
    print(cadena_mas_larga(['hola','adiós','murciélago']))
    print(union_listas([1,2,3],[3,4]))
    print(interseccion_listas([1,2,3],[2,3,4]))
    print(diferencia_listas([1,2,3],[2,3]))

if __name__ == '__main__':
    main()