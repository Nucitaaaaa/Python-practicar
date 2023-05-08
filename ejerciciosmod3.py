
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