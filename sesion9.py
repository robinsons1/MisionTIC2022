"""

Para

El ciclo Para o For en Python nos ayuda a ejecutar dentro dentro de un rango determinado de iteraciones. 
Esto es particularmente útil cuando usamos estructuras de datos que son inherentement "ordenadas"; listas, colecciones, cadenas de caracteres, etc.

En la semana uno exploramos el tipo de dato string (una cadena de caracteres). 
Los caracteres dentro de este tipo de dato en Python puede ser recorridos con la posicion en la que se encuentran dentro de la cadena. Veamos un ejemplo:
"""

def ejemplo1():
    palabra = "Prueba"
    longitud = len(palabra)

    print("Primer ciclo")
    for i in range(longitud):
        print(palabra[i])

    print("Segundo ciclo")
    for x in "Prueba":
        print(x)
#ejemplo1()

"""
Vamos a modificar este ejemplo para conocer la longitud de la palabra y validar la ubicación de cada valor dentro de la cadena.
"""
def ejemplo2():
    palabra = "Prueba"
    longitud = len(palabra)

    print("Longitud", longitud)

    for i in range(longitud):
        print(i,palabra[i])

#ejemplo2()

def actividad1():
    print("actividad1")
    # Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.
    N=int(input("¿Cuantos numeros de la serie de Fibonacci desea imprimir?: "))-2
    A=0
    B=1
    for i in range(N):
        if i==0:
            print("0 : 0","1 : 1",sep="\n")
        C=A+B
        print(i+2,":",C)
        A=B
        B=C
#actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .
    palabra=str(input("Ingrese la palabra: "))
    P_C=len(palabra)
    print(f"El numero de letras en la palabra '{palabra}' es: {P_C}.")
    cuenta=0
    for i in palabra:
        if i=="a":
            break
        cuenta+=1
    print(f"Numero de letras en la palabra '{palabra}' hasta una 'a' es: {cuenta}.")
#actividad2()

def actividad3():
    print("actividad3")
    #Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).
    P=N=C=0
    for i in range(10):
        numero=int(input(f"Ingrese el numero {i}: "))
        if numero<0:
            N+=1
        if numero>0:
            P+=1
        elif numero==0:
            C+=1
    print("",f"Positivos: {P}",f"Negativos: {N}",f"Neutros: {C}",sep="\n")
#actividad3()

def actividad4():
    print("actividad4")
    #Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de cada número ingresado usando un ciclo Para (For).
    numero=0
    while numero!=-1:
        print()
        numero=int(input("Ingrese el numero: "))
        a=1
        for i in range(numero):
            a=a*(numero-i)
            #print(f"{a}+{numero}*({numero}-{i})")
            i+=1
        if numero!=-1:
            print(f"{numero}! = {a}")
        else:
            print("Fin del programa.")
actividad4()