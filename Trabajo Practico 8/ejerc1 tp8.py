#  Calcular la media de una lista de 25 estudiantes de una clase de informática con notas en cuatro 
# materias

matriz=[[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

total=0
# cargar notas

Filas=len(matriz)
Columnas=len(matriz[0])

def cargar(matriz):
 for i in range(Filas):
    for j in range(Columnas):
       matriz[i][j]=int(input('ingrese la nota: '))


# sumar notas

def sumar(matriz, total):
 total=0
 for i in range(Filas):
    for j in range(Columnas):
       total+=matriz[i][j]
 return(total)




cargar(matriz)
sumar(matriz, total)
print(matriz)