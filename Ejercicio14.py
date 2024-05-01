'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.'''

def calcular_precio_final(precio_inicial):
  if precio_inicial >= 0:
    descuento = 0.2
    precio_final = precio_inicial - (precio_inicial * descuento)
    return precio_final

precio_inicial = float(input("Ingrese el precio inicial del artículo: "))

precio_final = calcular_precio_final(precio_inicial)

print(f"El precio final del artículo con el 20% de descuento es: {precio_final}")