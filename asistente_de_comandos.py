ids = []
comandos = []
descripciones = []
tipos = []
instrucciones = []
estados = []
fechas = []
autores = []
observaciones = []
#------------------------------------------#
#--|menu_principal_asistente_de_comandos|--#
#------------------------------------------#
while True:
    print("menu principal asistente de comandos")
    print("1) registrar comando")
    print("2) editar comando")
    print("3) eliminar comando")
    print("4) buscar comando")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|registrar_comando|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_comando = 1
        else:
            id_comando = ids[-1] + 1
        comando = input("nombre del comando: ")
        descripcion = input("descripción: ")
        tipo = input("tipo de comando: ")
        instruccion = input("instrucción: ")
        estado = input("estado (activo o inactivo): ")
        fecha = input("fecha de creación: ")
        autor = input("autor: ")
        observacion = input("observación: ")
        ids.append(id_comando)
        comandos.append(comando)
        descripciones.append(descripcion)
        tipos.append(tipo)
        instrucciones.append(instruccion)
        estados.append(estado)
        fechas.append(fecha)
        autores.append(autor)
        observaciones.append(observacion)
        print("comando registrado correctamente.")
        print("id:", id_comando)
    #--------------------#
    #--|editar_comando|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen comandos registrados.")
        else:
            print("editar comando")
            for i in range(len(ids)):
                print(f"{ids[i]} | {comandos[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del comando: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("comando:", comandos[posicion])
                comandos[posicion] = input("nuevo comando: ")
                descripciones[posicion] = input("nueva descripción: ")
                tipos[posicion] = input("nuevo tipo: ")
                instrucciones[posicion] = input("nueva instrucción: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                autores[posicion] = input("nuevo autor: ")
                observaciones[posicion] = input("nueva observación: ")
                print("comando actualizado correctamente.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_comando|--#
    #----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen comandos registrados.")
        else:
            print("eliminar comando")
            for i in range(len(ids)):
                print(f"{ids[i]} | {comandos[i]}")
            id_buscar = int(input("ingrese la id del comando: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("comando:", comandos[posicion])
                respuesta = input("¿desea eliminar este comando? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    comandos.pop(posicion)
                    descripciones.pop(posicion)
                    tipos.pop(posicion)
                    instrucciones.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    autores.pop(posicion)
                    observaciones.pop(posicion)
                    print("comando eliminado correctamente.")
                else:
                    print("el comando no fue eliminado.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_comando|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen comandos registrados.")
        else:
            print("buscar comando")
            id_buscar = int(input("ingrese la id del comando: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("comando:", comandos[posicion])
                print("descripción:", descripciones[posicion])
                print("tipo:", tipos[posicion])
                print("instrucción:", instrucciones[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("autor:", autores[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen comandos registrados.")
        else:
            activos = 0
            inactivos = 0
            sistema = 0
            utilidad = 0
            consola = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {comandos[i]} | {tipos[i]} | {estados[i]}")
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "inactivo":
                    inactivos += 1
                if tipos[i].lower() == "sistema":
                    sistema += 1
                elif tipos[i].lower() == "utilidad":
                    utilidad += 1
                elif tipos[i].lower() == "consola":
                    consola += 1
            print("estadísticas asistente de comandos")
            print("cantidad de comandos:", len(ids))
            print("activos:", activos)
            print("inactivos:", inactivos)
            print("sistema:", sistema)
            print("utilidad:", utilidad)
            print("consola:", consola)
            nombre_comando = input("ingrese el nombre del comando: ")
            encontrado = False
            for i in range(len(comandos)):
                if comandos[i].lower() == nombre_comando.lower():
                    encontrado = True
                    if estados[i].lower() == "activo":
                        print("instrucción encontrada")
                        print(instrucciones[i])
                    else:
                        print("el comando está deshabilitado.")
                    break
            if encontrado == False:
                print("comando no encontrado.")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el asistente de comandos.")
        break
    else:
        print("opción no válida.")