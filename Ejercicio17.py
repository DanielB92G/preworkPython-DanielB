''' Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros. '''

def convertir_millas_a_kilometros(millas):
  if millas >= 0:
    kilometros = millas * 1.60934
    return kilometros

millas = float(input("Ingrese la distancia en millas: "))

kilometros = convertir_millas_a_kilometros(millas)

print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros.")