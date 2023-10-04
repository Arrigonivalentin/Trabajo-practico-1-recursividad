# Leer un vector con la edad de un grupo de x cantidad de personas. Se pide mostrar la 
# cantidad de jóvenes considerando a una persona joven si su edad esta entre 20 y 40 
# años.

lista=[0, 0, 0, 0, 0, 0]

contador=0

def edades(contador):

    contadorpers=0

    for i in range(0, 6):
         edad=int(input("ingrese las edades: "))

         lista[i]=edad

         contador+=1

         if edad>20 and edad<40:
              contadorpers+=1
         

    print("la cantidad de personas que hay es: ", contador)

    if contadorpers==1:
         print("hay una persona con una edad entre 20 a 40 años")

    elif contadorpers==0:
         print("no hay ninguna persona entre 20 a 40 años")

    else:
         print("hay mas de una persona con una edad entre 20 a 40 años")


edades(contador)