#  Dada una matriz de 5 filas y 10 columnas: a- Escribir el algoritmo necesario para cargar la matriz 
# con valores. B- Determinar la sumatoria de c/u de las columnas. C- Mostrar el mayor valor de c/u 
# de sus columnas. D- Mostrar la posición (F,C) del menor valor de la matriz.


matriz=[[0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0 ]]



mayor=0
total_columnas=0

filas=len(matriz)
columnas=len(matriz[0])



def cargar(matriz):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j]=int(input("ingrese un número: "))


def suma_columnas(matriz, total_columnas):
  for j in range(columnas):
     total_columnas=0
     for i in range(filas):
         total_columnas+=matriz[i][j]
     print("el total de la columna ", j, "es: ", total_columnas)


def valores(matriz, mayor):
   for j in range(columnas):
      mayor=0
      for i in range (filas):
         if matriz[i][j]>mayor:
          mayor=matriz[i][j]
      print("el mayor de la columna ", j, "es: ", mayor)


def posc(matriz):
   posicion=[0, 0]
   menor=matriz[0][0]
   for i in range(filas):
      for j in range(columnas):
         if matriz[i][j]<menor:
            menor=matriz[i][j]
            posicion=[i,j]
   print("el menor se encuentra en la posición: ", posicion)
         




cargar(matriz)

print(matriz)

suma_columnas(matriz, total_columnas)

valores(matriz, mayor)
posc(matriz)




