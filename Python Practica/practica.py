"""

#Ejercicio_1

print("Hola mundo")


#Ejercicio_2

mensaje = "Hola mundo"

print(mensaje)


#Ejercicio_3

nombre = str(input("Introduce tu nombre: "))

print("Hola,", nombre)



#Ejercicio_4

operacion = (((3 + 2 ) / ( 2 * 5)) ** 2)

print(operacion)


#Ejercicio_5

HorasTrabajadas = float(input("Ingrese el numero de horas que trabaja por dia: "))
CosteHora = float(input("Ingrese el monto que gana por hora trabajada: "))
Paga = HorasTrabajadas * CosteHora

print("Su paga será de:",Paga,"$")


#Ejercicio_6

n = int(input("Ingrese un numero: "))
sumanumeros = n * (n + 1) / 2

print(sumanumeros)


#Ejercicios_7

peso = float(input("Ingrese su peso en kg :"))
estatura = float(input("Ingrese su estatura en Metros :"))
masacorporal = peso / estatura ** estatura

print("su indice de masa corporal es de:",masacorporal)


#Ejercicio_8

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

cociente = num1 // num2
resto = num1 % num2

print("El cociente de", num1, "/", num2, "es", cociente, "y su residuo es de", resto)


#Ejercicio_9

dineroinvertir = float(input("Ingrese la cantidad de dinero que va a inventir: "))
interesanual = float(input("Ingrese el interes anual: "))
años = float(input("Ingrese el numero de años que va a invertir: "))
capital = dineroinvertir * (1 + interesanual/100) ** años

print("Su capital será de:", capital)


#Ejercicio_10

payasos = int(input("Ingrese la cantidad de pasayos en el pedido: "))
muñecas =int(input("Ingrese la cantidad de muñecas en el pedido: "))

peso = (payasos * 112) + (muñecas * 75)

print("El peso total del paquete será de: ", peso, "Kg")

"""

#Ejercicio_11

dinerocuenta = float(input("Ingrese la cantidad de dinero depositada en su cuenta: "))

primeraño = dinerocuenta * ( 1 + 0.04)
segundoaño = primeraño * ( 1 + 0.04)
terceraño = segundoaño * ( 1 + 0.04)

print("Su ahorro en el primer año será de" + " " + str(round(primeraño, 2))) 
print("Su ahorro en el segundo año será de" + " " + str(round(segundoaño, 2))) 
print("Su ahorro en el tercer año será de" + " " + str(round(terceraño, 2))) 