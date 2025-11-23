import math

def soma (a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def raiz_quadrada(x):
    return math.sqrt(x)

def potencia(base, expoente):
    return math.pow(base, expoente)