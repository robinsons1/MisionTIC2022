#Reto 2
#Robinson Segura Aponte

veces=int(input(""))
su_mo=0
su_ca=0
sumamente_apto=0
moderadamente_apto=0
marginalmente_apto=0
no_apto=0

for i in range(veces):

    materia_organica=float(input(""))
    ca=float(input(""))

    su_mo+=materia_organica
    su_ca+=ca

    if i==veces-1:
        pro_mo=su_mo/veces
        pro_ca=su_ca/veces

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

if veces<=0:
    print("Error.")
else:
    print("{0:.2f}".format(pro_mo))
    print("{0:.2f}".format(pro_ca))

    print("sumamente apto",sumamente_apto)
    print("moderadamente apto",moderadamente_apto)
    print("marginalmente apto",marginalmente_apto)
    print("no apto",no_apto)

