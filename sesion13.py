"""
Matrices o vectores bidimensionales

En Python podemos trabajar los arreglos bidimensionales como listas de listas, es decir, cada elemento de la lista es una lista.

Nota Existe una librería en Python que maneja tanto vectores como matrices llamada numpy. 
Esta librería está por fuera del alcance de este curso pero puedes investigarla.

Veamos un ejemplo:
"""

def ejemplo1():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    print(a)
#ejemplo1()

#O podemos recorrer todos los elementos e imprimir como una matriz
def ejemplo2():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
#ejemplo2()

#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.

import random
import pprint

def actividad1():
    vector=[]
    may=0
    
    for i in range(5):
        vector.append([])
        for j in range(10):
            vector[i].append(random.randint(1, 100))
    pprint.pp(vector)

    men=vector[0][0]
    pos_m=[0,0]

    for i in range(len(vector)):
        for j in range(len(vector[i])):
            if vector[i][j]>may:
                may=vector[i][j]
                pos_M=[i,j]
            if vector[i][j]<men:
                men=vector[i][j]
                pos_m=[i,j]
    
    print()
    print(f"Numero mayor es {may} y esta en la posicion {pos_M}")
    print(f"Numero menor es {men} y esta en la posicion {pos_m}")          
#actividad1()

#Actividad 2
#
#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

def escalar(matriz, escalar):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=matriz[i][j]*escalar
    pprint.pp(matriz)
    
def actividad2():
    vector=[]

    m=int(input("Tamaño m de la matriz: "))
    n=int(input("Tamaño n de la matriz: "))
    escala=int(input("Escalar: "))

    for i in range(m):
        vector.append([])
        for j in range(n):
            vector[i].append(random.randint(1, 100))
    print("Matriz: ")
    pprint.pp(vector)

    print("")
    print(f"Matriz * {escala}: ")
    escalar(vector,escala)

actividad2()