'''
1.1 Dado el siguiente diccionario, cambia el valor de la clave "edad" a 25.
  persona = {"nombre":"juan","edad":10}
  
1.2 Declara una variable "precio" y asignale el valor 25. Luego, crea una variable "impuesto" y asignale el valor de "precio" multiplicado por o.21.
  Muestra ambos valores por consola de esta forma:
  El precio es 25 y el impuesto es 5.25.
1.3 Dado el siguiente diccionario, imprime con un print el valor de la clave "apellido".
  persona = {"nombre":"Juan","apellido":"Perez"}
'''

persona = {"nombre":"juan","edad":10}
persona["edad"]=25
print (persona["edad"])

precio=25
impuesto=precio*0.21
print(f'El precio es {precio} y el impuesto es {impuesto}')

persona = {"nombre":"Juan","apellido":"Perez"}
print(persona["apellido"])