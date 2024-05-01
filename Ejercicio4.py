'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

def Numero_Vocales(palabra):
    vocales='aeiouAEIOU'
    cuente = 0
    for palabras in palabra:
      if palabras in vocales:
        cuente += 1
    return cuente

palabra = input('Ingrese una palabra:')
cantidad_vocales = Numero_Vocales(palabra)

print(f'La palabra "{palabra}" tiene {cantidad_vocales} vocales')