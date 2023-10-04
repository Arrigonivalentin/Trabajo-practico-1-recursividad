#  Imprimir la media de los elementos que se encuentran en las posiciones pares y la media 
# de los elementos que se encuentran en las posiciones impares de un vector numérico

lista=[0, 0, 0, 0, 0, 0, 0]

suma_pares=0
contador=0
contador2=0
suma_impares=0

def asignacion():
    for i in range (0, 6):
        lista[i]=int(input("ingrese seis números: "))

asignacion()

def suma(suma_pares, contador, suma_impares, contador2):
    for i in range (0, 6):
        if i%2==0:
         suma_pares=suma_pares+lista[i]

         contador+=1
        else:
           suma_impares=suma_impares+lista[i]
           contador2+=1

print("el resultado de la suma de los pares es: ", suma_pares/contador)

print("el resultado de la suma de los impares es: ", suma_impares/contador2)



print(suma(suma_pares, contador, suma_impares, contador2))
