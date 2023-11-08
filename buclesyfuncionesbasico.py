'''1. Crea una función para verificar si un número es par o impar y devuelva “El
número es par” o “El número es impar” según corresponda.

2. Crea una función a la que pases un número como argumento, calcule el factorial
de ese número y haga print del resultado.

3. Crea una función a la que se le pase un número como argumento, calcule la
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado
total de dígitos.

4. Dada una lista de números, crea una función que devuelva el número máximo
de la lista.

5. Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado.

6. Dados dos números, crea una función para encontrar el mínimo común múltiplo
(MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM.

7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el
área de un triángulo.

8. Crea una función que, dado un número, verifique si un número es positivo,
negativo o cero.

9. Crea una función que, dada una palabra, cuente la cantidad de letras en una
palabra.

10. Crea una función que, dada una lista de números, convierta la lista de números
a su valor absoluto.

11. Crea una función que, dado un número, verifique si un número es primo.

12. Dados dos números, crea una función para encontrar el máximo común divisor
(MCD) de esos dos números.'''

#Definición de funciones
def inputint():
  try: 
    num=int(input())
    return num
  except:
      print('\nNo se ha introducido un numero')
      return 'err'
    
def parimpar():
  print('Introduce un número: ')
  num=inputint()
  if num!= 'err':
    if divmod(num,2)[1]==0:
      print(f"El número {num} es par")
    else: print(f"\n\nEl número {num} es impar\n\n")
  else: print('Error en la introducción de datos\n')
  
def factorial(num1):
  if num1!='err':
    cont=1
    total=1
    while cont != num1+1:
      total *= cont
      cont+=1
    print(f'\n\nEl factorial de {num1} es {total}\n\n')
  else: print('Error en la introducción de datos\n')

def calcdigit(num1):
  if num1!='err':
    print(f'El número de digitos es: {len(num1)}')
  else: print('Error en la introducción de datos')
  
def sumalista(num1):
  if num1!='err':
    max=0
    for numactual in num1:
      if numactual>max: max=numactual
    print (f'El número máximo es: {max}')
  else: print('Error en la introducción de datos')
  
def crearlista():
  num=True
  lista=[]
  while num!=0:
    print('\nIntroduce un número, 0 para terminar la lista: ')
    num=inputint()
    if num!='err' and num!=0: lista.append(num)
  return lista

def sumadigit(num1):
  if num1!='err':
    total=0
    for digit in str(num1):
      total+=int(digit)
    return total
  else: print('Error en la introducción de datos')
  
def mcm():
  print('\nIntroduce un número: ')
  num1=inputint()
  print('\nIntroduce el segundo número:')
  num2=inputint()
  if num1!=0 and num2!=0 and num1!='err' or num2!='err':
     total=max(num1, num2)
     while True:
        if total % num1==0 and total%num2==0:
         return total
        total+=1
  elif num1=='err' or num2=='err': print('Error en la introducción de datos')
  else: return 0

def areatriangulo(base,altura):
  if base or altura != 'err':
    area=int(base*altura/2)
    return area
  else: print('Error en la introducciónd de datos')

def signo(num):
  if num > 0:
    return 'positivo'
  elif num <0:
    return 'negativo'
  else: return 0
  
def contword(word):
  cont=0
  for letra in word: 
    if letra.isalpha(): 
      cont += 1 
  return cont

def absoluto(lista):
  for pos in range(len(lista)):
      lista[pos] = abs(lista[pos]) 
  return lista

def primo(num1):
  cont=1
  while cont!=num1+1:
    if divmod(num1,cont)[1]==0 and cont!=1 and num1!=cont:
      return False
    cont+=1
  return True

def mcd():
  print('\nIntroduce un número: ')
  num1=inputint()
  print('\nIntroduce el segundo número:')
  num2=inputint()
  if num1!=0 and num2!=0 and num1!='err' or num2!='err':
      while num2: 
        num1, num2 = num2, num1 % num2 
      return num1
  elif num1=='err' or num2=='err': print('Error en la introducción de datos')

#Llamada y resolución de funciones
eleccion=404
while eleccion!=99:
  eleccion = int(input('\n\n 1: Verificar número par/impar \n 2: Cálculo de factorial \n 3: Cálculo de número de digitos\n 4: Número máximo \n 5: Suma de dígitos \n 6: Calcular MCM \n 7: Calcular area triangulo \n 8: Para o impar \n 9: Calcular número de digitos en palabra \n 10: Convertir listado a valor absoluto \n 11: Comprobar número primo \n 12: Calcular MCD \n 99: Salida\n Introduce opción: '))
  if eleccion==1: parimpar()
  elif eleccion==2: 
    print('Introduce un numero para calcular factorial: ')
    factorial(inputint())
  elif eleccion==3:
    print('Introduce un numero para calcular número de dígitos: ')
    calcdigit(input())
  elif eleccion==4: sumalista(crearlista())
  elif eleccion==5: 
    print('\nIntroduce un número para sumar sus dígitos: ')
    print(f'\nLa suma de los digitos es {sumadigit(inputint())}')
  elif eleccion==6:
    print(f'El MCM es: {mcm()}')
  elif eleccion==7:
    print(f'\nIntroduce la base del triangulo: ')
    num1=inputint()
    print('\nIntroduce la altura del triangulo: ')
    num2=inputint()
    print(f'\nEl area del triangulo es: {areatriangulo(num1,num2)}')
  elif eleccion==8:
    print('Introduce un número: ')
    num1=inputint()
    print(f'El número {num1} es {signo(num1)}')
  elif eleccion==9:
    word=input('Introduce una palabra: ')
    print(f'\n {word} contiene {contword(word)} letras')
  elif eleccion==10:
    lista=absoluto(crearlista())
    print(lista)
  elif eleccion==11:
    print('Introduce un número: ')
    num1=inputint()
    if primo(num1)==True:
      print (f'El número {num1} es primo')
    else: print(f'El número {num1} no es primo')
  elif eleccion==12:
     print(f'El MCD es: {mcd()}')
  elif eleccion==99:
    print('Salida del programa exitosa')
  else:
    print('Me fui a la puta')