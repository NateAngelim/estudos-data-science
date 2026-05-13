leituras_sujas = [10.5, "ERRO", 12.2, "None", 15.8, 9.1, "DESCARTAR"]
leituras_limpas = []

for leitura in leituras_sujas:
	try:
		leituras_limpas.append(float(leitura))
	except (ValueError, TypeError):
		print("Aviso: Valor inválido ignorado")

if leituras_limpas:
	media = sum(leituras_limpas) / len(leituras_limpas)
	print(f"Média das leituras limpas: {media:.2f}")
else:
	print("Nenhuma leitura válida encontrada.")
