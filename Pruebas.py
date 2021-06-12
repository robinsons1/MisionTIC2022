sumamente_apto=2
moderadamente_apto=1
marginalmente_apto=2
no_apto=0

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


""" print(orden1)
lista={marginalmente_apto:"marginalmente apto",moderadamente_apto:"moderadamente apto",no_apto:"no apto",sumamente_apto:"sumamente apto"}
print(lista)
cs=sorted(orden1)
print(cs)

print(f"{lista[cs[3]]} {cs[3]}")
print(f"{lista[cs[2]]} {cs[2]}")
print(f"{lista[cs[1]]} {cs[1]}")
print(f"{lista[cs[0]]} {cs[0]}") """


"""matriz=[["cali",2,3],["cali",5,6],["Bogota",8,9],["Bogota",10,12]]
print(* matriz)

for i in range(len(matriz)):
    if matriz[i][0]=="cali":
        print(matriz[i][0])

print(type(matriz[0][1]) is int)"""

"""def n_romanos():
    romanos={"a":11400,"b":12600,"c":41100,"d":14700,"e":38000}
    n=str(input("Ingrese el numero: "))
    print(romanos[n])
    print(romanos[n]*5)
n_romanos()"""

"""vector=[0,1,1,2,3,4,5]
print(vector.index(1))
"""

"""def matriz_input():
    matriz=[]
    for _ in range(3):
        datos = list(map(float, input().split(' ')))
        matriz.append(datos)
    
    print(matriz)
    
matriz_input()"""

"""a=5 if 1==21 else 0
print(a)"""

"""datos = list(map(float, input().split(' ')))
longitud=len(datos)
suma=0

for i in datos:
    suma+=i
promedio=suma/longitud
promedio=round(promedio,2)

for i in datos:
    print(i, end=' ')"""

################INGRESA DATOS CON ESPACIOS
'''
#datos = list(map(int, input().split(' ')))
#print(datos)

vector=[]

for i in range(3):
    vector.append([])
    datos = list(map(int, input().split(' ')))
    for j in range(3):
        vector[i].append(datos[j])
pprint.pp(vector)
'''

#################ORGANIZA VECTORES FORMA 2
"""a=[1,2,3,4]
print(a)
tamaño=len(a)

for i in range(len(a)):
    print("*")
    for j in range(len(a)):
        if a[j]>a[i]:
            x=a[j]
            y=a[i]
            
            a[i]=x
            a[j]=y
            #print(f"{a} : x: {x}, y: {y}, {a[j]} > {a[i]}")
            
print(a)"""