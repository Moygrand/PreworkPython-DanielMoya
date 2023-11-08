'''
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''
#Ejercicio 1
lista=[1,2,3,4,5,6,7,8,9,10]
for num in lista:
  print(num)
#Ejercicio 2
contador=0
while contador!=20:
  contador+=2
  print(contador)
#Ejercicio 3
contador2=0
suma=2
total=1
while contador2!=99:
  contador2+=1
  print(f"{total}+{suma}={total+suma}")
  total+=suma
  suma+=1