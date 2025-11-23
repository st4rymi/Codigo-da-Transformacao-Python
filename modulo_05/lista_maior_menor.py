def maior_menor(lista_numeros):
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    return maior, menor

numeros = [3, 10, 6, 1, 20]
maior, menor = maior_menor(numeros)

print(f"Maior número:", maior)
print(f"Menor número:", menor)