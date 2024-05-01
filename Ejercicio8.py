'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''

def calcular_imc(peso, altura):
  if altura == 0:
    raise ZeroDivisionError("No se puede dividir por cero.")
  else:
    imc = peso / (altura * altura)
    return imc

def interpretar_imc(imc):
  if imc < 18.5:
    clasificacion = "Bajo peso"
  elif imc < 25:
    clasificacion = "Peso normal"
  elif imc < 30:
    clasificacion = "Sobrepeso"
  else:
    clasificacion = "Obesidad"
  return clasificacion

peso = float(input("Ingrese su peso en kg: "))

altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)

clasificacion = interpretar_imc(imc)

print(f"Su IMC es: {imc}")
print(f"Clasificación: {clasificacion}")