#  Dada una matriz rectangular realizar un programa que devuelva el mayor de los elementos 
# contenidos en ella, considerando solamente aquellos en los cuales la suma de sus subíndices es
# par. Es decir [1,1], [1,3], [1,5] [2,2], etc

matriz= [[0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]

maximo=matriz[0][0]

Filas=len(matriz)
Columnas=len(matriz[0])


def cargar(matriz):
 for i in range(Filas):
    for j in range(Columnas):
        matriz[i][j] = int(input('ingrese el número: '))


def mayor(matriz, maximo):
   for i in range(Filas):
      for j in range(Columnas):
         if (i+j)%2==0 and (matriz[i][j]>maximo):
             maximo=matriz[i][j]
   return(maximo)

def mostrar(maximo):
 print("el mayor es:", maximo)


cargar(matriz)
print(matriz)
maximo=mayor(matriz, maximo)
mostrar(maximo)

