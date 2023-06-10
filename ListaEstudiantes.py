
menu = True
listaEstudiantes = []

while menu == True:
    print("\nIngrese el numero de lo que va a realizar:\nEscriba:\n1 Para agregar un estudiante\n2 Para mostrar los estudiantes\n3 Para eliminar un estudiante")
    elec = int(input("\nIngrese el numero aquí: "))

    if elec == 1:
        name = input("\nIngrese el nombre del estudiante aquí: ")
        lstName = input("\nIngrese el apellido del estudiante aquí: ")
        doc = int(input("\nIngrese el documento de identidad del estudiante del estudiante aquí: "))
        listaEstudiantes.append(name)
        listaEstudiantes.append(lstName)
        listaEstudiantes.append(doc)

    elif elec == 2:
        if listaEstudiantes:
            for i in range(0, len(listaEstudiantes), 3):
                print(f"\nEstudiante:\nNombre: {listaEstudiantes[i]} \nApellido: {listaEstudiantes[i+1]} \nDocumento: {listaEstudiantes[i+2]}")
        else: 
            print("No hay estudiantes")

    elif elec == 3:
        docu = int(input("\nIngrese el documento del estudiante a eliminar: "))
        for i in range(0,len(listaEstudiantes),3):
            if listaEstudiantes[i+2] == docu:
                listaEstudiantes.pop(i)
                listaEstudiantes.pop(i)
                listaEstudiantes.pop(i)
            else:
                print("El estudiante no se encuentra")

    elif elec == 9:
        break 

    else:
        print("Ingrese una opcion correcta")