ferramentas = ["Multímetro", "Osciloscópio", "Fonte de Bancada"]

# Adicionar a ferramenta "Ferro de Solda" ao final da lista
ferramentas.append("Ferro de Solda")

# Remover o item "Osciloscópio" da lista
ferramentas.remove("Osciloscópio")

# Imprimir o tamanho da lista
print(f"Tamanho da lista: {len(ferramentas)}")

# Imprimir todos os itens em ordem alfabética
print("\nItens em ordem alfabética:")
for item in sorted(ferramentas):
    print(f"  - {item}")
