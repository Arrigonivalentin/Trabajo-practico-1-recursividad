# Se tiene una empresa con 20 sucursales que vende distintos tipos de artículos (30). Se desea 
# acumular cantidad de ventas por sucursal y por artículo.

matriz=[[0, 0], 
        [0, 0], 
        [0, 0]]

totalart=0

Filas=len(matriz)
Columnas=len(matriz[0])

def cargar(matriz):
 for i in range(Filas):
    for j in range(Columnas):
       matriz[i][j]=int(input('ingrese la cantidad vendida: '))


def articulos(matriz, totalart):
  for i in range(Filas):
    totalart=0
    for j in range(Columnas):
      totalart=matriz[i][j]
      return(totalart)


cargar(matriz)
articulos(matriz, totalart)      
print(totalart)