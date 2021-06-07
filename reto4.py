#Reto 4
#Robinson Segura Aponte

def matriz_input(veces):
    matriz=[]
    for _ in range(veces):
        datos = list(map(float, input().split(' ')))
        matriz.append(datos)
    return matriz

veces=int(input(""))

su_mo=0
su_ca=0
sumamente_apto=0
moderadamente_apto=0
marginalmente_apto=0
no_apto=0
Vmo=[]
Vca=[]

matriz_materia_organica=[]
matriz_ca=[]

may=0
maximos=[]
vector=[]

men=0
minimos=[]

matriz_materia_organica=matriz_input(veces)
matriz_ca=matriz_input(veces)

for i in range(len(matriz_ca)):
    na=sum_a=mod_a=mar_a=0
    vector=[]
    for j in range(len(matriz_ca[i])):
        materia_organica=matriz_materia_organica[i][j]
        ca=matriz_ca[i][j]

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
            sum_a+=1
        elif salida_numerica==2:
            moderadamente_apto+=1
            mod_a+=1
        elif salida_numerica==1:
            marginalmente_apto+=1
            mar_a+=1
        elif salida_numerica==0:
            no_apto+=1
            na+=1

    print(sum_a,mod_a,mar_a,na)

    vector.append(sum_a)
    vector.append(mod_a)
    vector.append(mar_a)
    vector.append(na)

    print(* vector)

    may=men=na
    if may<=mar_a: may=mar_a
    if may<=mod_a: may=mod_a
    if may<=sum_a: may=sum_a

    if men>=mar_a: men=mar_a
    if men>=mod_a: men=mod_a
    if men>=sum_a: men=sum_a

    print(f"El mayor {may} esta en la posicion {vector.index(may)}")
    print(f"El menor {men} esta en la posicion {vector.index(men)}")

    if vector.index(may)==0: maximos.append("sumamente apto")
    if vector.index(may)==1: maximos.append("moderadamente apto")
    if vector.index(may)==2: maximos.append("marginalmente apto")
    if vector.index(may)==3: maximos.append("no apto")

    if vector.index(men)==0: minimos.append("sumamente apto")
    if vector.index(men)==1: minimos.append("moderadamente apto")
    if vector.index(men)==2: minimos.append("marginalmente apto")
    if vector.index(men)==3: minimos.append("no apto")


if veces<=0:
    print("Error.")

else:

    print(no_apto,marginalmente_apto,moderadamente_apto,sumamente_apto,sep=" ")
    lon=0
    for i in maximos:
        lon+=1
        if len(maximos)>lon: print(i,end=",")
        if len(maximos)<=lon: print(i,end="")
    
    lon=0
    print()
    for i in minimos:
        lon+=1
        if len(minimos)>lon: print(i,end=",")
        if len(minimos)<=lon: print(i,end="")
        