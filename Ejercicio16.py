'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.'''

def contar_pares_impares(lista_numeros):

  pares = 0
  impares = 0
  for numero in lista_numeros:
    if numero % 2 == 0:
      pares += 1
    else:
      impares += 1
  return {"pares": pares, "impares": impares}

def main():

  while True:
    try:
      lista_numeros = []
      numero = int(input("Ingrese un número (o 0 para finalizar): "))
      while numero != 0:
        lista_numeros.append(numero)
        numero = int(input("Ingrese otro número (o 0 para finalizar): "))

      conteo_pares_impares = contar_pares_impares(lista_numeros)

      print(f"La lista contiene {conteo_pares_impares['pares']} números pares y {conteo_pares_impares['impares']} números impares.")

      otra_operacion = input("¿Desea contar pares e impares en otra lista? (sí/no): ").lower()
      if otra_operacion != "sí":
        break

    except ValueError as error:
      print(f"Error: {error}")

if __name__ == "__main__":
  main()