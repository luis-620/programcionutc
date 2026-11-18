
# Universidad Tecnica de Cotopaxi
# Nombre: Luis Yugsi
# Tema: Control de entrada y salida de vehiculos

# Guardamos la capacidad maxima del parqueadero
capacidad = 50

# Contamos los vehiculos que estan estacionados
total = 0

# Repetimos el menu hasta que el usuario decida salir
while True:

    # Mostramos las opciones del sistema
    print("===== PARQUEADERO UTC =====")
    print("1. Ingresar vehiculo")
    print("2. Consultar vehiculos")
    print("3. Sacar vehiculo")
    print("4. Terminar")

    # Pedimos que el usuario elija una opcion
    opcion = int(input("Elija una opcion: "))

    # Revisamos la opcion seleccionada
    match opcion:

        # Opcion 1: Ingresar un vehiculo
        case 1:

            # Verificamos si hay espacio disponible
            if total < capacidad:

                # Sumamos un vehiculo al parqueadero
                total += 1

                # Mostramos el resultado del ingreso
                print("Ingreso realizado correctamente.")
                print("Vehiculos estacionados:", total)

            else:

                # Avisamos que el parqueadero esta lleno
                print("No hay espacio disponible.")

        # Opcion 2: Consultar el parqueadero
        case 2:

            # Calculamos los espacios que quedan libres
            espacios = capacidad - total

            # Mostramos la informacion actual
            print("Vehiculos estacionados:", total)
            print("Espacios disponibles:", espacios)

        # Opcion 3: Retirar un vehiculo
        case 3:

            # Comprobamos que exista algun vehiculo
            if total > 0:

                # Restamos un vehiculo del contador
                total -= 1

                # Informamos que la salida fue correcta
                print("Salida realizada correctamente.")
                print("Espacios disponibles:", capacidad - total)
                 #resta los vehículos ocupados a la capacidad total.
            else:

                # Avisamos que el parqueadero esta vacio
                print("No hay vehiculos para retirar.")

        # Opcion 4: Finalizar el programa
        case 4:

            # Mostramos un mensaje de despedida
            print("Gracias por utilizar el parqueadero UTC.")

            # Detenemos el ciclo
            break

        # Si el usuario escribe una opcion incorrecta
        case _:

            # Mostramos un mensaje de error
            print("Opcion incorrecta. Intente nuevamente.")
