'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.'''

def convertir_dolares_a_euros(dolares):
  if isinstance(dolares, float) and dolares >= 0:
    tasa_cambio = 0.85
    euros = dolares * tasa_cambio
    return euros

dolares = float(input("Ingrese la cantidad de dólares a convertir: "))

euros = convertir_dolares_a_euros(dolares)

print(f"{dolares} dólares equivalen a {euros} euros.")