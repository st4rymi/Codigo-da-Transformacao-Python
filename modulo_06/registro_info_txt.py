nome_arquivo_txt = "informacoes.txt"

try:
    with open(nome_arquivo_txt, "w", encoding="utf-8") as arquivo:
        arquivo.write("Nome: Evangelina Elis\n")
        arquivo.write("Profissão: Estudante\n")
        arquivo.write("Cidade: São Paulo\n")

    print(f"✅ Arquivo '{nome_arquivo_txt}' criado e preenchido com sucesso.")

    with open(nome_arquivo_txt, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    print("\n📄 Conteúdo do arquivo:")
    print(conteudo)

except Exception as erro:
    print(f"❌ Erro ao manipular arquivo TXT: {erro}")