# 3- Se tiene una clase de 30 estudiantes, para c/u se almacenan los siguientes datos:
# - Nro_estudiante
# - Nombre

# tambein Se pide:
# a- Lista de alumnos con sus respectivas notas ordenados alfabéticamente.
# b- Nro. de estudiante con mayor nota.
# c- Nombre de estudiante de menor nota.
# d- Nota que obtuvo la alumna Laura Suárez.

import os

alumnos=[0, 0, 0, 0]

lim=0

buscado="laura suarez"

def ingresar_alumnos():
    numero_estudiante=int(input("Ingrese el numero del estudiante: "))
    nombre_estudiante=input("Ingrese el nombre del estudiante: ")
    nota_estudiante=int(input("Ingrese la nota del estudiante: "))
    os.system('cls')
    alumno={
        'numero_estudiante':numero_estudiante,
        'nombre_estudiante':nombre_estudiante,
        'nota_estudiante':nota_estudiante
    }

    return(alumno)


def cargar_estudiantes(alumnos, lim):
    opcion=input("¿desea cargar los datos de un estudiante? SI/NO: ")
    while opcion=="si" and (lim<len(alumnos)):
        nuevo_alumno=ingresar_alumnos()
        alumnos[lim]=nuevo_alumno
        lim+=1
        print()
        if lim<len(alumnos):
            opcion=input("¿desea cargar los datos de otro estudiante? SI/NO: ")
    return(lim)



def mostrar_alumnos_notas(alumnos, limite):
    for i in range(0, limite, 1):
        print()
        print("El/la estudiante ", alumnos[i]['nombre_estudiante'], "tiene como nota: ", alumnos[i]['nota_estudiante'])


def mayor_nota(limite, alumnos):
    nota=0
    for i in range(0, limite, 1):
        if alumnos[i]['nota_estudiante']>nota:
            nota=alumnos[i]['nota_estudiante']
            numero_nota_mayor=alumnos[i]['numero_estudiante']
    return(numero_nota_mayor)


def menor_nota(limite, alumnos):
    nota_menor=alumnos[0]['nota_estudiante']
    for i in range(0, limite, 1):
        if alumnos[i]['nota_estudiante']<=nota_menor:
            nota_menor=alumnos[i]['nota_estudiante']
            numero_nota_mayor=alumnos[i]['numero_estudiante']
    return(numero_nota_mayor)



def nota_laura_suarez(limite, alumnos, buscado):
    for i in range(0, limite, 1):
        if alumnos[i]['nombre_estudiante']==buscado:
            nota_laura=alumnos[i]['nota_estudiante']
            print("La nota de Laura Suarez es: ", nota_laura)


limite=cargar_estudiantes(alumnos, lim)

mostrar_alumnos_notas(alumnos, limite)

print()

print("El número de el/la estudiante con mayor nota es: ", mayor_nota(limite, alumnos))

print()

print("El número de el/la estudiante con menor nota es: ", menor_nota(limite, alumnos))

print()

nota_laura_suarez(limite, alumnos, buscado)