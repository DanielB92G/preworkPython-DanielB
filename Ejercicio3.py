'''Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.'''

def Mayor_Edad(edad):
  if edad >= 18:
    return True
  else:
    return False
edad = int(input('Ingrese su edad:'))
if Mayor_Edad(edad):
  print('Eres mayor de edad')
else:
  print('Eres menor de edad')