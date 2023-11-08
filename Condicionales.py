'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''

#Ejercicio 1
numero=-1
if numero > 0:
  print(f"El número {numero} es positivo")
else: print(f"El número {numero} es negativo")
#Ejercicio 2
if divmod(numero,2)[1]==0:
  print(f"El número {numero} es par")
else: print(f"El número {numero} es impar")
#Ejercicio 3
numero1=33
numero2=5
numero3=63
if numero1>numero2:
  if numero1>numero3:
    print (f"El mayor es {numero1}")
  else: print (f"El mayor es {numero3}")
elif numero2>numero3:
  print (f"El mayor es {numero2}")
else: print (f"El mayor es {numero3}")
