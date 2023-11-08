'''1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.
2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario.
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”.
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.
15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.
16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.
18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.
21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.
22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números
23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.
24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.
26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.
27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.
29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.'''

#Definicion de funciones
def inputint():
  try: 
    num=int(input())
    return num
  except:
      print('\nNo se ha introducido un numero')
      return 'err'
    
def fibonacci(n):
  a=0
  b=1
  c=0
  if n>0:
    n=n-1
    list=[1]
    for num in (range(n)):
      c=b+a
      a=b
      b=c
      list.append(c)
    print (list)
  else: print('Nada que listar')
  
def divisores(n):
  listadiv=[]
  divisor=n
  while divisor!=0:
      if n%divisor==0:
        listadiv.append(divisor)
      divisor-=1
  print (listadiv)
  


#Llamamientos
print ('Introduce un numero: ')
numero=inputint()
print('Serie de fibonacci: ')
fibonacci(numero)
print('Listado divisores: ')
divisores(numero)
