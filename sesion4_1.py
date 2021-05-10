#mayor de 3 numeros

a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))
c=int(input("Ingrese c: "))

'''
#                                FORMA 1
if a>b and a>c:
    mayor=a
elif b>a and b>c:
    mayor=b
else:
    mayor=c

print("Mayor es: ",mayor)
'''

#                                 FORMA 2
maximo=a

if maximo<b:
    maximo=b
if maximo<c:
    maximo=c

print("Mayor es: ",maximo)