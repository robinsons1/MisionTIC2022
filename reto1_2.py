# RETO 1 

Mo = float(input('ingrese el valor total de la materia organica'))
Ca = float(input('ingrese el valor del calcio disponible en el suelo'))

if Mo > 5.0:
    if Ca >= 2.0 and Ca <= 4.0:
       print('Sumamente apto') 
    if Ca >= 4.1 and Ca <= 8.0:
        print('Moderadamente apto')
    if Ca >= 8.1 and Ca <= 12.0:
        print('Marginalmente apto')
    if Ca<2 or Ca>12:
        print('No apto')
    
    
if Mo >= 4.1 and Mo <= 5.0:
    if Ca >= 2.0 and Ca <= 4.0:
       print('Moderadamente apto') 
    if Ca >= 4.1 and Ca <= 8.0:
        print('Moderadamente apto')
    if Ca >= 8.1 and Ca <= 12.0:
        print('Marginalmente apto')
    if Ca<2 or Ca>12:
        print('No apto')

if Mo >= 3.0 and Mo <= 4.0:
    if Ca >= 2.0 and Ca <= 4.0:
       print('Marginalmente apto') 
    if Ca >= 4.1 and Ca <= 8.0:
        print('Marginalmente apto')
    if Ca >= 8.1 and Ca <= 12.0:
        print('Marginalmente apto')
    if Ca<2 or Ca>12:
        print('No apto')
    
if Mo<3:
    if Ca >= 2.0 and Ca <= 4.0:
       print('No apto') 
    if Ca >= 4.1 and Ca <= 8.0:
        print('No apto')
    if Ca >= 8.1 and Ca <= 12.0:
        print('No apto')
    if Ca<2 or Ca>12:
        print('No apto')