'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.'''

def convertir_numero(minutos):
  if minutos >= 0:
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return f"{horas} horas y {minutos_restantes} minutos"

minutos = int(input("Ingrese el número de minutos: "))

horas_minutos = convertir_numero(minutos)
print(f"{minutos} minutos equivalen a {horas_minutos}.")