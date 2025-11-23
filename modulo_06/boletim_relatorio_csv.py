import csv
from typing import List, Dict

nome_arquivo_csv = "sistema_notas.csv"

def registrar_notas(registros: List[Dict]):
    """Grava os registros de notas no arquivo CSV."""
    
    cabecalho = ["Aluno", "Disciplina", "Nota_1", "Nota_2", "Media_Final"]
    
    try:

        with open(nome_arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

            escritor.writeheader()
            escritor.writerows(registros)

        print(f"✅ Notas registradas em '{nome_arquivo_csv}' com sucesso.")

    except IOError as erro:
        print(f"❌ Erro ao registrar notas: {erro}")


def ler_notas():
    """Lê e exibe todos os registros do CSV."""
    
    print(f"\n📘 Conteúdo encontrado em '{nome_arquivo_csv}':")
    
    try:
        with open(nome_arquivo_csv, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                print(
                    f"Aluno: {linha['Aluno']} | "
                    f"Disciplina: {linha['Disciplina']} | "
                    f"Média Final: {linha['Media_Final']}"
                )

    except FileNotFoundError:
        print("⚠️ Arquivo CSV não encontrado. Registre notas antes de tentar ler.")
    except Exception as erro:
        print(f"❌ Erro ao carregar arquivo CSV: {erro}")


notas_exemplo = [
    {"Aluno": "Gustavo", "Disciplina": "Matemática", "Nota_1": 6.5, "Nota_2": 8.0, "Media_Final": 7.25},
    {"Aluno": "Matheus", "Disciplina": "Geografia", "Nota_1": 9.0, "Nota_2": 9.5, "Media_Final": 9.25},
    {"Aluno": "Lais", "Disciplina": "Inglês", "Nota_1": 7.0, "Nota_2": 7.5, "Media_Final": 7.25}
]

registrar_notas(notas_exemplo)
ler_notas()