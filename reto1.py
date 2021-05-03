#Reto 1
#Robinson Segura Aponte

materia_organica=float(input())
ca=float(input())

############################   Equivalencia de categorias
#SUMAMENTE APTO     -> 3
#MODERADAMENTE APTO -> 2
#MARGINALMENTE APTO -> 1
#NO APTO            -> 0

###########################       Materia organica

if materia_organica>5:
    C_materia_organica=3
elif materia_organica>=4.1 and materia_organica<=5:
    C_materia_organica=2
elif materia_organica>=3 and materia_organica<=4:
    C_materia_organica=1
elif materia_organica<3:
    C_materia_organica=0

###########################             Ca

if ca>=2 and ca<=4:
    C_ca=3
elif ca>=4.1 and ca<=8:
    C_ca=2
elif ca>=8.1 and ca<=12:
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
    salida_texto="Sumamente apto"
elif salida_numerica==2:
    salida_texto="Moderadamente apto"
elif salida_numerica==1:
    salida_texto="Marginalmente apto"
elif salida_numerica==0:
    salida_texto="No apto"

print(salida_texto)