"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1
#ejemplo1()

def actividad1(): # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 
    print("actividad1")
    numero=int(input("Ingrese un numero: "))
    i=2
    while i<=numero:
        if (i%2)==0:
            print(i)
        i += 1
#actividad1()

def actividad2():  #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.
    print("actividad2")
    numero=int(input("Ingrese el numero: "))
    i=1
    digitos=0
    while i>0:
        division=numero//(10*i)
        #print(numero,"//",10*i,"=",division)
        digitos+=1
        i*=10
        if division<=0:
            i=-1 
    print("Numero de digitos es: ",digitos)
#actividad2()    
    
def actividad3():
    print("actividad3")
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).
    numero=int(input("Ingrese el numero: "))
    i=1
    suma=numero
    while numero!=-1:
        numero=int(input("Ingrese el numero: "))
        if numero!=-1:
            suma+=numero
            i+=1
    promedio=suma/i
    print("Promedio: ",promedio)
#actividad3()