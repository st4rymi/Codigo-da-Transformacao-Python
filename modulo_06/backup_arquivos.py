import shutil
import os

pasta_origem = "pasta_original"
pasta_destino = "pasta_backup"

try:
    if not os.path.exists(pasta_origem):
        os.makedirs(pasta_origem)
        print(f"📂 Pasta criada: {pasta_origem}")

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"📂 Pasta criada: {pasta_destino}")

    arquivos = os.listdir(pasta_origem)

    if not arquivos:
        print("⚠️ Nenhum arquivo encontrado na pasta de origem.")
    else:
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            if os.path.isfile(caminho_arquivo):
                shutil.copy(caminho_arquivo, pasta_destino)

        print(f"✅ Backup concluído! Arquivos copiados para '{pasta_destino}'.")

except Exception as erro:
    print(f"❌ Erro no sistema de backup: {erro}")