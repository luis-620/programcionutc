#Universidad Tecnica de Cotopaxi
#Nombre: Luis Yugsi
#Problema: Ingresar 8 números, separarlos en pares e impares, ordenarlos y sumar cada grupo
#Fecha: 19/11/2026

pares = []
impares = []

for i in range(8):
    num = int(input(f"Ingrese el número {i + 1}: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()

print("Números pares:", pares)
print("Suma de pares:", sum(pares))
print("Números impares:", impares)
print("Suma de impares:", sum(impares))
