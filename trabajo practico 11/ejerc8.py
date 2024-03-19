import os
# 8- De cada alumno de una materia ‘x’ se registra Nº de alumno, nota y sexo.

#  Se desea saber:
# a-cuantos varones aprobaron (nota>=4).
# b- que % de mujeres sacó 10.
# c- % de desaprobados.

alumnos=[0, 0, 0, 0]

lim=0


def ingresar_alumnos():
    numero_alumno=int(input("Ingrese número del alumno: "))
    nota_alumno=int(input("Ingrese la nota del alumno: "))
    sexo_alumno=input("Ingrese el sexo del alumno: ")
    # os.system('cls')
    alumno={
        'numero_alumno':numero_alumno,
        'nota_alumno':nota_alumno,
        'sexo_alumno':sexo_alumno,
    }

    return(alumno)


def cargar_alumnos(alumnos, lim):
    opcion=input("¿desea cargar los datos de un alumno? SI/NO: ")
    while opcion=="si" and (lim<len(alumnos)):
        nuevo_alumno=ingresar_alumnos()
        alumnos[lim]=nuevo_alumno
        lim+=1
        print()
        if lim<len(alumnos):
            opcion=input("¿desea cargar los datos de otro alumno? SI/NO: ")
    return(lim)


def aprobados(alumnos, limite):
    varones_aprobados=0
    for i in range(0, limite, 1):
        if alumnos[i]['sexo_alumno']=="masculino" and alumnos[i]['nota_alumno']>=4:
            varones_aprobados+=1
    print("La cantidad de varones aprobados es: ", varones_aprobados)


def porcentaje_mujeres(alumnos, limite):
    cantidad_mujeres_10=0
    for i in range(0, limite, 1):
        if alumnos[i]['sexo_alumno']=="femenino" and alumnos[i]['nota_alumno']==10:
            cantidad_mujeres_10+=1
    porcentaje=(cantidad_mujeres_10*100)/limite
    return(porcentaje)


def porcentaje_desaprobados(alumnos, limite):
    cantidad_desaprobados=0
    for i in range(0, limite, 1):
        if alumnos[i]['nota_alumno']<4:
            cantidad_desaprobados+=1
    desaprobados=(cantidad_desaprobados*100)/limite
    return (desaprobados)




limite=cargar_alumnos(alumnos, lim)
aprobados(alumnos, limite)
print("El porcentaje de mujeres que sacaron 10 es del: %", porcentaje_mujeres(alumnos, limite))
print("El porcentaje de desaprobados es del: %", porcentaje_desaprobados(alumnos, limite))