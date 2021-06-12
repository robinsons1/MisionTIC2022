#Reto 5
#Robinson Segura Aponte

import csv
#import pprint

def mayor_menor(matriz,col):
    may=0
    men=1000
    for i in range(len(matriz)):
        if float(matriz[i][col])>may: may=float(matriz[i][col])
        if float(matriz[i][col])<men: men=float(matriz[i][col])
    return may,men

city=input()

archivo1=open('data.csv', "r")
lector=csv.reader(archivo1)
matriz=[]
ciudad=[]
a=prom_mo=prom_ca=0
suma_mo=suma_ca=0
sumamente_apto=0
moderadamente_apto=0
marginalmente_apto=0
no_apto=0

for fila in lector:             #ELIMINAR COLUMNAS INNECESARIAS
    x=fila.pop(6)
    x=fila.pop(4)
    x=fila.pop(2)
    x=fila.pop(1)
    matriz.append(fila)

for i in matriz:                #GUARDAR EN UNA MATRIZ LOS DATOS DE LA CIUDAD NECESARIA
    if matriz[a][0]==city: 
        ciudad.append(i)
    a+=1

for i in range(len(ciudad)):    #SUMAR COLUMNAS PARA OBTENER PROMEDIOS
    suma_mo+=float(ciudad[i][1])
    suma_ca+=float(ciudad[i][2])

prom_mo=suma_mo/len(ciudad)
prom_ca=suma_ca/len(ciudad)

mayor_mo,menor_mo=mayor_menor(ciudad,1)
mayor_ca,menor_ca=mayor_menor(ciudad,2)

for i in range(len(ciudad)): 
    materia_organica=float(ciudad[i][1])
    ca=float(ciudad[i][2])

    ############################   Equivalencia de categorias
    #SUMAMENTE APTO     -> 3
    #MODERADAMENTE APTO -> 2
    #MARGINALMENTE APTO -> 1
    #NO APTO            -> 0

    ###########################       Materia organica

    if materia_organica>5:
        C_materia_organica=3
    elif materia_organica>4 and materia_organica<=5:
        C_materia_organica=2
    elif materia_organica>=3 and materia_organica<=4:
        C_materia_organica=1
    elif materia_organica<3:
        C_materia_organica=0

    ###########################             Ca

    if ca>=2 and ca<=4:
        C_ca=3
    elif ca>4 and ca<=8:
        C_ca=2
    elif ca>8 and ca<=12:
        C_ca=1
    elif ca<2 or ca>12:
        C_ca=0

    #########################              Salida

    if C_materia_organica==C_ca:
        salida_numerica=C_materia_organica
    elif C_materia_organica<C_ca:
        salida_numerica=C_materia_organica
    elif C_materia_organica>C_ca:
        salida_numerica=C_ca

    if salida_numerica==3:
        sumamente_apto+=1
    elif salida_numerica==2:
        moderadamente_apto+=1
    elif salida_numerica==1:
        marginalmente_apto+=1
    elif salida_numerica==0:
        no_apto+=1

#pprint.pp(ciudad)

print("{0:.2f}".format(prom_mo),end=' ')
print("{0:.2f}".format(prom_ca),end=' ')
print()
print(menor_mo,menor_ca)
print(mayor_mo,mayor_ca)

#ORGANIZA ALFANUMERICAMENTE
diccionarios_coches = [
        {'categoria': 'marginalmente apto', 'repeticion': marginalmente_apto},
        {'categoria': 'moderadamente apto', 'repeticion': moderadamente_apto},
        {'categoria': 'no apto', 'repeticion': no_apto},
        {'categoria': 'sumamente apto', 'repeticion': sumamente_apto}
]
ordenados = sorted(diccionarios_coches, reverse=True,key=lambda coche : coche['repeticion'])

a=ordenados[0]
b=ordenados[1]
c=ordenados[2]
d=ordenados[3]

print(a["categoria"],a["repeticion"])
print(b["categoria"],b["repeticion"])
print(c["categoria"],c["repeticion"])
print(d["categoria"],d["repeticion"])