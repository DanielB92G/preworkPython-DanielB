'''Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100'''

def suma_pares(uno, cien):
  suma = 0
  for numero in range(uno, cien + 1):
    if numero % 2 == 0:
      suma += numero
  return suma

uno = 1
cien = 100

suma_total_pares = suma_pares(uno, cien)

print(f"La suma de todos los números pares entre {uno} y {cien} es: {suma_total_pares}")