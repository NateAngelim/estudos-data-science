"""
Script para ler arquivo CSV com tratamento de erros
- FileNotFoundError para arquivo não encontrado
- ValueError para conversão de preço inválido
"""

try:
    with open('dados_vendas.csv', 'r', encoding='utf-8') as arquivo:
        # Ler cabeçalho
        cabecalho = arquivo.readline().strip().split(',')
        print(f"Cabeçalho: {cabecalho}\n")
        
        # Processar linhas
        for numero_linha, linha in enumerate(arquivo, start=2):
            try:
                dados = linha.strip().split(',')
                
                # Verificar se tem todos os campos
                if len(dados) != 3:
                    raise ValueError("Número de colunas incorreto")
                
                produto = dados[0]
                quantidade = int(dados[1])
                preco = float(dados[2])  # Aqui pode gerar ValueError
                
                total = quantidade * preco
                print(f"✓ Linha {numero_linha}: {produto} | Qtd: {quantidade} | Preço: R${preco:.2f} | Total: R${total:.2f}")
                
            except ValueError as e:
                print(f"✗ Linha {numero_linha}: Linha ignorada devido a erro de formato")

except FileNotFoundError:
    print("❌ Erro: Arquivo 'dados_vendas.csv' não encontrado!")
    print("   Por favor, verifique se o arquivo existe no diretório atual.")
