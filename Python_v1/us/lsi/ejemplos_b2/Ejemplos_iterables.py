'''
Created on 11 oct 2025

@author: migueltoro

'''

from typing import Iterable
from us.lsi.tools.Iterable import distinct, flat_map, iterate
from us.lsi.tools.File import absolute_path, iterable_de_fichero, iterable_de_csv
from itertools import accumulate
from operator import mul
import re

'''
Comparación entre la forma clásica , explícita y por comprensión de definir colecciones

'''
    
def test1():
    # Forma clásica
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            print(t)
    # Forma por comprensión   
    r:Iterable[int] = (x**2 for x in range(3, 70) if x % 3 == 0)
    print('________________________________________')
    print(r)
    for e in r:
        print(e)
    
    # Forma por explícita
   
    r2: Iterable[int] = (3,56,78,67,45) # En realidad es una tupla que como sabemos es iterable
    print('________________________________________')
    print(r2)
    for e in r2:
        print(e)
        
'''
Funciones para transformar iterables

    map(f,it)  aplica la función f a cada elemento del iterable it
    filter(p,it)  selecciona los elementos del iterable it que cumplen el predicado p
    distinct(it) elimina los elementos repetidos del iterable it
    sorted(it,key) ordena los elementos del iterable it según la función key
    flat_map(it,key)  aplica la función key a cada elemento del iterable it y concatena los resultados
    flat_map_enumerate(it,key) como flat_map pero el iterable it es un enumerate y key se aplica al segundo elemento de la tupla
    zip(it1,it2,...)  crea un iterable de tuplas a partir de los iterables it1,it2,...
    enumerate(it) crea un iterable de tuplas (i,e) donde i es el índice del elemento e en el iterable it
    accumulate(it,f) crea un iterable con los resultados parciales de aplicar la función f a los elementos del iterable it
    iterate(x0,f,p) crea un iterable que comienza en x0 y genera los siguientes elementos aplicando la función f mientras se cumple el predicado p
    limit(it,n) crea un iterable con los n primeros elementos del iterable it
    skip(it,n) crea un iterable sin los n primeros elementos del iterable it
    take_while(it,p) crea un iterable con los elementos del iterable it mientras se cumple el predicado p
    drop_while(it,p) crea un iterable sin los elementos del iterable it mientras se cumple el predicado p
    first_and_rest(it) devuelve una tupla con el primer elemento del iterable it y un iterable con el resto de elementos o None si está vacío    

'''    
        
def test7():
    fichero:str= absolute_path("datos/datos_3.txt")
    it3:Iterable[list[str]] = iterable_de_csv(fichero)
    it4:Iterable[str] = flat_map(it3)
    it5:Iterable[int] = map(lambda e:int(e),it4)
    it6:Iterable[int] = distinct(it5)
    r0:list[int] = sorted(it6,key=lambda x:x)
    print(f'sorted = {r0}')
    
def test8():
    r7:Iterable[str] = flat_map(iterable_de_fichero(absolute_path("datos/datos_3.txt")),key=lambda ln: re.split(',',ln))
    print(list(r7))
    print('________________')
    r8:Iterable[str] = flat_map(iterable_de_csv(absolute_path('resources/lin_quijote.txt'), encoding='ISO-8859-1',delimiter=' '))
    r9:Iterable[str] = filter(lambda x: len(x)>0,r8)
    print(list(r9))
    
def test9():
    cadena:str = "lunes,martes,miercoles,jueves,viernes,sabado,domingo"
    it7:Iterable[tuple[int,str]] = enumerate(cadena)
    it8:Iterable[tuple[int,str]] = filter(lambda e:e[0]%2==0,it7)
    it9:Iterable[str] = map(lambda e: e[1],it8)
    print(list(it9))
    
def test10():
    a:int = 0
    b:int = 200
    c:int = 5
    d:int = 4
    it1:Iterable[int] = map(lambda x:x**2,range(a,b,c))
    it2:Iterable[int] = filter(lambda x:x%d==0, it1)
    print(list(it2))
    
def test11():
    versions:list[int] = [14, 3, 6]
    r5:Iterable[int] = accumulate(versions,mul)
    print(list(r5))
    
def test12():
    r6:Iterable[int] = iterate(3,lambda x:x*7,lambda x: x<1000)
    print(f'Iterate = {list(r6)}')
    
def test13():
    languages:list[str] = ['Java', 'Python', 'JavaScript']
    versions:list[int] = [14, 3, 6]   
    r1:Iterable[tuple[str,int]] = zip(languages, versions)
    print(list(r1))
    dias:list[str] = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
    r2:Iterable[tuple[int,str]] = enumerate(dias)
    r3:list[tuple[int,str]] = list(r2)
    print(list(r3))
    r4:dict[int,str]  = dict(r3)
    print(r4)
        

if __name__ == '__main__':
    pass