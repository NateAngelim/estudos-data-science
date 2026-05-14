import csv
import json
from pathlib import Path

def processar_vendas(arquivo_csv, arquivo_relatorio):
    """
    Processa um arquivo CSV de vendas, tratando dados corrompidos.
    
    Args:
        arquivo_csv (str): Caminho do arquivo CSV de entrada
        arquivo_relatorio (str): Caminho do arquivo JSON de saída
    """
    vendas_validas = []
    total_vendas = 0.0
    quantidade_erros = 0
    erros_detalhados = []
    
    # Usar context manager para garantir fechamento do arquivo
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            for num_linha, linha in enumerate(leitor, start=2):  # start=2 porque a linha 1 é header
                try:
                    produto = linha.get('produto', '').strip()
                    quantidade_str = linha.get('quantidade', '').strip()
                    preco_str = linha.get('preço', '').strip()
                    
                    # Validar se os campos existem
                    if not produto or not quantidade_str or not preco_str:
                        raise ValueError(f"Campo vazio detectado")
                    
                    # Converter para números
                    quantidade = int(quantidade_str)
                    preco = float(preco_str)
                    
                    # Calcular valor total da venda
                    valor_venda = quantidade * preco
                    
                    # Adicionar à lista de vendas válidas
                    vendas_validas.append({
                        'produto': produto,
                        'quantidade': quantidade,
                        'preço': preco,
                        'valor_total': valor_venda
                    })
                    
                    total_vendas += valor_venda
                    
                except ValueError as e:
                    quantidade_erros += 1
                    erros_detalhados.append({
                        'linha': num_linha,
                        'dados': dict(linha),
                        'erro': str(e)
                    })
                    print(f"⚠️  Erro na linha {num_linha}: {linha}")
                    print(f"   Motivo: Falha ao converter valores numéricos\n")
    
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{arquivo_csv}' não encontrado.")
        return
    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {e}")
        return
    
    # Criar relatório
    relatorio = {
        'resumo': {
            'total_vendas_validas': len(vendas_validas),
            'total_erros': quantidade_erros,
            'valor_total': round(total_vendas, 2),
            'percentual_sucesso': round((len(vendas_validas) / (len(vendas_validas) + quantidade_erros) * 100), 2) if (len(vendas_validas) + quantidade_erros) > 0 else 0
        },
        'vendas_validas': vendas_validas,
        'erros': erros_detalhados
    }
    
    # Salvar relatório em JSON usando context manager
    try:
        with open(arquivo_relatorio, 'w', encoding='utf-8') as arquivo_json:
            json.dump(relatorio, arquivo_json, indent=2, ensure_ascii=False)
        
        print("\n" + "="*60)
        print("✅ RELATÓRIO DE LIMPEZA DE DADOS")
        print("="*60)
        print(f"Arquivo processado: {arquivo_csv}")
        print(f"Relatório salvo em: {arquivo_relatorio}\n")
        print(f"📊 Resumo:")
        print(f"   • Vendas válidas: {relatorio['resumo']['total_vendas_validas']}")
        print(f"   • Erros encontrados: {relatorio['resumo']['total_erros']}")
        print(f"   • Valor total em vendas: R$ {relatorio['resumo']['valor_total']:,.2f}")
        print(f"   • Taxa de sucesso: {relatorio['resumo']['percentual_sucesso']}%")
        print("="*60 + "\n")
        
    except IOError as e:
        print(f"❌ Erro ao salvar relatório: {e}")

if __name__ == "__main__":
    # Definir caminhos dos arquivos
    caminho_csv = Path(__file__).parent / "dados_vendas.csv"
    caminho_relatorio = Path(__file__).parent / "relatorio_limpeza.json"
    
    # Processar vendas
    processar_vendas(str(caminho_csv), str(caminho_relatorio))
