'''
Created on 22 sept 2022

@author: migueltoro
'''
from functools import reduce
from typing import TypeVar, Callable,Iterable
from us.lsi.tools.Iterable import count_if, first_index_if, distinct, first
from fractions import Fraction
from statistics import mean
from us.lsi.tools.File import lineas_de_csv, lineas_de_fichero,absolute_path,encoding, iterable_de_fichero
import re
from math import sqrt

E = TypeVar('E')

'''
Acumuladores
    sum(it) suma los elementos del iterable it
    min(it,key) minimo de los elementos del iterable it según la función key
    max(it,key) máximo de los elementos del iterable it según la función key
    any(it) True si algún elemento del iterable it es True
    all(it) True si todos los elementos del iterable it son True
    all_different(it) True si todos los elementos del iterable it son distintos
    mean(it) media de los elementos del iterable it
    tolist(it) convierte el iterable it en una lista
    toset(it) convierte el iterable it en un conjunto
    reduce(f,it) aplica la función f a los elementos del iterable it de forma acumulativa
    first(it,p) devuelve el primer elemento del iterable it que cumple el predicado p
    count_if(it,p) cuenta los elementos del iterable it que cumplen el predicado p
    first_index_if(it,p) devuelve el índice del primer elemento del iterable it que cumple el predicado p o -1 si no existe
    first_and_last(it) devuelve una tupla con el primer y el último elemento del iterable it o None si está vacío
       
    grouping_reduce(it,key,op,value,andThen) agrupa los elementos del iterable it según la función key y aplica 
        la función op a los valores obtenidos aplicando la función value a cada elemento. 
        Si se proporciona la función andThen se aplica a los resultados de op
    grouping_list(it,key,value,andThen) agrupa los elementos del iterable it según la función key y crea
        una lista con los valores obtenidos aplicando la función value a cada elemento.
        Si se proporciona la función andThen se aplica a las listas obtenidas
    grouping_set(it,key,value,andThen) agrupa los elementos del iterable it según la función key y crea
        un conjunto con los valores obtenidos aplicando la función value a cada elemento.
        Si se proporciona la función andThen se aplica a los conjuntos obtenidos
    groups_size(it,key,value) agrupa los elementos del iterable it según la función key y cuenta
        los valores obtenidos aplicando la función value a cada elemento
    join(it1,it2,key1,key2) une los elementos de los iterables it1 e it2 según las funciones key1 y key2
    str_iter(it,sep,prefix,suffix,key) devuelve una cadena con los elementos del iterable it separados por sep, 
        con prefijo prefix y sufijo suffix y aplicando la función key a cada elemento
    str_dict(d,key1,key2,sep,prefix,suffix) como str_iter pero para diccionarios
    str_set(s,sep,prefix,suffix,key) como str_iter pero para conjuntos
    str_list(l,sep,prefix,suffix,key) como str_iter pero para listas
    str_tuple(t,sep,prefix,suffix,key) como str_iter pero para tuplas
    
'''

dias = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]

texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

square = {2: 4, -3: 9, -1: 1, -2: 4}

key2 = max(square, key = lambda k: square[k])

def tolist(iterable:Iterable[E])->list[E]:
    ls= []
    for e in iterable:
        ls.append(e)
    return ls

def toset(iterable:Iterable[E])->set[E]:
    st : set[E]= set()
    for e in iterable:
        st.add(e)
    return st

def test1():
    print(sum((Fraction(51, 5), Fraction(25, 2), Fraction(59, 5))))
    print(mean((2, 3, 4, 2, 3, 6, 4, 2)))
    print(sorted(dias, key=len))
    print(reduce(lambda x,y: x*y,range(2,30,5)))
    
def test2():
    es:set[str] = set()
    print(reduce(lambda s,e: s | {e}, texto, es))
    print(max(dias,key=lambda x:len(x)))
    print(any((e%13==0 for e in range(2,341,5))))
    print(all((e%2==0 for e in range(2,341,5))))
    print(first(e for e in range(2,341,5) if e%13==0))
    
def test3():
    print("Apariciones de la letra a:", count_if(texto,lambda e:e=="a"))
    print("Primera aparicion de la letra a:",first_index_if(texto,lambda e:e=="a"))
    print(count_if(distinct(texto)))
    
def media(ls:list[int]) -> float:
    a = (0,0)
    for e in ls:
        a = (a[0]+e,a[1]+1)
    assert a[1]>0,'La lista esta vacia'
    return a[0]/a[1]

def desviacion_tipica(ls:list[int]) -> float:
    a = (0.,0.,0)  #(sum x^2, sum x, num elem)
    for e in ls:
        a = (a[0]+e*e,a[1]+e,a[2]+1)
    assert a[2]>0,'La lista esta vacia'
    return sqrt(a[0]/a[2]-(a[1]/a[2])**2) 

def suma_aritmetica(a:int,b:int,c:int)->int:
    s = 0
    for e in range(a,b,c):
        s = s + e
    return s

def suma_primeros(m:int,n:int)->int:
    i = 0;
    a = 0
    for e in range(m):
        if i < n:
            a = a + e
        else:
            break
        i = i +1
    return a

def test4():
    a,b,c = 2,500,7
    print(f"La suma de la progresion aritmetica de {a} a {b} con razon {c} es {suma_aritmetica(a,b,c)}")
    m,n=10000000, 10
    print(f'Suma de los primeros {n} numeros de la secuencia 0 a {m} es {suma_primeros(m, n)}')

def numero_de_lineas(file: str) -> int:
    return len(lineas_de_fichero(file,encoding='utf-16'))

def numero_de_palabras_distintas(file: str,encoding:str) -> int:
    sep = r'[ ,;.\n():?!\"]'
    lns = lineas_de_fichero(file,encoding=encoding)
    s = 0
    for linea in lns:
        for _ in re.split(sep, linea):
            s = s+1
    return s

def num_caracteres_no_delimitadores(file:str,encoding:str):
    sep = r'[ ,;.\n():?!\"]'
    lineas:Iterable[str] = iterable_de_fichero(file, encoding=encoding)
    n:int = 0
    for ln in lineas:
        for p in re.split(sep,ln):
            for _ in p:
                n = n+1
    return n

def lista_de_fichero(file:str,encoding:str,delim:str)->list[int]:
    lns:list[list[str]] = lineas_de_csv(file,encoding=encoding,delimiter=delim)
    r:list[int] = []
    for linea in lns:
        for p in linea:
            if len(p) > 0:
                r.append(int(p))  
    return r

def suma_elementos_fichero_if(file:str,encoding:str,pd:Callable[[int],bool])->int:
    lns:list[str] = lineas_de_fichero(file,encoding=encoding)
    r:int = 0
    for linea in lns:
        for p in re.split(',', linea):
            if len(p) > 0:
                e = int(p)
                if pd(e):
                    r = r + e 
    return r

def test5():
    print(encoding(absolute_path('resources/quijote.txt')))
    print(encoding(absolute_path('resources/lin_quijote.txt')))
    print(lista_de_fichero(absolute_path('datos/datos_2.txt'),encoding='utf-8',delim=","))
    
def test6():
    print(num_caracteres_no_delimitadores(absolute_path('resources/quijote.txt'),encoding='utf-16'))
    print(numero_de_palabras_distintas(absolute_path('resources/quijote.txt'),encoding='utf-16'))
    

if __name__ == '__main__':
    test3()
    
