'''Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual. '''
import datetime
def calcular_edad(año_nacimiento):
    año_actual = datetime.date.today().year
    edad = año_actual - año_nacimiento
    return edad

año_nacimiento = int(input("Ingrese su año de nacimiento: "))

edad = calcular_edad(año_nacimiento)

print(f"Su edad actual es de {edad} años.")