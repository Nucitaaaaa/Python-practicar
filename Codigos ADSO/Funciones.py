
#Ejercicio_Explicación_Funciones


#Sin_Parametros

def nombre(): #Se define el nombre de la función
    print(f"El nombre de mi perro es shiro") #Se le da la instrucción de qué debe hacer cuando se llame la función 

nombre() #Se llama la función 


#Con_Parametros

num1 = int(input("Ingrese el primer numero: ")) #Se declara la primera variable en la que se almacenará un numero entero 
num2 = int(input("Ingrese el primer numero: ")) #Se declara la segunda variable en la que se almacenará un numero entero 

def calc (suma,resta,mult,divi): #Se define la función con 4 parametros que representan las 4 operaciónes basicas
    
    print(f"Suma = {suma}, Resta = {resta}, Multiplicación = {mult}, División = {divi}") #Se le da la instrucción de qué debe hacer cuando se llame la función 

calc (num1 + num2, num1 - num2, num1 * num2, round(num1 / num2,2)) #Se llama la función con lor argumentos que adquiere cada parametro 


#Con_Parametros2

def message(pais = "colombia", ciudad = "Ibagué"): #Se define la función con dos parametros los cuales tienen valores por defecto 
    print(f"Tu pais es {pais} tu ciudad es {ciudad}") #Se le da la instrucción de qué debe hacer cuando se llame la función 

message() #Se llama la función sin argumentos 
message("inglaterra") #Se llama la función con 1 argumento 
message("Mexico","Guadalajara") #Se llama la función con 2 argumentos 


#return

numero = int(input()) #Se declara la primera variable en la que se almacenará un numero entero 
def es_par(numero): #Se define una función con un parametro el cual representa el numero ingresado por el usuario 
    if numero % 2 == 0: #Se declara una condicional con respecto a el parametro/variable que ingresa el usuario
        return "es par" #Se da la instrucción de que hacer si la condición se cumple 
    else:
        return "Es impar"  #Se da la instrucción de que hacer si la condición no se cumple 

resultado = es_par(numero) #Se declara una variable la cual almacena el llamado a la función 
print(resultado) #Se hace un print del resultado del condicional 


#return2

def mult(x): #Se define una función con un parametro el cual representa un numero entero 
    d = x * 2  #Se le da la instrucción de qué debe hacer cuando se llame la función 
    t = x * 3 
    return d, t 
doble, triple = mult(5) #Se declaran 2 variables las cuales tienen como valor el resultado de la ejecución de la función
print(doble, triple) #Se hace un print del valor de las dos variables 

















def suma(a, b):
    resultado = a + b
    resultado2= b + a 
    return resultado

resultado_suma = suma(3, 4)
print(resultado_suma)















