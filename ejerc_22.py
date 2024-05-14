# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo

# c. Utilizar un vector para representar la mochila.


mochila = ["ganzua", "pala", "destornillador", "sable de luz"]

def usar_la_fuerza(mochila, i=0):
    if len(mochila)==0:
        return print("la mochila esta vacia")
    elif len(mochila)==i:
        return print("no se enocntro el sable")
    elif mochila[i]=="sable de luz":
        return(print("se enocntro el sable, se necesio sacar: ", i, "objetos"))
    else:
        return (usar_la_fuerza(mochila, i+1))
        
    

usar_la_fuerza(mochila)
    


