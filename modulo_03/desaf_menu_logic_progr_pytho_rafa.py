executar_programa = True

while executar_programa:
    print("\n--- MENU ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Sair")

    opcao = input("Escolha uma opção (1, 2, 3 ou 4): ") 

    if opcao == '1': 
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"O resultado da SOMA é: {soma}\n")

    elif opcao == '2':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da SUBTRAÇÃO é: {resultado}\n")

    elif opcao == '3':
        num1 = int(input("Digite o dividendo: "))
        num2 = int(input("Digite o divisor: "))
        
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da DIVISÃO é: {resultado}\n")
        else:
            print("Erro: Não é possível dividir por zero!\n")

    elif opcao == '4':
        print("Saindo do programa. Até mais!")
        executar_programa = False 

    else:
        print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.\n")
