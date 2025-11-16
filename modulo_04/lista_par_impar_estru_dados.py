numeros = [1, 4, 7, 10, 15, 22, 33, 40]

lista_pares = []
liata_impares = []

for numero in numeros:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

print("\n=== Resultado da Separação ===")
print("Números fornecidos:", numeros)
print("Números pares:", lista_pares)
print("Números ímpares:", lista_impares)