#conversion de segundos a horas minutos
numero=int(input('ingrese los segundos:')) #ingreso de segundos
horas=numero//3600 #conversion de minutos a horas
resto=numero%3600 #residuo de la division de segundos entre 3600
minutos=resto//60 #conversion de segundos a minutos
segundos=resto%60 #residuo de la division de segundos entre 60
print('los segundos ingresados son:',segundos,'segundos') #imprime los segundos ingresados
print('los minutos ingresados son:',minutos,'minutos') #imprime los minutos
print('las horas ingresadas son:',horas,'horas') #imprime las horas
