import numpy as np

dados = np.random.randint(1, 101, size=10)
valor_maximo = dados.max()
valor_minimo = dados.min()

if valor_maximo == valor_minimo:
	dados_normalizados = np.zeros_like(dados, dtype=float)
else:
	dados_normalizados = (dados - valor_minimo) / (valor_maximo - valor_minimo)

print("Dados originais e normalizados:")
print("Original | Normalizado")
for valor_original, valor_normalizado in zip(dados, dados_normalizados):
	print(f"{valor_original:8} | {valor_normalizado:.4f}")
