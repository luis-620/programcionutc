
# Universidad Tecnica de Cotopaxi
# Nombre: Luis Yugsi
# Tema: Sistema de control de ingreso y salida de vehiculos
# Capacidad maxima: 50 vehiculos

# Se establece la capacidad total del parqueadero
capacidad = 50

# Variable que cuenta los vehiculos que estan dentro
vehiculos = 0

# Ciclo que permite mostrar el menu hasta que el usuario decida salir
while True:

    print("-----------------------------------")
    print("""       PARQUEADERO UTC
          
          1. Registrar ingreso
          2. Registrar salida
          3. Ver espacios libres
          4. Finalizar programa
          """)
    
    # Se solicita al usuario seleccionar una opcion
    opcion = int(input("Seleccione una opcion: "))

    print("-----------------------------------")

    # Se utiliza match para comprobar la opcion seleccionada
    match opcion:

        case 1:
            # Verifica si todavia existe espacio disponible
            if vehiculos < capacidad:
                vehiculos += 1
                print("Ingreso registrado correctamente.")
                print(f"Espacios disponibles: {capacidad - vehiculos}")
            else:
                # Se muestra un mensaje cuando ya no hay espacio
                print("El parqueadero ha alcanzado su capacidad maxima.")

        case 2:
            # Comprueba que exista al menos un vehiculo para retirar
            if vehiculos > 0:
                vehiculos -= 1
                print("Salida del vehiculo registrada.")
                print(f"Espacios libres actualmente: {capacidad - vehiculos}")
            else:
                # Evita retirar un vehiculo cuando el parqueadero esta vacio
                print("El parqueadero se encuentra vacio.")

        case 3:
            # Calcula los espacios que todavia estan disponibles
            disponibles = capacidad - vehiculos
            print(f"Actualmente hay {vehiculos} vehiculos estacionados.")
            print(f"Quedan {disponibles} espacios libres.")

        case 4:
            # Termina el ciclo y cierra el programa
            print("Sistema finalizado. Gracias por utilizar el parqueadero UTC.")
            break

        case _:
            # Se ejecuta cuando se ingresa una opcion diferente
            print("Opcion no valida. Intente nuevamente.")
