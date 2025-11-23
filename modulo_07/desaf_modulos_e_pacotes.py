from utilidades import soma, subtracao, multiplicacao, divisao, raiz_quadrada, potencia
from externo.exemplo_faker import gerar_pessoa_fake
from jogo.adivinhacao import jogar

def menu():
    print("""
==========================
      MENU PRINCIPAL
==========================
1 - Usar funções matemáticas
2 - Gerar pessoa falsa (Faker)
3 - Jogar Adivinhação
0 - Sair
""")

def menu_matematica():
    print("""
--- Funções Matemáticas ---
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Raiz Quadrada
6 - Potência
0 - Voltar
---------------------------
""")

def ler_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida: por favor digite um número válido.")

def executar_matematica():
    while True:
        menu_matematica()
        op = input("Escolha: ").strip()

        if op == "0":
            break

        if op in ["1", "2", "3", "4", "6"]:
            a = ler_numero("Por favor, digite o primeiro número: ")
            b = ler_numero("Agora, digite o segundo número: ")

        try:
            if op == "1":
                print("Resultado:", soma(a, b))
            elif op == "2":
                print("Resultado:", subtracao(a, b))
            elif op == "3":
                print("Resultado:", multiplicacao(a, b))
            elif op == "4":
        
                try:
                    print("Resultado:", divisao(a, b))
                except ZeroDivisionError:
                    print("Erro: divisão por zero não é permitida.")
            elif op == "5":
                x = ler_numero("Digite um número: ")

                try:
                    print("Raiz quadrada:", raiz_quadrada(x))
                except ValueError as e:
                    print("Erro ao calcular raiz quadrada:", e)
            elif op == "6":
                print("Potência:", potencia(a, b))
            else:
                print("Opção inválida! :( Tente novamente.")
        except Exception as e:
    
            print("Ocorreu um erro durante a operação:", e)

        input("\nPressione Enter para continuar...")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            executar_matematica()

        elif opcao == "2":
            pessoa = gerar_pessoa_fake()
            print("\nPessoa gerada:")
            if isinstance(pessoa, dict):
                for chave, valor in pessoa.items():
                    print(f"{chave.capitalize()}: {valor}")
            else:
            
                print(pessoa)
            print()
            input("Pressione Enter para continuar...")

        elif opcao == "3":
        
            jogar()
            input("Pressione Enter para voltar ao menu...")

        elif opcao == "0":
            print("Saindo... Obrigado por usar o programa!")
            break

        else:
            print("Ops, opção inválida! Tente novamente.\n")

if _name_ == "_main_":
    main()