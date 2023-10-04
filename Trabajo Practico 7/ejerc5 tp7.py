#  Leer un vector de 10 elementos reales y emitir las siguientes leyendas según, 
# corresponda: “El vector tiene todas sus componentes positivas”, “El vector tiene 
# componentes negativas”, “El vector tiene algún cero”.

lista=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# def asignacion():
#     for i in range (0, 10):
#         lista[i]=float(input("ingrese 10 números: "))
        
#     if lista[i]>0:
#          print("todos los los componentes son positivos")

#     elif lista[i]<0:
#          print("tiene componentes negativos")

#     elif lista[i]==0:
#          print("la lista tiene algún cero")

# asignacion()


def asignacion(lista):
    for i in range (0, 10):
        lista[i]=float(input("ingrese 10 números: "))



    if lista[i]>0:
         print("todos los elementos son positivos")

    elif lista[i]>0 and lista[i]==0:
         print("la lista tiene algun cero")

    elif lista[i]<0 and lista[i]==0:
         print("la lista tiene algun cero")
     
    elif lista[i]<0:
         print("todos los elementos son negativos")



asignacion(lista)

