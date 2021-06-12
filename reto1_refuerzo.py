import math

areas={"a":11400,"b":12600,"c":41100,"d":14700,"e":38000}

area =  float(input())
ant_old = int(input())
type_new = input()
area_old =  ant_old*4800

if type_new=="a" or type_new=="b" or type_new=="c" or type_new=="d" or type_new=="e": 
    if ant_old >= 0:
        print(max(0,math.ceil((area-area_old)/areas[type_new])))
    else:
        print('error en los datos')
else:
    print('error en los datos')

