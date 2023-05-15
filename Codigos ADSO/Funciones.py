
#Ejercicio_Explicación_Funciones

"""
#Sin_Parametros

def nombre():
    print(f"El nombre de mi perro es shiro")

nombre()
"""
"""
#Con_Parametros

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el primer numero: "))

def calc (suma,resta,mult,divi):
    
    print(f"Suma = {suma}, Resta = {resta}, Multiplicación = {mult}, División = {divi}")

calc (num1 + num2, num1 - num2, num1 * num2, round(num1 / num2,2))
"""

"""
#return

numero = int(input())
def es_par(numero):
    if numero % 2 == 0:
        return "es par"
    else:
        return "Es impar"

resultado = es_par(numero)
print(resultado)

"""
#return2

def cuadrado(numero):
    cuadrado = numero ** 2
    return cuadrado

resultado = cuadrado(5)
print(resultado)


















def suma(a, b):
    resultado = a + b
    resultado2= b + a 
    return resultado

resultado_suma = suma(3, 4)
print(resultado_suma)















