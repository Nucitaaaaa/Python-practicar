
beatles = []
print("Paso 1:", beatles)

beatles = beatles.append(["John Lennon","Paul McCartney","George Harrison"])

print("Paso 2:", beatles)

i = 0 

for i in beatles:
    print("Escriba\"Stu Sutcliffe\" y \"Pete Best\" para incluirlos en la lista")
    stu = input()
    pete = input()
    beatles = beatles.append(stu, pete)
print("Paso 3:", beatles)

del beatles[3,4]
print("Paso 4:", beatles)

beatles = beatles.insert("Ringo Starr", 0)
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))