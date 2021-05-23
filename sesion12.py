"""
Funciones con listas

Aquí van algunas funciones útiles cuando trabajamos con listas.

    remove(x) - remueve el primer valor X de la lista
    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
    len(x) - permite calcular el tamaño de una lista
"""
def ejemplo1():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))
#ejemplo1()

"""
Como vemos, append(x) inserta el valor x al final de la lista.

Pero también existe la función insert(pos, x) que nos permite insertar x en la posición pos. 

Veamos un ejemplo
"""
def ejemplo2():
    a = [1, 3, 2, 5, 2]
    a.insert(4,8)
    print(a)
#ejemplo2()

#Actividad 1

#Escribamos un programa que nos permita crear con una lista de 6 números aleatorios entre 1 y 20, 
#y luego creemos tres funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
#    orden(x) - Una función que ordene los datos de una lista x ascendentemente y la imprima en orden

import random

def mayor(a):
    may=0
    pos=0
    for i in a:
        if i>may:
            may=i
    for i in a:
        if i==may:
            break
        pos+=1
    return may,pos

def primos(a):
    prim=[]
    for i in a:
        div=0
        for x in range(1,i+1):
            divisor=i%x
            if divisor==0:
                div+=1
        if div==2:
            prim.append(i)
    return prim

def orden(a):
    tamaño=len(a)
    nuevo=[]
    for _ in range(tamaño):
        for _ in a:
            N_mayor,pos=mayor(a)
            del a[pos]
            nuevo.insert(0,N_mayor)
    return nuevo

def actividad2():
    aleatorios=[]
    for i in range(6):
        aleatorios.append(random.randint(1, 20))
    print(f"Lista: {aleatorios}")
    sup,pos=mayor(aleatorios)
    print(f"El numero mayor es {sup} y esta en la posicion {pos}")
    N_primos=primos(aleatorios)
    print(f"Numeros primos: {N_primos}")
    ordenado=orden(aleatorios)
    print(f"Lista ordenada: {ordenado}")
actividad2()