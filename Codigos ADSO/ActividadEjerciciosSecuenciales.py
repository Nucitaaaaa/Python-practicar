
"""
#Ejercicio_1

Diseñar un algoritmo que permita por teclado capturar el nombre , la edad, la ciudad de una persona , los resultados mostrar por pantalla.

#Solución

name = str(input("Escriba su nombre: "))
age = int(input("Digite su edad: "))
city = str(input("Escriba su ciudad de origen: "))

print(f"Nombre: {name}\nEdad: {age}\nCiudad: {city}")

"""

"""
#Ejercicio_2

Diseñar un algoritmo que permita calcular el salario mensual de un trabajador
teniendo en cuenta los días que trabajó y el valor de cada día.

#Solución

valorDia = int(input("Digite la cantidad de dinero que gana por dia:"))
diasTrabajados = int(input("Digite cuantos dias trabajó durante el mes:"))

salario = valorDia * diasTrabajados

print(f"Su salario mensual es de: ${salario}")

"""

"""
#Ejercicio_3

Diseñar un algoritmo que permita calcular las operaciones básicas aritméticas ingresadas por teclado de dos números dados.

#Solución

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 // num2

print(f"El resultado de la suma de {num1} y {num2} es {suma}")
print(f"El resultado de la resta de {num1} y {num2} es {resta}")
print(f"El resultado de la multiplicación de {num1} y {num2} es {multi}")
print(f"El resultado de la division de {num1} y {num2} es {divi}")

"""

"""
#Ejercicio_4

Diseñar un algoritmo que permita aplicar un descuento en el supermercado de tal forma permita visualizar el monto a pagar después de aplicar dicho procedimiento.

#Solución

producto = str(input("Escriba el producto a adquirir: "))
precio = float(input("Digite el precio original del producto: "))

print(f"El precio original de el producto ({producto}) es de {precio}")

descuento = int(input("Ingrese el descuento que se le aplicará al producto: "))

descuento = precio * descuento / 100
precioDescuento = precio - descuento

print(f"El precio con descuento de el producto ({producto}) es de {precioDescuento}")

"""
"""
#Ejercicio_5

En un salón de clase nos pide diseñar un algoritmo que permita determinar el porcentaje
de varones y el porcentaje de mujeres …. Cantidad de Niños 50 - Niñas 20. (tener en cuenta
constante).

#Solución

print("En la clase hay 70 personas en total, 50 niños y 20 niñas")

NIÑOS = 50
NIÑAS = 20

PORCENTAJENIÑOS = NIÑOS * 100 / 70
PORCENTAJENIÑAS = NIÑAS * 100 / 70

print(f"El porcentaje de niños en la clase es de {round(PORCENTAJENIÑOS, 1)}%")
print(f"El porcentaje de niñas en la clase es de {round(PORCENTAJENIÑAS, 1)}%")

"""

"""
#Ejercicio_6

Determina su área y volumen de un cilindro, aplicando un radio ingresando su valor por
teclado y también su altura. Formula área = 2 *pi*r*h y el volumen = pi *(r*r)*h. (tener en
cuenta constante).

#Solución

import math

r = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cilindro: "))

PI = math.pi

area = 2 * PI * r * (r + h) 
volumen = PI * r**2 * h

print(f"El area del cilindro es de {round(area,2)} y su volumen es de {round(volumen,2)}")

"""

"""
#Ejercicio_7

Diseñar un algoritmo que lea por consola el valor de una factura, en este caso aplicaremos
un IVA 19% (Colombia)(0.19). (tener en cuenta constante).

#Solución

factura = float(input("Digite el valor de su factura: "))

IVA = 0.19

facturaConIva = factura * IVA

print(f"Su factura sin iba tendria un costo de {factura}, Mientras que con IVA incluido quedará con un costo de {facturaConIva}")

"""

"""
#Ejercicio_8

Defina un algoritmo que permita calcular la nota final de un alumno, teniendo en cuenta
que ha realizado 3 evaluaciones y que cada evaluación está sometida a un porcentaje , el
cual es:
La primera nota tiene un peso de 25%
La segunda nota tiene un peso de 45%
La tercera nota tiene un peso de 30%

#Solución

nota1 = float(input("Ingrese la primera nota de la evaluación"))
nota2 = float(input("Ingrese la segunda nota de la evaluación"))
nota3 = float(input("Ingrese la tercer nota de la evaluación"))

"""

"""
#Ejercicio_9

Defina un algoritmo que permita calcular el nuevo salario de un trabajador si a este le
incrementaron su sueldo en un 25% adicional a su sueldo anterior.

#Solución

salarioAnterior = float(input("Ingrese su salario anterior: "))

salarioNuevo = 125 * salarioAnterior / 100

print(f"Su salario nuevo será de {salarioNuevo}")

"""

"""
#Ejercicio_10

Un estudiante desea saber cuál será su calificación final en la materia de Informática, dicha
calificación se compone por 3 porcentajes , a su vez cada porcentaje tiene cierta cantidad
de notas, primero diremos los siguiente:
La nota de los 3 primeros exámenes parciales tiene un peso de 55%.
La nota del examen final tiene un peso de 30%.
La nota del trabajo final tiene un peso de 15%.
Hallar la calificación final de todas notas10.

#Solución
"""

"""
#Ejercicio_11

Se tiene un trabajador que se gana de sueldo $43000 el día, durante 25 días laborables, se
necesita hallar cuanto es el sueldo y cuanto se aporta a pensión con el 7.7 %, compuesto
así:
5 % pensión
0.3 % administración fonda
2.4 % seguro de discapacidad.

#Solución
"""


