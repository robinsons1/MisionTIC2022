

datos = list(map(float, input().split(' ')))
longitud=len(datos)
suma=0

for i in datos:
    suma+=i
promedio=suma/longitud
promedio=round(promedio,2)

for i in datos:
    print(i, end=' ')

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
            print(f"{a} : x: {x}, y: {y}, {a[j]} > {a[i]}")
            
print(a)"""