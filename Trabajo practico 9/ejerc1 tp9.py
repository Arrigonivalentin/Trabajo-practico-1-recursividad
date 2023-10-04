#  Hacer un algoritmo que:

# - Lea una lista de números de teclado que culmina con uno negativo.
# - Los ordene en forma creciente y Visualice la lista ordenada.
# - Buscar si existe el Nº 27 en la lista.


lista=[0, 0, 0, 0, 0, 0]


def asignacion(lim):
  num = int(input("ingrese un número: "))

  if num<0:
     print

  while (num!=-1) and lim<len(lista):
     
    lista[lim] = num

    lim+= 1
    
    num = int(input("ingrese un número: "))
     
  return(lim)




def burbuja(lista):
    for i in range(0,(len(lista)-1)-1):
        for j in range(0,len(lista)-1-i):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux


def busqueda_binaria(lista, lim, buscado, pos):
    pri=0
    ult=len(lista)-1
    while (pos==0) and (pri<=ult):
        med=(pri+ult)//2
        if lista[med]==buscado:
            pos=med
        elif lista[med]>=buscado:
            ult=med-1
        else:
            pri=med+1   
    return(pos)

def mostrar_lista(lista):
    print(lista)


buscado=27 
lim=0 
asignacion(lim)
pos=0
mostrar_lista(lista)
burbuja(lista)
mostrar_lista(lista)
x=busqueda_binaria(lista, lim, buscado, pos)
if x!=0: print('el buscado está en: ', x)
else: print('el buscado no está en la lista')


burbuja(lista)
