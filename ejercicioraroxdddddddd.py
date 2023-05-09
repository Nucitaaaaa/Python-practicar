
"""
color = input("Selecciona un color: A o a para azul, R o r para rojo: ")

if color == "A" or "a":
    color2 = input("Selecciona el segundo color: V o v para verde, AM o am para amarillo: ")
    if color2 != "V" or "v":
        print("La combinación de los colores será azul verdoso")
    elif color2 != "AM" or "am":
        print("La combinación de los colores será verde")
else:
    print("Imprima un color valido")

if color == "R" or "r":
    color2 = input("Selecciona el segundo color: V o v para verde, AM o am para amarillo: ")
    if color2 != "V" or "v":
        print("La combinación de los colores será marrón")
    elif color2 != "AM" or "am":
        print("La combinación de los colores será morado")
else:
    print("Imprima un color valido")

edad = int(input("Digite su edad: "))

if edad > 0 <= 18:
    print("No puede salir")
elif edad >= 18 <= 31:
    print("Puede salir dos horas")
elif edad > 31:
    print("Puede salir xd")
else:
    print("error")

sueldo = float(input("Digite su sueldo actual: "))
if sueldo < 1000:
    bonificacion = sueldo * 10 / 100
    print("Tiene una bonificación de $" + str(bonificacion), "por lo que su sueldo será de $" + str(sueldo + bonificacion))
elif sueldo > 1000 and sueldo < 2000:
    bonificacion = sueldo * 20 / 100
    print("Su sueldo será de $" + str(sueldo - bonificacion))
elif sueldo > 2000 and sueldo < 5000:
    bonificacion = sueldo * 20 / 100
    print("Su sueldo será de $" + str(sueldo - bonificacion))


for i in range(1,31):
    if i % 2 != 0:
        print(i)

i = 2

while i < 32:
    print(i)
    i += 2

"""


for i in range(1,21):
    print("El numero es", i)
    i += 1
print("La suma de todos será:", i*10)