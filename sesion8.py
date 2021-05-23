"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

La opción break, puede parar el ciclo aunque la condición sea real. Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1 
#ejemplo1()

def actividad1():
    print("actividad1")
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.
    numero=int(input("Ingrese un numero: "))
    i=0
    while i<numero:
        if i%2==0:
            print(i)
        i+=1
        if i==10:
            break
#actividad1()


"""
La opción continue, puede continuar el ciclo y saltarse cuando sea verdadera. Por ejemplo:
"""

def ejemplo2():
    i = 1
    while i < 6:
        if i == 3:
            i += 1 
            print(i)
            print("SALTA")
            continue
        print(i)
        i += 1 
#ejemplo2()

def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario pero saltarse si el digito es 4.
    numero=nu=int(input("Ingrese el numero: "))
    digitos=digitos1=cuatro=0
    num=nu%10

    while numero>0:
        numero=numero//10
        digitos+=1

    while digitos1<digitos:
        print(nu,num,digitos,digitos1,cuatro)
        if num==4:
            #nu=nu//10
            #num=nu%10
            cuatro+=1
            #continue
        nu=nu//10
        num=nu%10
        digitos1+=1
    print("Numero de digitos es: ",digitos1-cuatro)
actividad2()