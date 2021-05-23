"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
En Python, definimos una función con la siguiente estructura

def funcion(parametros)

Recuerda que los parametros son opcionales!
"""

def suma(a,b):
    
    print(a+b)
#suma(3,4)


#Actividad 1
#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar

def imprimaProducto(nombre, precio):
    print(f"Producto: {nombre}.",f"Valor: {precio}",sep="\n")

def caja():
    i="S"
    total=0
    while i=="S":
        nombre=str(input("\nNombre del producto: "))
        precio=float(input("Precio: "))
        total+=precio
        imprimaProducto(nombre,precio)
        i=str(input("¿Desea ingresar otro producto?: S/N "))
    print(f"\nTotal: {total}")
#caja()

#Actividad 2
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.

import random

def numeros():
    i=0
    par=1
    impar=0
    while i<10:
        while par!=0:
            N=random.randint(0, 100)
            if N%2==0:
                par=0
                impar=1
        print(N)
        i+=1
        while impar!=0:
            N=random.randint(0, 100)
            if N%2!=0:
                par=1
                impar=0
        print(N)
        i+=1

def numAleatorio():
    i=0
    while i!=1:
        N=random.randint(100, 130)
        if N!=110 and N!=115 and N!=120:
            i=1
    print(N,"\n")
    numeros()
numAleatorio()