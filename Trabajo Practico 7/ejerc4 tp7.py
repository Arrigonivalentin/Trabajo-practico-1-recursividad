# Generar y emitir el vector A = (1,0,1,0,1,0, ...) de N elementos.

lista=[0, 0, 0, 0, 0, 0]


for i in range (0, len(lista),2):
    lista[i]=1


print (lista)