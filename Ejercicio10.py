'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.)'''

def obtener_dia_semana(numero_dia):

  if 1 <= numero_dia <= 7:
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return dias_semana[numero_dia - 1]

numero_dia = int(input("Ingrese el número de día (1 para lunes, 2 para martes, etc.): "))

dia_semana = obtener_dia_semana(numero_dia)

print(f"El día {numero_dia} de la semana es {dia_semana}.")