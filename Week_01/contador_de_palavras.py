import re


def contar_palavras(frase: str) -> dict:
	"""Conta quantas vezes cada palavra aparece em uma frase usando um dicionário.

	Normaliza para minúsculas, remove pontuação básica e separa por espaços.
	Retorna um dicionário onde as chaves são palavras e os valores são contagens.
	"""
	if not frase:
		return {}
	texto = frase.lower()
	texto = re.sub(r"[^\w\s]", "", texto, flags=re.UNICODE)
	palavras = texto.split()
	contagens = {}
	for p in palavras:
		contagens[p] = contagens.get(p, 0) + 1
	return contagens


def main() -> None:
	frase = input("Digite uma frase: ")
	resultado = contar_palavras(frase)
	for palavra in sorted(resultado):
		print(f"{palavra}: {resultado[palavra]}")


if __name__ == "__main__":
	main()

