"""
Função para limpar dados de temperatura e analisar com NumPy
- Converte lista para NumPy Array
- Remove/substitui valores inválidos (None, strings vazias)
- Retorna Média e Desvio Padrão
"""

import numpy as np

def limpar_e_analisar(lista_dados):
    """
    Limpa dados de temperatura e retorna estatísticas.
    
    Args:
        lista_dados: lista com valores de temperatura (pode conter None ou strings vazias)
        
    Returns:
        dict: dicionário com 'media' e 'desvio_padrao'
    """
    # Converter para NumPy Array
    dados_array = np.array(lista_dados, dtype=object)
    
    # Filtrar valores válidos (remover None e strings vazias)
    valores_validos = []
    for valor in dados_array:
        if valor is not None and valor != '' and valor != ' ':
            try:
                # Converter para float para validação numérica
                temp = float(valor)
                valores_validos.append(temp)
            except (ValueError, TypeError):
                print(f"⚠️  Valor inválido ignorado: {repr(valor)}")
    
    # Converter valores válidos para NumPy Array numérico
    dados_limpos = np.array(valores_validos, dtype=float)
    
    # Calcular estatísticas
    media = np.mean(dados_limpos)
    desvio_padrao = np.std(dados_limpos)
    
    return {
        'media': media,
        'desvio_padrao': desvio_padrao,
        'quantidade_total': len(lista_dados),
        'quantidade_valida': len(dados_limpos),
        'quantidade_removida': len(lista_dados) - len(dados_limpos)
    }


# Teste da função com dados de exemplo
if __name__ == "__main__":
    # Dados de temperatura de uma semana com valores inválidos
    temperaturas = [
        22.5,      # Válido
        None,      # Inválido
        23.1,      # Válido
        '',        # Inválido
        24.3,      # Válido
        21.8,      # Válido
        None,      # Inválido
        25.0,      # Válido
        ' ',       # Inválido
        22.9,      # Válido
        'erro',    # Inválido (string não numérica)
        20.5       # Válido
    ]
    
    print("=" * 60)
    print("ANÁLISE DE DADOS DE TEMPERATURA")
    print("=" * 60)
    print(f"\nDados originais: {temperaturas}")
    print(f"Total de valores: {len(temperaturas)}\n")
    
    resultado = limpar_e_analisar(temperaturas)
    
    print("RESULTADO DA LIMPEZA E ANÁLISE:")
    print("-" * 60)
    print(f"Valores válidos: {resultado['quantidade_valida']}")
    print(f"Valores removidos: {resultado['quantidade_removida']}")
    print(f"Média de temperatura: {resultado['media']:.2f}°C")
    print(f"Desvio Padrão: {resultado['desvio_padrao']:.4f}°C")
    print("=" * 60)
