# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:

# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

from pila_para_parcial import Stack

dinosaurios = [
    {
    "nombre": "Tyrannosaurus Rex",
    "especie": "Theropoda",
    "peso": 7000,
    "descubridor": "Barnum Brown",
    "ano_descubrimiento": 1902
    },
    {
    "nombre": "Triceratops",
    "especie": "Ceratopsidae",
    "peso": 6000,
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1889
    },
    {
    "nombre": "Velociraptor",
    "especie": "Dromaeosauridae",
    "peso": 15,
    "descubridor": "Henry Fairfield Osborn",
    "ano_descubrimiento": 1924
    },
    {
    "nombre": "Brachiosaurus",
    "especie": "Sauropoda",
    "peso": 56000,
    "descubridor": "Elmer S. Riggs",
    "ano_descubrimiento": 1903
    },
    {
    "nombre": "Stegosaurus",
    "especie": "Stegosauridae",
    "peso": 5000,
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1877
    },
    {
    "nombre": "Spinosaurus",
    "especie": "Spinosauridae",
    "peso": 10000,
    "descubridor": "Ernst Stromer",
    "ano_descubrimiento": 1912
    },
    {
    "nombre": "Allosaurus",
    "especie": "Theropoda",
    "peso": 2000,
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1877
    },
    {
    "nombre": "Apatosaurus",
    "especie": "Sauropoda",
    "peso": 23000,
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1877
    },
    {
    "nombre": "Diplodocus",
    "especie": "Sauropoda",
    "peso": 15000,
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1878
    },
    {
    "nombre": "Ankylosaurus",
    "especie": "Ankylosauridae",
    "peso": 6000,
    "descubridor": "Barnum Brown",
    "ano_descubrimiento": 1908
    },
    {
    "nombre": "Parasaurolophus",
    "especie": "Hadrosauridae",
    "peso": 2500,
    "descubridor": "William Parks",
    "ano_descubrimiento": 1922
    },
    {
    "nombre": "Carnotaurus",
    "especie": "Theropoda",
    "peso": 1500,
    "descubridor": "José Bonaparte",
    "ano_descubrimiento": 1985
    },
    {
    "nombre": "Styracosaurus",
    "especie": "Ceratopsidae",
    "peso": 2700,
    "descubridor": "Lawrence Lambe",
    "ano_descubrimiento": 1913
    },
    {
    "nombre": "Therizinosaurus",
    "especie": "Therizinosauridae",
    "peso": 5000,
    "descubridor": "Evgeny Maleev",
    "ano_descubrimiento": 1954
    },
    {
    "nombre": "Pteranodon",
    "especie": "Pterosauria",
    "peso": 25,
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1876
    },
    {
    "nombre": "Quetzalcoatlus",
    "especie": "Pterosauria",
    "peso": 200,
    "descubridor": "Douglas A. Lawson",
    "ano_descubrimiento": 1971
    },
    {
    "nombre": "Plesiosaurus",
    "especie": "Plesiosauria",
    "peso": 450,
    "descubridor": "Mary Anning",
    "ano_descubrimiento": 1824
    },
    {
    "nombre": "Mosasaurus",
    "especie": "Mosasauridae",
    "peso": 15000,
    "descubridor": "William Conybeare",
    "ano_descubrimiento": 1829
    },
]

pila_dinos = Stack()
pila_aux = Stack()
pila_AQS = Stack()

for dinosaurio in dinosaurios:
    pila_dinos.push(dinosaurio)


def volver_pila(pila_dinos, pila_aux):
    while pila_aux.size() >0:
        pila_dinos.push(pila_aux.pop())

# a) Contar cuantas especies hay;
def cantidad_especies(pila_dinos):
    lista_especies=[]
    while pila_dinos.size() > 0:
        if lista_especies.count(pila_dinos.on_top()["especie"]) == 0:
            lista_especies.append(pila_dinos.on_top()["especie"])
            pila_aux.push(pila_dinos.pop())
        else:
            pila_aux.push(pila_dinos.pop())
    return print("la cantidad de especies es:", len(lista_especies))

cantidad_especies(pila_dinos)
volver_pila(pila_dinos, pila_aux)
print




# b) Determinar cuantos descubridores distintos hay;
def cantidad_descubridores(pila_dinos):
    lista_descubridores=[]
    while pila_dinos.size() > 0:
        if lista_descubridores.count(pila_dinos.on_top()["descubridor"]) == 0:
            lista_descubridores.append(pila_dinos.on_top()["descubridor"])
            pila_aux.push(pila_dinos.pop())
        else:
            pila_aux.push(pila_dinos.pop())
    return print("la cantidad de descubridores es:", len(lista_descubridores))

cantidad_descubridores(pila_dinos)
volver_pila(pila_dinos, pila_aux)
print()



# c) Mostrar todos los dinosaurios que empiecen con T;

def empiezan_T(pila_dinos):
    nombres_T = []
    for i in range(pila_dinos.size()):
        if pila_dinos.on_top()['nombre'].startswith(('T')):
            nombres_T.append(pila_dinos.on_top()['nombre'])
            pila_aux.push(pila_dinos.pop())
        else:
            pila_aux.push(pila_dinos.pop())
    return(nombres_T)



print("estos son los dinosaurios que empiezan con T: ", empiezan_T(pila_dinos))
volver_pila(pila_dinos, pila_aux)
print()

# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg

def peso_menor_275(pila_dinos):
    lista_menores_275 = []
    for i in range(pila_dinos.size()):
        if pila_dinos.on_top()['peso']<275:
            lista_menores_275.append(pila_dinos.on_top()['nombre'])
            pila_aux.push(pila_dinos.pop())
        else:
            pila_aux.push(pila_dinos.pop())
    return(lista_menores_275)

print("estos son los dinosaurios que pesan menos de 275kg")
for element in peso_menor_275(pila_dinos):
    print(element)

print()

volver_pila(pila_dinos, pila_aux)


# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

def empiezan_con_AQS(pila_dinos, pila_AQS):
    for i in range(pila_dinos.size()):
        if pila_dinos.on_top()['nombre'].startswith(("A", "Q", "S")):
            pila_AQS.push(pila_dinos.on_top()['nombre'])
            pila_aux.push(pila_dinos.pop())
        else:
            pila_aux.push(pila_dinos.pop())
    print(pila_AQS.elements)

print("estos son los dinosaurios que empiezan con A, Q y S: ")
empiezan_con_AQS(pila_dinos, pila_AQS)





