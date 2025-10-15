# Introdução.py
# Programa de apresentação simples.

def saudacao():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Seja bem-vindo(a) ao curso de Python.")

resposta = input("Você gostaria de um café? (sim/não) ")
if resposta.lower() == 'sim':
    print("Òtimo! Vou preparar um café para você.")
else:
    print("Tudo bem! Quem sabe mais tarde...")
saudacao()