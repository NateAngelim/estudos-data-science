frase = "Python é a ferramenta principal para análise de dados."

print("Quantidade de letras 'a':", frase.lower().count("a"))
print("Frase em maiúsculas:", frase.upper())

lista_palavras = frase[:].split()
print("Lista de palavras:", lista_palavras)
print("Palavras em ordem inversa:", lista_palavras[::-1])