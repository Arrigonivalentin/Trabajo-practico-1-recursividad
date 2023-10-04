#  Leer un vector de N elementos. Emitir el valor mínimo y la cantidad de veces que se repitió 
# ese valor.


lista=[0, 0, 0, 0, 0]

for i in range (0, 5):
    lista[i]=int(input("ingrese cinco números: "))

print("el valor minimo es: ", min(lista))
print("la cantidad de veces que se repitió es: ", lista.count(min(lista)))