'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el usuario. '''

def suma_numeros(lista):
  if lista:
    total = 0
    for numero in lista:
      total += numero
    return total

lista = []
numero = float(input("Ingrese un número o pulse 0 para finalizar: "))
while numero != 0:
      lista.append(numero)
      numero = float(input("Ingrese otro número o pulse 0 para finalizar: "))

suma_total = suma_numeros(lista)
print(f"La suma total de los números en la lista es: {suma_total}")
