import pprint

def matriz_input():
    matriz=[]
    for _ in range(10):
        datos = list(map(float, input().split(' ')))
        matriz.append(datos)
    return matriz

print("Ingrese la matriz de asignacion: ")
m_asig=matriz_input()

print("Ingrese la matriz de registro: ")
m_reg=matriz_input()

print()
print("MATRIZ DE ASIGNACION: ")
pprint.pp(m_asig)
print()
print("MATRIZ DE REGISTRO: ")
pprint.pp(m_reg)

print()
eficiencia=[]
tasa_entrega=[]
cumplimiento=[]
entrega_a_tiempo=0

for i in range(10):
    ################ EFICIENCIA
    ef=[]
    e=((m_asig[i][2]-m_reg[i][2])/(m_asig[i][2]))*100 if m_asig[i][2]>=0 and m_reg[i][2]>=0 else 0
    ef.append(m_asig[i][1])
    ef.append(round(e,2))
    eficiencia.append(ef)

    ################ TASA ENTREGA
    t_e=[]
    te=(((m_reg[i][3])/(m_reg[i][2]))*100) if m_reg[i][3]>=0 and m_reg[i][2]>=0 else 0
    t_e.append(m_asig[i][1])
    t_e.append(round(te,2))
    tasa_entrega.append(t_e)

    ############### CUMPLIMIENTO
    cum=[]
    c=(((m_reg[i][3])/(m_asig[i][3]))*100) if m_reg[i][3]>=0 and m_asig[i][3]>=0 else 0
    cum.append(m_asig[i][1])
    cum.append(round(c,2))
    cumplimiento.append(cum)

    ############# ENTREGAS A TIEMPO
    if m_asig[i][2]<m_reg[i][2] and m_asig[i][2]>=0 and m_reg[i][2]>=0: entrega_a_tiempo+=1 


print("MATRIZ DE EFICIENCIA: ")
pprint.pp(eficiencia)
print()
print("MATRIZ TASA ENTREGA (l/min): ")
pprint.pp(tasa_entrega)
print()
print("MATRIZ DE CUMPLIMIENTO: ")
pprint.pp(cumplimiento)
print()
print(f"ENTREGAS A TIEMPO: {entrega_a_tiempo*10}%")