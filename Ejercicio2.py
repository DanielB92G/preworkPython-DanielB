'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.'''

def Monto_Total(restaurante):
    propina = restaurante * 0.15
    total = restaurante + propina
    return total
restaurante = float(input('Ingrese el costo total a pagar:'))
Total_Comida = Monto_Total(restaurante)
print(f"El total de la factura, incluyendo una propina del 15% es: {Total_Comida}")