"""2- confeccionaruna funcionque le enviamos
el lado de un cuadrado y nos muestresu superficie"""

def sumar(v1, v2):
    suma= v1 + v2
    print("la suma de  los valores es",suma)
    
def calcular_sup_cuadrado(lado):
    superficie= lado * lado
    print("la superficie del cuadradoes", superficie)

#bloque pricipal
suma(10, 40)
calcular_sup_cuadrado(20)
x=12
calcular_sup_cuadrado(x)
