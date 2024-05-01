'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''

def Palindromo(palabra):
  palabra = palabra.replace(" ", "").lower()
  palabra_invertida = palabra[::-1]
  if palabra == palabra_invertida:
    return True
  else:
    return False

palabra = input("Ingrese una palabra: ")

if Palindromo(palabra):
  print(f"La palabra '{palabra}' es un palíndromo.")
else:
  print(f"La palabra '{palabra}' no es un palíndromo.")