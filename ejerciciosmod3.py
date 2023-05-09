"""
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

"""


















