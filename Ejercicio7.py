'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.'''

def realizar_operacion(num1, num2, operacion):
  if operacion == "+":
    resultado = num1 + num2
  elif operacion == "-":
    resultado = num1 - num2
  elif operacion == "*":
    resultado = num1 * num2
  elif operacion == "/":
    if num2 == 0:
      raise ZeroDivisionError("No se puede dividir por cero.")
    else:
      resultado = num1 / num2
  else:
    raise ValueError("Operación no válida.")

  return resultado

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
resultado = realizar_operacion(num1, num2, operacion)
print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")