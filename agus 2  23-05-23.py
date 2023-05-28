"""
en una empresa se tiene 5 empleados.
desarrollar los siguientes funcuiones y llamarlas desde el bloque principal

1-cargar los sueldos de los 5 empleados por teclado y retomar dicha lista.
2- imprimir todos los sueldos
3- imprimir  sueldos altos ( mayor a 200000)
4- calcular e imprimir cuanto gasta la empresa en sueldos.
5- calcular y retomar rl promedio de sueldos.
"""
def cargar_sueldos():
    sueldos = []
    for x in range(5):
         valor = int(input("ingrese sueldo:"))
         sueldos.append(valor)
    return sueldos

def imprimir_todos(sueldos):
        print(sueldos)

        
def sueldo_altos(sueldos):
 for x in range(len(sueldos)):
     if sueldos[x]>200000:
            print(sueldo[x])

def gasto_sueldos(sueldos):
    pass
    

def retomar_promedio(sueldos):
    pass

    

 sueldos=cargar_sueldos()
imprimir_todos (sueldos)
