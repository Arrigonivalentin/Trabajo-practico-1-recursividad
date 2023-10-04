#  Leer un vector de N elementos, de a uno por vez. Generar y emitir la sumatoria de sus 
# componentes de posición par.


lista=[0, 0, 0, 0, 0, 0]

suma=0

def asignacion():
    for i in range(0, 6):
        
        lista[i]=float(input("ingrese seis numeros: "))
        

def sumatoria(suma):
     for i in range (0,6):

        if i%2==0:
         suma=suma+lista[i]

     return (suma)


asignacion()   

sumatoria(suma)

print ("la suma de sus componentes es: ", sumatoria(suma))
