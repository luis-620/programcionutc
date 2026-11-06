#suma pares
numero=int(input("ingrese un numero:"))
suma=0
for i in range(0,numero+1,2):
    print(i ,end=" ")
    suma+=i
print(f"la suma de los numeros pares es: {suma}")