def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Digite apenas números (ex.: 3.5 ou 2).")
        return

    soma = num1 + num2
    diferenca = num1 - num2
    multiplicacao = num1 * num2

    if num2 != 0:
        divisao = num1 / num2
        resto = num1 % num2
    else:
        divisao = "Erro: divisão por zero"
        resto = "Erro: divisão por zero"

    print("\nResultados:")
    print(f"Soma: {soma}")
    print(f"Subtração (diferença): {diferenca}")

    print(f"Multiplicação: {multiplicacao}")