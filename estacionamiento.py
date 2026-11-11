#Autor: Luis Yugsi
#Fecha: 10/11/2026
#Tema:estacionamiento
disponibles = 50
while True:
 print("Bienvenido al estacionamiento")
 print("1. Consultar espacios disponibles")
 print("2. ingresar vehículo")
 print("3. retirar vehículo")
 print("4. Salir")
 opcion=int(input("Seleccione una opción: "))
 match opcion:
     case 1:
            print(f"""******************************
            Espacios disponibles: {disponibles}
            *******************************""")
     case 2:
         if disponibles>0:
             disponibles-=1
             print(f"""******************************
                Vehículo ingresado. Espacios disponibles: {disponibles}
                *******************************""")
     case 3:
         if disponibles<10:
             disponibles+=1
             print(f"""******************************
                   Vehículo retirado. Espacios disponibles: {disponibles}
                   *******************************""")
     case 4:
            print("Gracias por usar el estacionamiento.")
            break