a=[10,5,57,4,54,3,52]
print(a)

tamaño=len(a)
nuevo=[]

for _ in range(tamaño):
    may=0
    pos=0
    for i in a:
        if i>may:
            may=i

    for i in a:
        if i==may:
            break
        pos+=1

    del a[pos]
    a.append(may)
    del a[-1]
    nuevo.insert(0,may)

print(nuevo)
# [57,54,52,10,5,4,3]
