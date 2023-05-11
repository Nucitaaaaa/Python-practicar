
#Ejercicio_1

#Mi_Forma
a = float(input("digite el primer num: "))
b = float(input("digite el segundo num: "))
c = float(input("digite el tercer num: "))

resultado = (a ** 3) * ((b ** 2) - 2 * a * c) / 2 * b

print(resultado) #Quedo mal xd


#Solucion
a = float(input("digite el primer num: "))
b = float(input("digite el segundo num: "))
c = float(input("digite el tercer num: "))

resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)

print(resultado)