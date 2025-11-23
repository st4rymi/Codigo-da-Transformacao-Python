import json

nome_arquivo_json = "clientes.json"

dados_clientes = {
    "cliente_001": {
        "nome": "Victor Silva",
        "email": "vic@exemplo.com",
        "telefone": "(11) 99999-0001",
        "ativo": True
    },
    "cliente_002": {
        "nome": "Melissa Souza",
        "email": "souz@exemplo.com",
        "telefone": "(11) 98888-0002",
        "ativo": False
    },
    "cliente_003": {
        "nome": "Elizabeth Santos",
        "email": "beth@exemplo.com",
        "telefone": "(11) 97777-0003",
        "ativo": True
    }
}

def salvar_clientes(arquivo: str, dados: dict):
    """Salva o dicionário de clientes em um arquivo JSON."""
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"✅ Dados salvos em '{arquivo}' com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao salvar dados em '{arquivo}': {e}")

def carregar_clientes(arquivo: str) -> dict:
    """Carrega e retorna o dicionário de clientes a partir do JSON.
       Se ocorrer erro, retorna um dicionário vazio."""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
        print(f"✅ Arquivo '{arquivo}' carregado com sucesso.")
        return dados
    except FileNotFoundError:
        print(f"⚠️ Arquivo '{arquivo}' não encontrado. Retornando dicionário vazio.")
        return {}
    except json.JSONDecodeError:
        print(f"❌ Arquivo '{arquivo}' está com formato inválido. Retornando dicionário vazio.")
        return {}
    except Exception as e:
        print(f"❌ Erro ao carregar '{arquivo}': {e}")
        return {}

def imprimir_resumo_clientes(dados: dict):
    """Imprime um resumo simples (total + lista de chaves)."""
    total = len(dados)
    print("\n📁 Resumo dos Clientes:")
    print(f"Total de clientes: {total}")
    if total:
        print("IDs dos clientes:", ", ".join(dados.keys()))
    else:
        print("Nenhum cliente disponível.")

def exibir_detalhe_cliente(dados: dict, cliente_id: str):
    """Mostra os dados de um cliente específico, se existir."""
    print(f"\n🔎 Detalhe do cliente '{cliente_id}':")
    cliente = dados.get(cliente_id)
    if cliente:
        for chave, valor in cliente.items():
            print(f" - {chave}: {valor}")
    else:
        print("Cliente não encontrado.")

if _name_ == "_main_":
    try:
        salvar_clientes(nome_arquivo_json, dados_clientes)

        clientes_carregados = carregar_clientes(nome_arquivo_json)

        imprimir_resumo_clientes(clientes_carregados)
        exibir_detalhe_cliente(clientes_carregados, "cliente_002")

        print("\n✏️ Atualizando status do cliente_002 para ativo = True e salvando novamente...")
        if "cliente_002" in clientes_carregados:
            clientes_carregados["cliente_002"]["ativo"] = True
            salvar_clientes(nome_arquivo_json, clientes_carregados)
            print("✅ Atualização concluída.")
        else:
            print("⚠️ cliente_002 não existe; nada foi atualizado.")

    except Exception as e:
        print(f"❌ Erro inesperado durante a execução: {e}")