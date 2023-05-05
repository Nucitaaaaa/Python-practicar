
#var_menu
menu = 0

#Bucle_menu
while menu == 0:
    
    #Instrucciones
    print("Calculadora Basica\n")
    print("Digite:\n\n1 Para suma\n2 Para resta\n3 Para multiplicación\n4 Para división\n5 Para division residual\n9 Para salir de la calculadora\n")

    #fin_bucle_si
    operacion = int(input("Digite el numero de la operación a realizar: "))
    if operacion == 9:
        print("\nGracias por usar esta calculadora")
        break
    elif operacion != 1 or 2 or 3 or 4 or 5:
        print("\nDigite un numero de operación valido")
        break
    else:
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
