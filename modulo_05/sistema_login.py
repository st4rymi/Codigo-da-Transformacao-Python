def login():
    usuarios + {
        "rafael": "cafe46",
        "luna": "livro0",
        "rita": "filosofia#"
    }

    usuario_resgistrado = input("Digite seu nome de usuário: ")
    senha_resgistrada = input("Digite sua senha: ")

    if usuario_registrado in usuarios and usuarios[usuario] == senha_registrada:
        print(f"Bem-vindo(a), {usuario_registrado}! Login realizado com sucesso.")
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return False