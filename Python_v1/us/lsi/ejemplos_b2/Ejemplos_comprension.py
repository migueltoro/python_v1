'''
Created on 18 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import absolute_path, encoding

def test0():
    print(encoding(absolute_path('/resources/lin_quijote.txt')))
    
def test1():
    # Forma clásica
    sr: list[int] = []
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            sr.append(t)

    # Forma por comprensión 
    s:list[int] = [x**2 for x in range(3, 70) if x % 3 == 0]
    print(s)
    print(sr)
    
    # Forma por explícita
    s2: list[int] = [3,56,78,67,45]
    print(s2)
        
def test2():
    # Forma clásica
    sts: set[int] = set()
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            sts.add(t)
    
    # Forma por comprensión     
    st:set[int] = {x**2 for x in range(3, 70) if x % 3 == 0}
    print(sts)
    print(st)
    # Forma por explícita
    st2: set[int] = {3,56,78,67,45}
    print(st2)
    
def test3():
    # Forma clásica
    dtr: dict[int,int] = {}
    for x in range(3, 70):
        if x % 3 == 0:
            t1 = x**2
            t2 = x**3
            dtr[t1] = t2

    # Forma por comprensión 
    dt:dict[int,int] = {x**2:x**3 for x in range(3, 70) if x % 3 == 0}
    print(dtr)
    print(dt)
    # Forma por explícita
    dt2: dict[int,int] = {3:56,78:67,45:45}
    print(dt2)
    
'''
Usos 
'''

    
def test4():
    nombres:list[str] = ["Miguel", "Ana", "Jose Maria", "Guillermo", "Maria", "Luisa"]
    ranking:dict[str,int] = {nombre: nombres.index(nombre) for nombre in nombres}
    print(f'ranking = {ranking}')
    

def test5():  
    texto:str = "este es un pequeño texto para probar la siguiente definicion por comprension"
    iniciales = {p[0] for p in texto.split()}
    palabras = {p for p in texto.split()}
    palabras_por_iniciales = {c: [p for p in palabras if p[0]==c] for c in iniciales}
    print(f'palabras_por_iniciales = {palabras_por_iniciales}')
    

    

if __name__ == '__main__':
    test5()
    