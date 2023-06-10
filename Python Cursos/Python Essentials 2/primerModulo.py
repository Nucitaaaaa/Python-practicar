
"""
print("xd")

print(__name__)

if __name__ == "__main__":
    print("Prefiero ser módulo.")
else:
    print("Me gusta ser un módulo.")

"""

__counter = 0 #Se utiliza para saber cuantas veces se invocarán las funciones

def suma(lista): #Se define la función suma 
    global __counter #se declara global la variable __counter
    __counter += 1 #Cada que la función se use, se suma 1 al contador
    la_suma = 0 #Se declara un acumulador para la funcion suma 
    for elementos in lista: #Se crea un bucle for para el contador anterior
        la_suma += elementos #Se le suma al contador el valor de cada elemento de la lista
    return la_suma #retorna el resultado de la suma 

def producto(lista): #Se define la función producto
    global __counter #se declara global la variable __counter
    __counter += 1 #Cada que la función se use, se suma 1 al contador
    elProducto = 1 #Se declara un acumulador para la función producto
    for elementos in lista: #Se crea un bucle for para el contador anterior
        elProducto *= elementos #Se le multiplica al contador el valor de cada elemento de la lista 
    return producto #Retorna el resultado del producto 

#Prueba_Entidades

if __name__ == "__main__":
    print("Soy un modulo probando entidades")
    lista = [ i + 1 for i in range(5)]
    print(suma(lista) == 15)
    print(producto(lista) == 120)

