#cajero automatico
saldo = 0  # Saldo inicial
while True:
 print("Bienvenido al cajero automático")
 print("1. Consultar saldo")
 print("2. depositar dinero")
 print("3. retirar dinero")
 print("4. Salir")
 opcion=int(input("Seleccione una opción: "))
 match opcion:
     case 1:
         print(f"su saldo es {saldo}")
     case 2:
         try:
             monto = float(input("Ingrese el monto a depositar: "))
             if monto > 0:
                 saldo += monto
                 print(f"Depósito realizado con éxito.su saldo actual es {saldo}")
             else:
                 print("El monto debe ser positivo.")
         except ValueError:
             print("Por favor, ingrese un número válido.")
     case 3:
         try:
             monto = float(input("Ingrese el monto a retirar: "))
             if monto > 0:
                 if saldo >= monto:
                     saldo -= monto
                     print(f"Retiro realizado con éxito.su saldo actual es {saldo}")
                 else:
                     print("Fondos insuficientes.")
             else:
                 print("El monto debe ser positivo.")
         except ValueError:
             print("Por favor, ingrese un número válido.")
     case 4:
         print("Gracias por usar el cajero automático.")
         break
     case _:
         print("Opción no válida. Por favor, seleccione una opción correcta.")