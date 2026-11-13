#Programa que realiza operaciones matematicas basicas como suma, resta, multiplicacion y division
#Autor: Luis Yugsi

def operaciones (valor):  #FUNCION QUE RECIBE UN PARAMETRO PARA SUMAR, RESTAR, MULTIPLICAR Y DIVIDIR
    
    if valor == 1: # llama a la funcion suma
        print("Suma")   #mensaje de suma
        num1 = int(input("Ingrese el primer número: ")) #ingreso del primer numero
        num2 = int(input("Ingrese el segundo número: ")) #ingreso del segundo numero
        print("El resultado de la suma es:", num1 + num2)# realiza la suma y muestra el resultado
    elif valor == 2: # llama a la funcion resta
        print("Resta")# mensaje de resta
        num1 = int(input("Ingrese el primer número: "))#ingreso del primer numero
        num2 = int(input("Ingrese el segundo número: "))#ingreso del segundo numero
        print("El resultado de la resta es:", num1 - num2)  #realiza la resta y muestra el resultado    
    elif valor == 3:# llama a la funcion multiplicacion
        print("Multiplicación")# mensaje de multiplicacion
        num1 = int(input("Ingrese el primer número: ")) #ingreso del primer numero
        num2 = int(input("Ingrese el segundo número: "))#ingreso del segundo numero
        print("El resultado de la multiplicación es:", num1 * num2)#realiza la multiplicacion y muestra el resultado
    elif valor == 4:# llama a la funcion division
        print("División")# mensaje de division
        num1 = int(input("Ingrese el primer número: ")) #ingreso del primer numero
        num2 = int(input("Ingrese el segundo número: ")) #ingreso del segundo numero
        if num2 != 0:# verifica que el segundo numero no sea cero para evitar division por cero
            print("El resultado de la división es:", num1 / num2)#realiza la division y muestra el resultado
        else:# si el segundo numero es cero, muestra un mensaje de error
            print("Error: No se puede dividir entre cero.")  #mensaje de error
    """
    Función que recibe un parametro para sumar,restar,multiplicar y dividir.
    """

print("""ingrese un valor a operar: 
      1 para sumar
      2 para restar
      3 para multiplicar
      4 para dividir""")
valor = int(input("Ingrese el valor: "))
operaciones(valor)# Llamada a la función y muestra del resultado
print("final")
print("luis yugsi creador")

