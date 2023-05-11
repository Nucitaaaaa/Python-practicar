
"""
#Ejercicio_1

edad = int(input("Digite su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

#Ejercicio_2

contraseña = input("Digite una contraseña: ")
contraseña_pregunta = input("Digite la contraseña que ha digitado anteriormente: ")

if contraseña == contraseña_pregunta.lower():
    print("Su contraseña es correcta")
else:
    print("Su contraseña es incorrecta")

#Ejercicio_3

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if num2 == 0:
    print("Error: el divisor no puede ser igual a 0")
else:
    division = num1 // num2
    print("El resultado de su division es:", division)

#Ejercicio_4

num = int(input("Digite un numero: "))

if num % 2 == 0:
    print(num, "es un numero par")
else:
    print(num, "es un numero impar")

#Ejercicio_5

edad = int(input("Digite su edad: "))
num = int(input("Digite su ingreso mensual: "))

if edad >= 18 and num >= 1000:
    print("Usted debe tributar")
else:
    print("Usted no debe tributar")

#Ejercicio_6

letra_nombre = str(input("Digite su nombre: "))
sexo = str(input("Digite su sexo(M O H): "))

if sexo == "M":
    if letra_nombre.lower() < "m":
        print("Usted pertenece al grupo A")
    else:
        print("Usted pertenece al grupo B")
elif sexo == "H":
    if letra_nombre.lower() > "n":
        print("Usted pertenece al grupo A")
    else:
        print("Usted pertenece al grupo B")

#Ejercicio_7

renta_anual = int(input("Digite su ingreso anual: "))

if renta_anual < 10000:
    print("Su valor impositivo será del 5%")
elif renta_anual > 10000 and renta_anual < 20000:
    print("Su valor impositivo será del 10%")
elif renta_anual > 20000 and renta_anual < 35000:
    print("Su valor impositivo será del 20%")
elif renta_anual > 35000 and renta_anual < 60000:
    print("Su valor impositivo será del 30%")
else:
    print("Su valor impositivo será del 45%")
    
#Ejercicio_8

paga = 2400
puntuacion = float(input("Digite su puntuación: "))

if puntuacion == 0.0:
    rendimiento = "inaceptable"
    print("Su rendimiento ha sido", rendimiento, "Por lo que su paga será de $" + str(paga))
elif puntuacion == 0.4:
    rendimiento = "aceptable"
    paga = paga * 40 / 100
    print("Su rendimiento ha sido", rendimiento, "Por lo que su paga será de $" + str(paga))
elif puntuacion == 0.6:
    rendimiento = ""
    paga = paga * 60 / 100
    print("Su rendimiento ha sido", rendimiento, "Por lo que su paga será de $" + str(paga))
else:
    print("Digite una puntuacion valida")

#Ejercicio_9

edad = int(input("Digite su edad: "))

if edad < 4:
    print("Su entrada será gratuita")
elif edad >=4 and edad <= 18:
    print("Su entrada costará 5€")
else:
    print("Su entrada costará 10€")
    
"""

#Ejercicio_10

pizzaCliente = 0

while pizzaCliente != "Salir":
    
    ingredientesVegetarianos = ["Pimiento","Tofu"]
    ingredientesNoVegetarianos = ["Peperoni","Jamón","Salmón"]
    ingredientesNormales = ["Mozzarella","Tomate"]

    print("\nBievenido, contamos con:\n\n-Pizza Vegetariana\n-Pizza No Vegetariana\n\nPara salir de la pizzeria, escriba \"Salir\"\n")

    pizzaCliente = str(input("que tipo de pizza quiere?: "))

    if pizzaCliente == "Pizza Vegetariana":
        print(f"\nPara Pizza Vegetariana contamos con los siguientes ingredientes:\n\n-{ingredientesVegetarianos[0]}\n-{ingredientesVegetarianos[1]}")
        ingredienteElegido = str(input("\nQue ingrediente va a agregar?: "))
        if ingredienteElegido == ingredientesVegetarianos[0]:
            print(f"\nHa elegido la Pizza vegetariana numero 1, la cual tendrá de ingredientes normales {ingredientesNormales[0]} y {ingredientesNormales[1]}, y de ingrediente especial tendrá {ingredientesVegetarianos[0]}.")
        elif ingredienteElegido == ingredientesVegetarianos[1]:
            print(f"\nHa elegido la Pizza vegetariana numero 2, la cual tendrá de ingredientes normales {ingredientesNormales[0]} y {ingredientesNormales[1]}, y de ingrediente especial tendrá {ingredientesVegetarianos[1]}.")
        else:
            print("\nEscoge un ingrediente valido")
    elif pizzaCliente == "Pizza No Vegetariana":
        print(f"\nPara Pizza No Vegetariana contamos con los siguientes ingredientes:\n\n-{ingredientesNoVegetarianos[0]}\n-{ingredientesNoVegetarianos[1]}\n-{ingredientesNoVegetarianos[2]}")
        ingredienteElegido = str(input("\nQue ingrediente va a agregar?: "))
        if ingredienteElegido == ingredientesNoVegetarianos[0]:
            print(f"\nHa elegido la Pizza no vegetariana  numero 1, la cual tendrá de ingredientes normales {ingredientesNormales[0]} y {ingredientesNormales[1]}, y de ingrediente especial tendrá {ingredientesNoVegetarianos[0]}.")
        elif ingredienteElegido == ingredientesNoVegetarianos[1]:
            print(f"\nHa elegido la Pizza no vegetariana numero 2, la cual tendrá de ingredientes normales {ingredientesNormales[0]} y {ingredientesNormales[1]}, y de ingrediente especial tendrá {ingredientesNoVegetarianos[1]}.")
        elif ingredienteElegido == ingredientesNoVegetarianos[2]:
            print(f"\nHa elegido la Pizza no vegetariana numero 3, la cual tendrá de ingredientes normales {ingredientesNormales[0]} y {ingredientesNormales[1]}, y de ingrediente especial tendrá {ingredientesNoVegetarianos[2]}.")
        else:
            print("\nEscoge un ingrediente valido")
    elif pizzaCliente == "Salir":
        print("\nGracias por comprar")
        break
    else:
        print("\nEscoge un tipo de pizza valida")