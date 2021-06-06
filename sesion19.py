"""
Manejo de archivos

Continuemos ahora con otras opciones como escribir y actualizar un archivo desde Python.

Recordemos las opciones disponibles para el manejo de archivos.
Modo 	Descripción
'r' 	Abrir el archivo en modo lectura, este es el valor por defecto
'w' 	Abrir el archivo para escritura, eliminará cualquier archivo existente con el mismo nombre
'x' 	Crear el archivo, si existe uno con el mismo nombre sacará un error
'a' 	Abrir el archivo para escribir. Todo lo escrito se adicionará al final del archivo
'b' 	Abrir en modo binario
't' 	Abrir en modo texto, este es el valor por defecto
'+' 	Abrir para lectura y escritura

Empecemos creando un archivo de texto llamado minuevoarchivo.txt. 
"""
def ejemplo1():
    nuevoArchivo = open('minuevoarchivo.txt', mode='a', encoding='utf-8-sig' )
    nuevoArchivo.write("Escribiendo desde Python\n")
#ejemplo1()

#Ahora vamos a crear un diccionario y a imprimir todos los valores y el valor almacenado con la clave 2
def ejemplo2():
    diccionario = { 1 : 'lunes', 2:'martes', 3:'miercoles', 4:'jueves', 5:'viernes', 6:'sabado', 7:'domingo'}

    print(diccionario)
    print(diccionario[2])
#ejemplo2()

# Actividad 1
#
# Vamos a elaborar un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano usando un diccionario como lo definimos anteriormente. 
def n_romanos():
    romanos={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",1:"X"}
    n=int(input("Ingrese el numero: "))
    print(romanos[n]) if 0<n<=10 else print("Fuera de rango")
#n_romanos()

#Actividad 2 
#Recordemos una de las actividades que hicimos en sesiones anteriores.
#
#Diseña un programa con las siguiente características:
#
#    Que tenga una función caja que 
#       a. Cree un archivo recibo.txt
#       b. Solicite al usuario nombre y precio de cada producto.
#       d. Una función adicional llamada guardaProducto(nombre, precio, archivo) que reciba el nombre y el precio de cada producto y los escriba en el archivo recibo.txt.
#       e. Que después de llamar a guardaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    Al final de tus funciones, puedes simplemente llamar a la función caja para probar

def guardaProducto(nombre, precio):
    Archivo = open('recibo.txt', 'a')
    Archivo.write(f"{nombre}:{precio}\n")

def caja():
    open('recibo.txt', mode='w', encoding='utf-8-sig' )
    Archivo=open('recibo.txt', "a")
    i="S"
    total=0
    while i=="S":
        nombre=str(input("\nNombre del producto: "))
        precio=float(input("Precio: "))
        total+=precio
        guardaProducto(nombre,precio)
        i=str(input("¿Desea ingresar otro producto?: S/N "))
    Archivo.write(f"Total={total}")
    print(f"\nTotal: {total}")
    Archivo.close()
caja() 