'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.'''

def calcular_area_rectangulo(longitud, ancho):

  if longitud >= 0 and ancho >= 0:
    area = longitud * ancho
    return area

longitud = float(input("Ingrese la longitud del rectángulo: "))

ancho = float(input("Ingrese el ancho del rectángulo: "))

area = calcular_area_rectangulo(longitud, ancho)

print(f"El área del rectángulo es de {area} unidades cuadradas.")