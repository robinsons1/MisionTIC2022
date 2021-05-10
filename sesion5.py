"""
Cada ejemplo y actividad será definida como un bloque independiente.
Si-Sino-Finsi
Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 
El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

    Si (condición) Entonces
        instrucción(es)
    Sino Si
        instrucción(es)
    Fin Si

En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciónes. 
Por ejemplo:
"""

def ejemplo1():
    x = int(input("Por favor ingresa un número: "))
    if x < 0:
        print('El número es Negativo')
    elif x > 0:
        print('El número es positivo')
    elif x == 0:
        print('El número es cero')
#ejemplo1()

def actividad1():
    print("actividad1")
    #Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare

    color=input("Ingrese el color del semaforo: ")
    if color=="verde":
        print("Siga.")
    elif color=="amarillo":
        print("Precaución")
    elif color=="rojo":
        print("pare")

    return color

#col=actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
        #Verde -------- Si hay peaton - Pare, Sino - Siga
        #Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
        #Rojo = Pare

    peaton=input("¿Hay peaton?: Y/N ")
    if col=="verde" and peaton=="Y":
        print("Pare")
    elif col=="verde" and peaton=="N":
        print("Siga")
    elif col=="amarillo" and peaton=="Y":
        print("Pare")
    elif col=="amarillo" and peaton=="N":
        print("Precaución")
    elif col=="rojo":
        print("Pare")

#actividad2()

def actividad3():
    print("actividad3")
    #Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 
        #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
        #retornar el resultado de la operación indicada.
    global a, b
    a=float(input("Ingrese a: "))
    b=float(input("Ingrese b: "))
    opcion=int(input("Seleccione, 1->a+b, 2->a*b, 3->a-b, 4->a/b: "))

    if opcion==1:
        resultado=a+b
        signo="+"
    elif opcion==2:
        resultado=a*b
        signo="*"
    elif opcion==3:
        resultado=a-b
        signo="-"
    elif opcion==4:
        resultado=a/b
        signo="/"
    return signo,resultado

sig,ans=actividad3()
print(a,sig,b,"=",ans)