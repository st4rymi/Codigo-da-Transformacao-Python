print("--------------------------")
print("Seja bem-vindo ao CDT!")
print("--------------------------")

aluno = {
    "nome": "Osvaldo",
    "idade": 80,
    "notas": [0.5, 8.0, 7.6]
}

print("Histórico de notas do aluno")

print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")

media_notas = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média das notas: {media_notas:.2f}")

print("---------------------------------------")

print(f"Notas: {aluno['notas']}")

print("\n--- Todas as informações ---")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")