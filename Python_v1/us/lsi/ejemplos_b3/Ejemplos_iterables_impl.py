'''
Created on 11 oct 2025

@author: migueltoro
'''

import random
from typing import TypeVar, Callable
from typing import Optional

identity = lambda x:x

R = TypeVar('R')
E = TypeVar('E')

from typing import Iterable

def aleatorios(n:int,a:int,b:int) -> Iterable[int]:
    assert a < b, f"en aleatorios: {a} debe ser menor que {b}"
    for _ in range(n):
        yield random.randint(a,b)

def iterate(initial:E, operator:Callable[[E],E], predicate:Callable[[E],bool]=lambda _:True) -> Iterable[E]:
    e = initial
    while predicate(e):
        yield e
        e = operator(e)
        
def limit(iterable:Iterable[E],limit:int) -> Iterable[E]:
    i = 0
    for e in iterable:
        if i < limit:
            yield e
            i = i +1
        else:
            break
        
def all_pairs(n:int,m:int,n0:int = 0, m0:int= 0)-> Iterable[tuple[int,int]]:
    for i in range(n0,n):
        for j in range(m0,m):
            yield (i,j)   

def distinct(iterable:Iterable[E])->Iterable[E]:
    seen:set[E] = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 
            
def flat_map(iterable:Iterable[E],key:Optional[Callable[[E],Iterable[R]]]=None) -> Iterable[R]:
    if key is None:
            key = identity
    for e in iterable:
        for pe in key(e):
            yield pe
            
def flat_map_enumerate(iterable:enumerate[E],key:Optional[Callable[[E],Iterable[R]]]=None) -> Iterable[tuple[int,R]]:
    if key is None:
        key = identity
    for ln,lv in iterable:    
        for r in key(lv):
            yield (ln,r)
            

if __name__ == '__main__':
    pass