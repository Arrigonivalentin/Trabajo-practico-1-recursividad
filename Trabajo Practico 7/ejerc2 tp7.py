# Sea un lote de Números enteros positivos que finaliza con un cero que no debe ser procesado. Generar un vector con dichos valores
#  y calcular la productoria de sus componentes.

lista=[0,0,0,0,0]

lim=0


def asignacion(lim):
  num = int(input("ingrese un número: "))

  while num!= 0 and lim<len(lista):
     
    lista[lim] = num

    lim+= 1
    
    num = int(input("ingrese un número: "))
     
  return(lim)





def mult(lista, lim):
  producto=1
 
  for i in range (lim):
    producto = producto*lista[i]

  print("el resultado es: ", producto)




#cuerpo principal

lim=asignacion(lim)

mult(lista, lim)
