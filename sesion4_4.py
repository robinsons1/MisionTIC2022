temperatura=int(input("Ingrese temperatura: "))

if -10<=temperatura<10:
    print("Mucho frio")
elif 10<=temperatura<15:
    print("Poco frio")
elif 15<=temperatura<25:
    print("Temperatura normal")
elif 25<=temperatura<30:
    print("Poco calor")
elif 30<=temperatura<45:
    print("Mucho calor")
else:
    print("Fuera de parametros")
