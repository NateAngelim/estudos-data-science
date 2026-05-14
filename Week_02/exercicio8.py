import numpy as np
import json
import csv
from pathlib import Path


def carregar_dados(caminho_csv, coluna='preço'):
    """
    Carrega dados numéricos de um arquivo CSV.
    
    Args:
        caminho_csv (str): Caminho do arquivo CSV
        coluna (str): Nome da coluna a extrair
    
    Returns:
        np.array: Array com valores numéricos válidos
    """
    dados = []
    
    try:
        with open(caminho_csv, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            for linha in leitor:
                try:
                    valor = float(linha.get(coluna, '').strip())
                    dados.append(valor)
                except (ValueError, AttributeError):
                    continue
        
        return np.array(dados) if dados else np.array([])
    
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{caminho_csv}' não encontrado.")
        return np.array([])


def calcular_estatisticas(array_dados):
    """
    Calcula estatísticas descritivas usando NumPy.
    
    Args:
        array_dados (np.array): Array com dados numéricos
    
    Returns:
        dict: Dicionário com estatísticas
    """
    if len(array_dados) == 0:
        return {}
    
    return {
        "quantidade": int(len(array_dados)),
        "media": float(np.mean(array_dados)),
        "mediana": float(np.median(array_dados)),
        "desvio_padrao": float(np.std(array_dados)),
        "variancia": float(np.var(array_dados)),
        "minimo": float(np.min(array_dados)),
        "maximo": float(np.max(array_dados)),
        "percentil_25": float(np.percentile(array_dados, 25)),
        "percentil_75": float(np.percentile(array_dados, 75))
    }


def salvar_relatorio(estatisticas, caminho_saida):
    """
    Salva as estatísticas em um arquivo JSON.
    
    Args:
        estatisticas (dict): Dicionário com os cálculos
        caminho_saida (str): Caminho do arquivo JSON
    """
    try:
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
            json.dump(estatisticas, arquivo, indent=2, ensure_ascii=False)
        print(f"✅ Relatório salvo em: {caminho_saida}\n")
    except IOError as e:
        print(f"❌ Erro ao salvar relatório: {e}")


def exibir_estatisticas(stats):
    """
    Exibe as estatísticas de forma formatada.
    
    Args:
        stats (dict): Dicionário com estatísticas
    """
    print("="*60)
    print("📊 ANÁLISE ESTATÍSTICA DOS DADOS")
    print("="*60)
    print(f"Quantidade de registros: {stats['quantidade']}")
    print(f"Valor médio: R$ {stats['media']:.2f}")
    print(f"Mediana: R$ {stats['mediana']:.2f}")
    print(f"Desvio padrão: R$ {stats['desvio_padrao']:.2f}")
    print(f"Variância: R$ {stats['variancia']:.2f}")
    print(f"\nValores mínimo e máximo:")
    print(f"  Mínimo: R$ {stats['minimo']:.2f}")
    print(f"  Máximo: R$ {stats['maximo']:.2f}")
    print(f"\nPercentis:")
    print(f"  Q1 (25%): R$ {stats['percentil_25']:.2f}")
    print(f"  Q3 (75%): R$ {stats['percentil_75']:.2f}")
    print("="*60 + "\n")


def main():
    """Função principal que orquestra o fluxo de dados."""
    # Definir caminhos
    caminho_csv = Path(__file__).parent / "dados_vendas.csv"
    caminho_relatorio = Path(__file__).parent / "relatorio_estatisticas.json"
    
    # Pipeline de processamento
    print("🔍 Carregando dados do CSV...\n")
    dados = carregar_dados(str(caminho_csv))
    
    if len(dados) == 0:
        print("❌ Nenhum dado válido encontrado.")
        return
    
    print(f"✅ {len(dados)} valores carregados com sucesso!\n")
    
    # Calcular estatísticas
    estatisticas = calcular_estatisticas(dados)
    
    # Exibir e salvar
    exibir_estatisticas(estatisticas)
    salvar_relatorio(estatisticas, str(caminho_relatorio))


if __name__ == "__main__":
    main()
