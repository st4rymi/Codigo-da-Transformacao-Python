'''
primicias
Pedir nome e idade;
armazenar em str, armazenar em int;
Exibe em tela a mensagem
Concateados com nome e idade
'''

print("\n¨¨¨¨¨¨¨¨¨¨¨¨")
print("\fBem vindo a CDT!!")
print("\n¨¨¨¨¨¨¨¨¨¨¨¨")

nome_pessoa = str(input("Qual o seu nome? "))
idade_pessoa = int(input("Qual o sua idade? "))
altura_pessoa = float(input("Qual o sua altura? "))
cartão_pessoa = str(input("Qual é o número do seu cartão de crédito? "))

print(f"Olá, {nome_pessoa}")
print(f"Sua idade é {idade_pessoa}")
print(f"Sua altura é {altura_pessoa}")
print(f"O número do seu cartão que vou roubar é {cartão_pessoa}")