#promedio
nota1=int(input("ingrese la primera nota:"))   #ingreso de la primera nota
nota2=int(input("ingrese la segunda nota:"))   #ingreso de la segunda nota
nota3=int(input("ingrese la tercera nota:"))    #ingreso de la tercera nota
suma=nota1+nota2+nota3    #calculo de la suma
promedio=suma/3      #calculo del promedio
if promedio>=7: #condicion para aprobar
    print("la nota1 es:",nota1) #imprime la primera nota
    print("la nota2 es:",nota2) #imprime la segunda nota    
    print("la nota3 es:",nota3) #imprime la tercera nota
    print("la suma de las notas es:",suma) #imprime la suma de las notas
    print("el promedio es:",promedio) #imprime el promedio
    print("el estudiante aprobo el curso") #mensaje de aprobación
elif promedio>=5 and promedio<7: #condicion para supletorio
    print("la nota1 es:",nota1) #imprime la primera nota
    print("la nota2 es:",nota2) #imprime la segunda nota    
    print("la nota3 es:",nota3) #imprime la tercera nota
    print("la suma de las notas es:",suma) #imprime la suma de las notas
    print("el promedio es:",promedio) #imprime el promedio
    print("el estudiante debe rendir supletorio") #mensaje de supletorio
else:
    print("la nota1 es:",nota1) #imprime la primera nota
    print("la nota2 es:",nota2) #imprime la segunda nota    
    print("la nota3 es:",nota3) #imprime la tercera nota
    print("la suma de las notas es:",suma) #imprime la suma de las notas
    print("el promedio es:",promedio) #imprime el promedio
    print("el estudiante no aprobo el curso") #mensaje de reprobación
    