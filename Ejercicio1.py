''' Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit. '''

def convertir(c):
    f = (c*9/5)+32
    return f

c = float(input('Ingresa los Grados Celsius:'))
print(f"La conversion a Grados Fahrenheit es: {convertir(c)}")