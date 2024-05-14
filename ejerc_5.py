# Desarrollar una función que permita convertir un número romano en un número decimal.


numero_romano = "XIX"
def romanoadecimal(numero_romano):
    valor = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(numero_romano) == 0:
        return 0
    elif len(numero_romano) == 1:
        return valor[numero_romano]
    else:
        if valor[numero_romano[0]] < valor[numero_romano[1]]:
            return valor[numero_romano[1]] - valor[numero_romano[0]] + romanoadecimal(numero_romano[2:])
        else:
            return valor[numero_romano[0]] + romanoadecimal(numero_romano[1:])


print("El número romano", numero_romano, "en decimal es:", romanoadecimal(numero_romano))


