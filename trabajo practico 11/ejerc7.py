import os
# 7- En una empresa se guardan:
# los códigos de empleados.
# edades.
# los sueldos.
# la antigüedad en años (Nº entero).

# Se pide calcular:

# a- Sueldo del empleado más antiguo y edad.
# b- Sueldo del empleado más nuevo y edad. 
# c- Promedio de sueldos.
# d- Promedio de edades.

empleados=[0, 0, 0, 0]

lim=0



def ingresar_empleados():
    codigo_empleado=int(input("Ingrese el codigo del empleado: "))
    edad_empleado=int(input("Ingrese la edad del empleado: "))
    sueldo_empleado=int(input("Ingrese el sueldo del empleado: "))
    ant_empleado=int(input("Ingrese la antigüedad del empleado (en años): "))
    os.system('cls')
    empleado={
        'codigo_empleado':codigo_empleado,
        'edad_empleado':edad_empleado,
        'sueldo_empleado':sueldo_empleado,
        'ant_empleado':ant_empleado
    }

    return(empleado)


def cargar_empleados(empleados, lim):
    opcion=input("¿desea cargar los datos de un empleado? SI/NO: ")
    while opcion=="si" and (lim<len(empleados)):
        nuevo_empleado=ingresar_empleados()
        empleados[lim]=nuevo_empleado
        lim+=1
        print()
        if lim<len(empleados):
            opcion=input("¿desea cargar los datos de otro empleado? SI/NO: ")
    return(lim)


# a- Sueldo del empleado más antiguo y edad.

def sueldo_edad_ant(empleados, limite):
    mas_antiguo=empleados[0]['ant_empleado']
    for i in range(0, limite, 1):
        if empleados[i]['ant_empleado']>=mas_antiguo:
            sueldo_empleado_antiguo=empleados[i]['sueldo_empleado']
            edad_empleado_antiguo=empleados[i]['edad_empleado']
    print("El sueldo del empleado más antiguo es de: $",sueldo_empleado_antiguo, " y tiene: ", edad_empleado_antiguo, " años")


# b- Sueldo del empleado más nuevo y edad.

def sueldo_edad_nuevo(empleados, limite):
    mas_nuevo=empleados[0]['ant_empleado']
    for i in range(0, limite, 1):
        if empleados[i]['ant_empleado']<=mas_nuevo:
            sueldo_empleado_nuevo=empleados[i]['sueldo_empleado']
            edad_empleado_nuevo=empleados[i]['edad_empleado']
    print("El sueldo del empleado mas nuevo es de: $", sueldo_empleado_nuevo, " y tiene ", edad_empleado_nuevo, " años")


# c- Promedio de sueldos.

def promedio_sueldos(empleados, limite):
    total_sueldos=0
    for i in range(0, limite, 1):
     total_sueldos+=empleados[i]['sueldo_empleado']
    promedio=total_sueldos/limite
    print("El promedio de todos los sueldos es de: $", promedio)


# d- Promedio de edades.

def promedio_edades(empleados, limite):
    total_edades=0
    for i in range(0, limite, 1):
        total_edades+=empleados[i]['edad_empleado']
    edad_promedio=(total_edades/limite)
    print("El promedio de edades es de: ", edad_promedio, "años")



limite=cargar_empleados(empleados, lim)
print()
sueldo_edad_ant(empleados, limite)
print()
sueldo_edad_nuevo(empleados, limite)
print()
promedio_sueldos(empleados, limite)
print()
promedio_edades(empleados, limite)


