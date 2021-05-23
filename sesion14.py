"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""

#Actividad 1

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"

#actividad1([[1,1],[2,7,2],[3,3,3]])

import random
import pprint

def actividad1():
    vector=[]

    m=int(input("Tamaño m de la matriz: "))
    n=int(input("Tamaño n de la matriz: "))

    for i in range(m):
        vector.append([])
        for j in range(n):
            vector[i].append(random.randint(1, 100))
    print("Matriz: ")
    pprint.pp(vector)

    if m==n:
        for i in range(len(vector)):
            for j in range(len(vector[i])):
                if i==j:
                    print(vector[i][j])
    else:
        print("La matriz no es cuadrada. ")
#actividad1()

#Actividad 2
#
#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc

def actividad2():
    vector=[]

    for i in range(3):
        vector.append([])
        datos = list(map(int, input("Ingrese los datos de la fila: ").split(' ')))
        for j in range(3):
            vector[i].append(datos[j])
    pprint.pp(vector)
    
    print()
    print("Primera fila: ")
    for i in range(len(vector)):
            for j in range(len(vector[i])):
                if i==0:
                    print(vector[i][j])

    print()
    print("Primera columna: ")
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            if j==0:
                print(vector[i][j])

    print()
    print(f"Elemento en la posicion 1,1: {vector[1][1]}")
actividad2()