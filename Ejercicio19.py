'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no. '''

def bisiesto(año):

  if año % 4 == 0:

    if año % 100 == 0 and año % 400 != 0:
      return False
    else:
      return True
  else:
    return False

año = int(input("Ingrese un año: "))

bisiesto_si = "es bisiesto" if bisiesto(año) else "no es bisiesto"

print(f"El año {año} {bisiesto_si}.")