"""
1 confeccion una funcion que retorne una lista
 de 4 elementos enteros

 """
def cargar ():
     lista=[]
     for x in range (4) :
          valor = int(input("ingrese valor:"))
          lista.append(valor)
     return lista

lista1 =  cargar ()
print ( lista1 )

"""
2 confeccionar una funcion que sume todos los elementos de la
lista y lo imprima
"""
def sumar_elementos(lista):
    suma=0
    for x in range(len (lista)):
        suma =suma + lista [x]
    print(suma)


sumar_elementos(lista1)

"""
3 confeccionar una funcion que imprima el mayor de la lista
"""

def imprimir_mayor (lista):
     mayor=lista [0]
     for x in range(1,len(lista)):
         if lista [x] > mayor:
             mayor = lista [x]
     print( "mayor elementos:" ,mayor )


imprimir_mayor(lista1)



             

