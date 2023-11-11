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

#Funciones útiles fuera de ejercicio
def reversalstring(word):
  anedac=''
  for actual in word:
    anedac= actual+anedac
  return anedac

def inputint():
  try: 
    num=int(input())
    return num
  except:
      print('\nNo se ha introducido un numero')
      return 'err'

def crearlista():
  num=True
  lista=[]
  while num!=0:
    print('\nIntroduce un número, 0 para terminar la lista: ')
    num=inputint()
    if num!='err' and num!=0: lista.append(num)
  return lista
def crearlistastring():
  num=True
  lista=[]
  while num:
    print('\nIntroduce un string, intro para terminar la lista: ')
    num=input()
    if num: lista.append(num)
  return lista
#Ejercicio 1
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
  else: print('Nada que listar')
  return list
#Ejercicio 2
def divisores(n):
  listadiv=[]
  divisor=n
  while divisor!=0:
      if n%divisor==0:
        listadiv.append(divisor)
      divisor-=1
  print (listadiv)
#Ejercicio 3
def unica(x):
  flag=True
  pos2=0
  resultado=[]
  for pos in range(len(x)-1):
    flag=False
    for valor in x:
      if x[pos]== valor and pos != pos2: 
        flag=True
      pos2+=1
    if flag==False:
      resultado.append(x[pos])
    pos2=0
  return resultado
#Ejercicio4
def sumadigit(num1):
  if num1!='err':
    total=0
    for digit in str(num1):
      total+=int(digit)
    return total
  else: print('Error en la introducción de datos')
#Ejercicio 5
def sumavocales(cadena):
 total=0
 for caracter in cadena:
    if caracter in 'aeiouAEIOU': total+=1
 return total
#Ejercicio 6
def listarn(lista,n):
  result=[]
  count=0
  for valor in lista:
    result.append(valor)
    if count == n-1: break
    count+=1
  return result
#Ejercicio 7
def calcletras(palabra):
  mayus=0
  minus=0
  for letra in palabra:
    if letra.islower(): minus+=1
    if letra.isupper(): mayus+=1
  result=[mayus,minus]
  return result
#Ejercicio 8
def perfectnumber(num):
  i=0
  total=0
  while i<num-1:
    i+=1
    if num%i==0:
      total+=i
  if total==num:
    return True
  else: return False
#Ejercicio 9 
def binario(num):
    result=''
    while num!=0:
      if num%2!=0:
        result+='1'
      else: result+='0'
      num=int(num/2)
    result=reversalstring(result)
    return result
#Ejercicio 10
def compare(word1, word2):
  result=''
  for caracter in word1:
    if caracter in word2.lower() or caracter in word2.upper():
      result+=caracter
  return result
#Ejercicio 11
def palindromo(word):
  reverse=reversalstring(word)
  word=word.replace(' ', '')
  reverse=reverse.replace(' ','')
  print (word, reverse)
  if word.lower() == reverse.lower(): return True
  else: return False
#Ejercicio 12
def fizzbuzz():
  i=1
  result=[]
  while i<=50:
    if i%3==0 and i%5==0:
      result.append('FizzBuzz')
    elif i%3==0: result.append('Fizz')
    elif i%5==0: result.append('Buzz')
    else: result.append(i)
    i+=1
  return print (result)
#Ejercicio 13
def ordenar(lista):
  lista.sort()
  return lista
#Ejercicio 14
def mayorquen(lista,n):
  result=[]
  for element in lista:
    if len(element)>n: result.append(element)
  return result
#Ejercicio 15
def localfibonacci(num):
  return fibonacci(num)[-1]
#Ejercicio 16
def masgrande(lista):
  return max(lista)
#Ejercicio 17
def sumadigitcubo(num):
  return sum(int(digit)**3 for digit in str(num))
#Ejercicio 18
def segundomasgrande(lista):
  lista.sort()
  return lista[-2]
#Ejercicio 19
def comparecomun(lista1, lista2):
  if compare(lista1, lista2): return True
  else: return False
#Llamamientos
menu=0
print('Ejercicios 1-10(1), ejercicios 11-20(2)')
menu=input()
if menu=='1':
  print ('Introduce un numero: ')
  numero=inputint()
  print(f'Serie de fibonacci: {fibonacci(numero)}')
  print('Listado divisores: ')
  divisores(numero)
  lista=crearlista()
  print (f'Los valores únicos son {unica(lista)}')
  print('Introduce un número: ')
  numero=inputint()
  print(f'La suma de los digitos de {numero} es {sumadigit(numero)}')
  print(f'Escribe una palabra: ')
  palabra=input()
  print(f'{palabra} contiene {sumavocales(palabra)} vocales')
  print('Introduce un número: ')
  numero=inputint()
  lista=crearlista()
  print(listarn(lista, numero))
  calcpal=calcletras(palabra)
  print (f'La palabra {palabra} contiene {calcpal[0]} letras mayúsculas y {calcpal[1]} minúsculas')
  if perfectnumber(numero) is True:
    print(f'El número {numero} es perfecto')
  else: print(f'El número {numero} no es perfecto')
  print (f'{numero} convertido a binario: {binario(numero)}')
  print('Introduce otra palabra: ')
  palabra2=input()
  print (f'Intersección de caracteres de {palabra} y {palabra2} es {compare(palabra,palabra2)}')
elif menu=='2':
  print('Introduce palabra 1: ')
  palabra1 = input()
  if palindromo(palabra1)==True: print('La palabra es un palindromo')
  else: print('La palabra no es un palindromo')
  fizzbuzz()
  lista=crearlista()
  print(f'Lista ordenada: {ordenar(lista)}')
  listastr=crearlistastring()
  print('Introduce un número:')
  n=inputint()
  print(f'Los elementos de esta lista: \n{listastr} \nque son mayores que {n}: \n{mayorquen(listastr,n)}')
  print (f'El número en la lista de fibonacci de {n} es: {localfibonacci(n)}')
  print (f'El número máximo de la lista es: {masgrande(lista)}')
  print(f'La suma de los digitos de {n} al cubo es {sumadigitcubo(n)}')
  print(f'El segundo numero más grande de la lista es {segundomasgrande(lista)}')