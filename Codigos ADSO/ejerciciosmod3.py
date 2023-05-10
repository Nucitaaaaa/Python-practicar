
#Condicionales

#if 

ramdom = int(input("Digita cualquier numero: "))

if ramdom > 100000:
    print("Un numero gigante")

#if_else

numero = int(input("Digita tu edad: "))

if numero % 2 == 0:
    print("Tu Edad Es Un Numero Par")
else:
    print("Tu Edad Es Un Numero Impar")


#if_elif_else

print("Bienvenido, hay 4 clases de boletas:\12n1-Normal\n2-Vip\n3-Super-vip\n4-Suprema\n")

tipo_boleta = int(input("Digita el numero correspondiente al tipo de boleta que gustas adquirir: "))
num_boleta = int(input("Digita el numero de boletas que vas a adquirir: "))

if tipo_boleta == 1:
    precio_boleta = 250000 * num_boleta
elif tipo_boleta == 2:
    precio_boleta = 500000 * num_boleta
elif tipo_boleta == 3:
    precio_boleta = 750000 * num_boleta
elif tipo_boleta == 4:
    precio_boleta = 1000000 * num_boleta
else:
    print("Digite un tipo de boleta valido")

print("El precio a pagar por adquirir", num_boleta, "será de:", precio_boleta)

#Bucles

#while

menu = 0

while menu == 0:
    
    #Instrucciones
    print("Calculadora Basica\n")
    print("Digite:\n\n1 Para suma\n2 Para resta\n3 Para multiplicación\n4 Para división\n5 Para division residual\n9 Para salir de la calculadora\n")

    #fin_bucle_si
    operacion = int(input("Digite el numero de la operación a realizar: "))
    if operacion == 9:
        print("Gracias por usar esta calculadora")
        break
    elif operacion != 1 or 2 or 3 or 4 or 5:
        print("\nDigite un numero de operación valido")
        print(" ")

    #operaciones
    num1 = int(input("Digite el primer numero: "))
    num2 = int(input("Digite el segundo numero: "))

    if operacion == 1:
        suma = num1 + num2
        print("\nEl resultado de la suma es:", suma)
        print(" ")
    elif operacion == 2:
        resta = num1 - num2
        print("\nEl resultado de la resta es:", resta)
        print(" ")
    elif operacion == 3:
        multi = num1 * num2
        print("\nEl resultado de la multiplicación es:", multi)
        print(" ")
    elif operacion == 4:
        divi = num1 / num2
        print("\nEl resultado de la división es:", divi)
        print(" ")
    elif operacion == 5:
        resi = num1 % num2
        print("\nEl resultado de la division en base a su residuo es:", resi)
        print(" ")

#for 

num = 0

for i in range (15):
    print(i)

#Ejercicio_sebastian

print("Bienvenido, este programa tiene el fin de mostrarle algunas combinaciones de colores\n")

color = str(input("Ingrese el color inicial, ingrese A para elegir Azul, o R para elegir Rojo: "))
color2 = str(input("Ingrese el segundo color a mezclar, ingrese V para elegir Verde, o AM para elegir Amarillo: "))

if color == "A" and color2 == "V":
    print("La combinación de estos colores dará como resultado el color Azul Verdoso")
elif color == "A" and color2 == "AM":
    print("La combinación de estos colores dará como resultado el color Verde")
elif color == "R" and color2 == "V":
    print("La combinación de estos colores dará como resultado el color Marrón")
elif color == "R" and color2 == "AM":
    print("La combinación de estos colores dará como resultado el color Naranja")
else:
    print("seleccione una combinación valida")


#Ejercicio_edad

edad = int(input("Digite su edad: "))

if edad > 0 and edad < 17:
    print("No puede salir")
elif edad > 17 and edad < 29:
    print("Puede salir dos horas")
elif edad > 29:
    print("Puede salir y volver cuando quiera")
else:
    print("Digite una edad correcta")


#bucles

for i in range(1,31):
    if i % 2 != 0:
        print(i)

i = 2

while i < 32:
    print(i)
    i += 2



for i in range(1,21):
    print("El numero es", i)
    i += 1
print("La suma de todos será:", i*10)




















