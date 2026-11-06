#Uiversidad Tecnica de Cotopaxi
#Nombre:Luis Yugsi
#Funcion para sumar los números pares hasta el número ingresado y ordenar 10 números diferentes de menor a mayor y de mayor a menor
#Fecha: 20/06/2024

# ingresar 10 numero diferentes y ordenarlos de menor a mayor y otro de mayor a menor
numeros = []    
for _ in range(10):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

numeros.sort()  # Ordenar de menor a mayor
print("Números ordenados de menor a mayor:")
print(numeros)

numeros.sort(reverse=True)  # Ordenar de mayor a menor
print("Números ordenados de mayor a menor:")
print(numeros)
print(f"Maximo:{max(numeros)}")
print(f"Minimo:{min(numeros)}")