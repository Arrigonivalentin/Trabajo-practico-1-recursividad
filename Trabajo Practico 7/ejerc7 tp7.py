#  Leer un vector de N elementos y emitir la posición que ocupa el mayor de ellos

lista=[0, 0, 0, 0, 0]

for i in range (0, 5):
    lista[i]=int(input("ingrese cinco números: "))

print("la posicion en la que se encuentra el mayor número es en el indice: ", lista.index(max(lista)))