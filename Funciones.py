'''Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Define una función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.'''
numero1 =7
numero2 =25
listanum=[2,4,8,5,1,4]
cadena="Transponder"
#Ejercicio 1
def sumadosnum(num1,num2):
  return num1+num2
print(sumadosnum(numero1,numero2))

#Ejercicio 2
def factorial(num1):
  cont=1
  total=1
  while cont != num1+1:
    total *= cont
    cont+=1
  return total 
print(factorial(numero1))

#Ejercicio 3
def primo(num1):
  cont=1
  while cont!=num1+1:
    if divmod(num1,cont)[1]==0 and cont!=1 and num1!=cont:
      return False
    cont+=1
  return True

if primo(numero1)== True:
  print (f'El número {numero1} es un numero primo') 
else: print (f'El número {numero1} no es un numero primo') 
      
#Ejercicio 4
def sumalista(num1):
  total=0
  for numactual in num1:
    total+=numactual
  return total
print(sumalista(listanum))

#Ejercicio 5
def reversalstring(word):
  anedac=''
  for actual in word:
    anedac= actual+anedac
  return anedac
print(reversalstring(cadena))