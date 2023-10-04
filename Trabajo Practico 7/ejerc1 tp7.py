# leer un vector de 100 Números reales, un componente por vez. Emitir la sumatoria de 
# sus componentes

lista=[0,0,0,0,0]

suma=0

def asignacion():
    for i in range(0,5):
        lista[i]=float(input("ingrese cinco numeros: "))
        

def sumatoria(suma):
     for i in range (0,5):
        suma=suma+lista[i]
     return (suma)


asignacion()   

sumatoria(suma)

print ("la suma de sus componentes es: ", sumatoria(suma))