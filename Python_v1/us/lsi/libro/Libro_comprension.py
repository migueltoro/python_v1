'''
Created on 25 jul. 2020

@author: migueltoro
'''

from typing import Iterable,Optional
from us.lsi.tools.File import lineas_de_fichero, encoding, absolute_path, iterable_de_fichero
from us.lsi.tools.Dict import str_dict, dict_invert_set
from us.lsi.tools.Iterable import flat_map,first,distinct,str_iter,grouping_set,count,\
    flat_map_enumerate
from collections import Counter
import re
from statistics import mean

sep = r'[^\wáéíóúÁÉÍÓÚñÑ]+'

def palabras_huecas() -> set[str]:
    lns:list[str] = lineas_de_fichero(absolute_path("resources/palabras_huecas.txt"))
    return {p for p in lns}

def lineas_de_libro(file: str) -> Iterable[str]:
    return iterable_de_fichero(file,encoding='utf-16')

def palabras_no_huecas(file: str) -> Iterable[str]:
    huecas:set[str] = palabras_huecas()
    lns:Iterable[str] = lineas_de_libro(file)
    pls:Iterable[str] = flat_map(lns,lambda x: re.split(sep, x))
    palabras:Iterable[str] = (p for p in pls if p not in huecas and len(p) > 0)
    return palabras

def palabras_no_huecas_distintas(file: str) -> Iterable[str]:
    return distinct(palabras_no_huecas(file))

def palabras_lineas(file:str) -> Iterable[tuple[int,str]]:
    lns:Iterable[str] = (ln for ln in lineas_de_libro(file) if len(ln) > 0)
    pl:Iterable[tuple[int,str]]  = flat_map_enumerate(enumerate(lns), key=lambda linea:re.split(sep,linea))
#    pl:Iterable[tuple[int,str]] = ((i,p) for i,linea in enumerate(lns) for p in re.split(sep,linea) if len(p) > 0) 
    return pl

def numero_de_lineas(file: str) -> int:
    return count(lineas_de_libro(file))

def numero_de_palabras_no_huecas(file:str) -> int:
    return count(palabras_no_huecas(file)) 

def numero_de_palabras_distintas_no_huecas(file:str) -> int:    
    return count(palabras_no_huecas_distintas(file))           

def longitud_media_de_lineas(file:str) -> float:
    return mean(len(ln) for ln in lineas_de_fichero(file))

def numero_de_lineas_vacias(file:str) -> int:
    return count(ln for ln in lineas_de_libro(file) if len(ln) == 0)

def linea_mas_larga(file:str) -> str:
    return max(lineas_de_libro(file), key= lambda x:len(x))

def primera_linea_con_palabra(file:str,palabra:str) -> Optional[str]:
    return first(lineas_de_libro(file),p=lambda ln:palabra in ln)

def linea_numero(file:str,n:int) -> Optional[str]:
    r:Optional[tuple[int,str]] = first(enumerate(lineas_de_libro(file)),p=lambda p:p[0] == n)
    return r[1] if r else None

def frecuencias_de_palabras(file:str) -> dict[str,int]:
    d: Counter[str] = Counter(palabras_no_huecas(file))
    return dict(sorted(d.items(), key=lambda t: t[1], reverse=True))

def palabras_por_frecuencias(file:str) -> dict[int,set[str]]:
    d:dict[int,set[str]] = dict_invert_set(dict(frecuencias_de_palabras(file)))
    return dict(sorted(d.items(), key=lambda t: t[0]))
 
def palabra_en_lineas(file:str) -> dict[str,set[int]]:
    palabras:Iterable[tuple[int,str]] = palabras_lineas(file)
    d:dict[str,set[int]] = grouping_set(palabras,key=lambda e: e[1], value=lambda e: e[0])
    return dict(sorted(d.items(), key=lambda t: t[0]))

def palabras_frecuentes(file:str, k:int)->list[str]:
    return [p for p,_ in Counter(palabras_no_huecas(file)).most_common(k)]

def test1():
    print(encoding(absolute_path("resources/quijote.txt")))
    print(str_iter(palabras_no_huecas(absolute_path("resources/quijote.txt")),sep='\n'))
    print(str_dict(palabras_por_frecuencias(absolute_path("resources/quijote.txt")),sep='\n'))
    
def test2():
    print(numero_de_palabras_distintas_no_huecas(absolute_path("resources/quijote.txt")))
    
def test3():
    print(str_iter(palabras_por_frecuencias(absolute_path("resources/quijote.txt")).items(),sep='\n',prefix='',suffix=''))
 
def test4():  
    print(str_iter(palabra_en_lineas(absolute_path("resources/quijote.txt")).items(),sep='\n',prefix='',suffix=''))

def test5():
    print(palabras_frecuentes(absolute_path("resources/quijote.txt"), 10))
    
def test6():
    file:str = absolute_path("resources/quijote.txt")
    f:dict[str,int]=frecuencias_de_palabras(file)
    d:dict[str,int] = {k: v for k, v in f.items() if v>100}
    print(str_dict(d,sep='\n'))
     
if __name__ == '__main__':
    test6()
#    print(palabras_huecas())
    
    
    
    
    