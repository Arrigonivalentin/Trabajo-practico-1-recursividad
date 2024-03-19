import os
# 1- Se tienen los datos de los afiliados que realizan aportes a obras sociales

# de cada uno se almacena:
#  Apellido y nombre.
#  Obra social.
#  Monto de cuota.
#  cantidad de integrantes del grupo familiar.


# Se pide:
# a- Realice un subprograma que cargue los datos hasta que el usuario lo desee.
# b- Listado ordenado por Obra Social y apellido y nombre.
# d- Mostrar total aportado a esta obra social por todos sus afiliados (IOSPER).
# e- Calcular total de familias que poseen más de 6 integrantes en su grupo familiar, 
# y de éstos mostrar solo los que aportan más de 10000 pesos.
# f- Mostrar si Pablo Benitez es afiliado, de ser asi mostrar la cantidad de integrantes 
# del grupo familiar y la obra social.



afiliados=[0, 0, 0, 0]

lim=0


def ingresar_afiliados():
    nombre_afiliado=input("Ingrese nombre y apellido del afiliado: ")
    obra_social_afiliado=input("Ingrese la obra social: ")
    monto_cuota_afiliado=int(input("Ingrese el monto que aporta: "))
    familiares_afiliado=int(input("Ingrese la cantidad de familiares: "))
    os.system('cls')
    afiliado={
        'nombre_afiliado':nombre_afiliado,
        'obra_social_afiliado':obra_social_afiliado,
        'monto_cuota_afiliado':monto_cuota_afiliado,
        'familiares_afiliado':familiares_afiliado
    }

    return(afiliado)


def cargar_afiliados(afiliados, lim):
    opcion=input("¿desea cargar los datos de un afiliado? SI/NO: ")
    while opcion=="si" and (lim<len(afiliados)):
        nuevo_afiliado=ingresar_afiliados()
        afiliados[lim]=nuevo_afiliado
        lim+=1
        print()
        if lim<len(afiliados):
            opcion=input("¿desea cargar los datos de otro afiliado? SI/NO: ")
    return(lim)

def total_aportado(afiliados, limite):
    aportado=0
    for i in range(0, limite, 1):
        if afiliados[i]['obra_social_afiliado']=="iosper":
            aportado=aportado+afiliados[i]['monto_cuota_afiliado']
    print("la cantidad de los aportes a la obra social de IOSPER es de: $", aportado)


def total_familias(afiliados, limite):
    aporte_familia_6=0
    total_familias_6=0
    for i in range(0, limite, 1):
        if afiliados[i]['familiares_afiliado']>6:
            total_familias_6+=1 
            if afiliados[i]['monto_cuota_afiliado']>10000:
                aporte_familia_6+=1
    print("El total de familias con más de 6 integrantes: ", total_familias_6)
    print()
    print("La cantidad de familias con más de 6 que aportan más de $10000 es: ", aporte_familia_6)


def buscar_persona(afiliados, limite):
    for i in range(0, limite, 1):
        if afiliados[i]['nombre_afiliado']=="pablo benitez":
         print("Pablo Benitez es afiliado")
         print()
         print("La cantidad de familiares de Pablo Benitez es: ", afiliados[i]['familiares_afiliado'], " y su obra social es: ", afiliados[i]['obra_social_afiliado'])


def burbuja(afiliados, limite):
    for i in range(limite - 1):
        for j in range(limite - 1 - i):
            ordenado_actual = afiliados[j]['obra_social_afiliado'] + afiliados[j]['nombre_afiliado']
            ordenado_siguiente = afiliados[j + 1]['obra_social_afiliado'] + afiliados[j + 1]['nombre_afiliado']
            if ordenado_actual > ordenado_siguiente:
                aux = afiliados[j]
                afiliados[j] = afiliados[j + 1]
                afiliados[j + 1] = aux

def Mostrar_personas(afiliados, limite):
   for i in range(0, limite, 1):
       afi = afiliados[i]
       print("obra social: ", afi['obra_social_afiliado'])
       print("Nombre: ", afi['nombre_afiliado'])
       print()


limite=cargar_afiliados(afiliados, lim)
burbuja(afiliados, limite)
Mostrar_personas(afiliados, limite)
total_aportado(afiliados, limite)
total_familias(afiliados, limite)
buscar_persona(afiliados, limite)