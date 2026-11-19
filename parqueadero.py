
# Autor: Luis Yugsi
# Fecha: 10/11/2026
# Tema: Estacionamiento

disponibles = 50  # Se establece que el estacionamiento tiene 50 espacios disponibles.

while True:  # Permite repetir el menú hasta que el usuario decida salir.

    print("Bienvenido al estacionamiento")  # Muestra el mensaje de bienvenida.
    print("1. Consultar espacios disponibles")  # Opción para consultar los espacios.
    print("2. Ingresar vehículo")  # Opción para ingresar un vehículo.
    print("3. Retirar vehículo")  # Opción para retirar un vehículo.
    print("4. Salir")  # Opción para terminar el programa.

    opcion = int(input("Seleccione una opción: "))  # Solicita al usuario una opción.

    match opcion:  # Comprueba qué opción seleccionó el usuario.

        case 1:  # Si selecciona la opción 1.
            print(f"""******************************
            Espacios disponibles: {disponibles}
            *******************************""")  # Muestra los espacios libres.

        case 2:  # Si selecciona la opción 2.
            if disponibles > 0:  # Comprueba si todavía hay espacios libres.
                disponibles -= 1  # Resta un espacio porque ingresó un vehículo.
                print(f"""******************************
                Vehículo ingresado. Espacios disponibles: {disponibles}
                *******************************""")  # Muestra los espacios restantes.

            else:  # Si ya no existen espacios disponibles.
                print("Estacionamiento lleno.")  # Informa que no puede ingresar otro vehículo.

        case 3:  # Si selecciona la opción 3.
            if disponibles < 50:  # Comprueba si hay vehículos dentro.
                disponibles += 1  # Suma un espacio porque salió un vehículo.
                print(f"""******************************
                Vehículo retirado. Espacios disponibles: {disponibles}
                *******************************""")  # Muestra los espacios disponibles.

            else:  # Si todos los espacios están libres.
                print("No hay vehículos para retirar.")  # Informa que no hay vehículos.

        case 4:  # Si selecciona la opción 4.
            print("Gracias por usar el estacionamiento.")  # Muestra el mensaje de despedida.
            break  # Finaliza el ciclo y termina el programa.

        case _:  # Si selecciona una opción que no existe.
            print("Opción no válida. Intente nuevamente.")  # Muestra un mensaje de error.
