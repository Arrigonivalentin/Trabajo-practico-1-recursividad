#  Supongamos que definimos un arreglo de 1000 pólizas de seguro de vida, cada una posee Nº de 
# póliza, nombre del asegurado, dirección, año de nacimiento, cantidad asegurada y cuota. Codificar 
# un algoritmo que permita ingresar pólizas en la estructura anterior. Además, se pide:
# - Mostrar los nombre y direcciones de las personas que cumplen 70 años en el 
# corriente año.
# - Mostrar las personas cuya cuota es menor a $ 30.00.
# - Mostrar las personas que tengan asegurada un monto mayor a $100.000 
# ordenados alfabéticamente
# - Mostrar si Pedro Fernández está asegurado en la compañía.

polizas=[0, 0, 0]

lim=0



def datos_polizas():
    numero_poliza=int(input("ingrese el numero de la poliza: "))
    nombre_asegurado=input("ingrese el nombre del asegurado: ")
    direccion=input("ingrese la direccion del asegurado: ")
    año_nacimiento=int(input("ingrese el año de nacimiento: "))
    cantidad_asegurada=int(input("ingrese la cantidad asegurada: "))
    cuota=int(input("ingrese la cantidad de la cuota: "))

    poliza={
        'numero_poliza':numero_poliza,
        'nombre_asegurado':nombre_asegurado,
        'direccion':direccion,
        'año_nacimiento':año_nacimiento,
        'cantidad_asegurada':cantidad_asegurada,
        'cuota':cuota
    }

    return(poliza)



def Cargar_polizas(lim,polizas):
    opcion=input("Ingrese (si) para cargar una poliza:  ")
    while (opcion=='si' and lim<(len(polizas))):
        otra_poliza=datos_polizas()
        polizas[lim]=otra_poliza
        lim+=1
        print()
        if lim<(len(polizas)):
            opcion=input("Ingrese (si) para cargar una poliza:  ")
    return (lim)


def mostrar_personas(polizas, limite):
    for i in range(0,limite,1):
        if polizas[i]['año_nacimiento']==1953:
            print(polizas[i]['nombre_asegurado'], "Cumple 70 años, su dirección es: ", polizas[i]['direccion'])



def cuota_menor(polizas, limite):
    cantidad_cuota_menor=0
    for i in range(0,limite,1):
        if polizas[i]['cuota']<30000:
            cantidad_cuota_menor+=1
    return(cantidad_cuota_menor)



def monto_asegurado(polizas, limite):
    cantidad_monto_asegurado=0
    for i in range(0, limite, 1):
        if polizas[i]['cantidad_asegurada']>100000:
         cantidad_monto_asegurado+=1
    return(cantidad_monto_asegurado)


def buscar_persona(polizas, limite):
    buscado="pedro fernandez"
    for i in range(0,limite,1):
        if polizas[i]['nombre_asegurado']==buscado:
            print("Pedro Fernandez está asegurado")


limite=Cargar_polizas(lim,polizas)

Cargar_polizas(lim, polizas)

mostrar_personas(polizas, limite)

print("la cantidad de personas con un monto asegurado es:", monto_asegurado(polizas, limite))

print("las personas con una cuota menor a $30000 es: ", cuota_menor(polizas, limite))


buscar_persona(polizas, limite)
