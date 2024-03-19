import os
# 5- En una librería se almacenan los datos de x cantidad de libros, por cada libro se tiene la siguiente 
# información:
# código y stock.
# Realizar un programa que informe cuando se deba reponer stock de 
# cada libro, considerando stock mínimo = 3 libros.

libros=[0, 0, 0, 0]

lim=0

def ingresar_libros():
    codigo_libro=int(input("Ingrese el codigo del libro: "))
    cantidad_stock=int(input("Ingrese la cantidad en stock del libro: "))
    nombre_libro=input("Ingrese el nombre del libro: ")
    os.system('cls')
    libro={
        'codigo_libro':codigo_libro,
        'cantidad_stock':cantidad_stock,
        'nombre_libro':nombre_libro
    }

    return(libro)


def cargar_libro(libros, lim):
    opcion=input("¿desea cargar los datos de un libro? SI/NO: ")
    while opcion=="si" and (lim<len(libros)):
        otro_libro=ingresar_libros()
        libros[lim]=otro_libro
        lim+=1
        print()
        if lim<len(libros):
            opcion=input("¿desea cargar los datos de otro libro? SI/NO: ")
    return(lim)

def reponer(libros, limite):
    for i in range(0, limite, 1):
        if libros[i]['cantidad_stock']<=3:
         print("Es necesario reponer en stock del libro: ", libros[i]['nombre_libro'])
        else:
            print("No es necesario reponer del libro: ", libros[i]['nombre_libro'])

limite=cargar_libro(libros, lim)
reponer(libros, limite)