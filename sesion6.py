# Diseñar 3 opciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
#   
# Luego crea un menú con las tres opciones.

def desglosar_numero(a):

    digito1=a//1000
    digito2=(a%1000)//100
    digito3=(a%100)//10
    digito4=a%10

    return digito1,digito2,digito3,digito4

def mayor_menor(b):
    digito1,digito2,digito3,digito4=desglosar_numero(b)

    maximo=digito1
    if maximo<digito2:
        maximo=digito2
    if maximo<digito3:
        maximo=digito3
    if maximo<digito4:
        maximo=digito4

    minimo=digito2
    if minimo>digito3:
        minimo=digito3
    if minimo>digito4:
        minimo=digito4

    return maximo, minimo

def funcion1():
    numero=int(input("Ingrese un numero de 4 dijitos: "))

    maximo,minimo=mayor_menor(numero)

    if (maximo%2)==0:
        tipo="par"
    else:
        tipo="impar"

    return maximo, tipo

def funcion2():

    a=int(input("Ingrese numero 1: "))
    b=int(input("Ingrese numero 2: "))

    mayor_a,menor_a=mayor_menor(a)
    mayor_b,menor_b=mayor_menor(b)

    return mayor_a,menor_b

def funcion3():
    numero=int(input("Ingrese el numero: "))

    may,meno=mayor_menor(numero)
    a,b,c,d=desglosar_numero(numero)

    if (b==c or b==d or c==d) or (b==c and c==d):
        if b==c:
            if b<d:
                may=d
                medio=meno=b
            else:
                may=medio=b
                meno=d
        elif b==d:
            if b<c:
                may=c
                medio=meno=b
            else:
                may=medio=b
                meno=c
        elif c==d:
            if c<b:
                may=b
                medio=meno=c
            else:
                may=medio=c
                meno=b
        elif b==c and c==d:
            may=meno=medio=b
    else:
        if (may==b and meno==c) or (may==c and meno==b):
            medio=d
        elif (may==b and meno==d) or (may==d and meno==b):
            medio=c
        elif (may==c and meno==d) or (may==d and meno==c):
            medio=b

    return may,medio,meno

if __name__ == "__main__":
    opc=int(input("Seleccione una opcion del programa: "))
    if opc==1:
        max,tip=funcion1()
        print("El mayor dígito es ",max,"y es",tip) 
    if opc==2:
        may_a,men_b=funcion2()
        nuevo=str(may_a)+str(men_b)
        print("El numero es: ",nuevo)
    if opc==3:
        mayor,medio,menor=funcion3()
        nuevo=str(mayor)+str(medio)+str(menor)
        print("El numero es: ",nuevo)