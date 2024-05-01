'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.'''

def cuente_palabras (oracion):

  oracion = oracion.strip()
  palabras = oracion.split()
  cantidad_palabras = len(palabras)
  return cantidad_palabras

oracion = input("Ingrese una oración: ")
cantidad_palabras = cuente_palabras(oracion)

print(f"La oración tiene {cantidad_palabras} palabras.")