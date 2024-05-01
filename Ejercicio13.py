'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo o no.'''

def es_primo(numero):
  if numero <= 1:
    return False
  elif numero <= 3:
    return True
  elif numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

numero = int(input("Ingrese un número: "))

es_primo_si = "es primo" if es_primo(numero) else "no es primo"

print(f"El número {numero} {es_primo_si}.")