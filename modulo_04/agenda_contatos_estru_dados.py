agenda = {}

def cadastrar():
    nome_contato = input("Nome do contato: ").strip().title()
    numero_contato = input("Número de telefone: ").strip()

    agenda[nome_contato] = numero_contato
    print(f"\nContato '{nome_contato}' salvo com sucesso!")

def procurar():
    busca = input("Quem você quer encontrar? ").strip().title()

    if busca in agenda:
        print(f"\n{busca} → {agenda[busca]}")
    else:
        print(f"\nNada encontrado para '{busca}'.")