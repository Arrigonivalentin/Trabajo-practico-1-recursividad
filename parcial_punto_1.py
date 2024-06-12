# 1) Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos. 



def invertir(lista):
    if (len(lista)-1) < 0:
        return 0
    else:
        print(lista[-1])
        return invertir(lista[:-1])

lista_numero=[1,2,3,4,5]

invertir(lista_numero)
