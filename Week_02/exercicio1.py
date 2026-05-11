import csv


def ler_vendas(caminho_arquivo: str) -> None:
    with open(caminho_arquivo, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for numero_linha, linha in enumerate(leitor, start=2):
            try:
                produto = linha["produto"].strip()
                quantidade = int(linha["quantidade"])
                preco = float(linha["preco"])
            except (ValueError, TypeError, KeyError):
                print(f"Linha {numero_linha} ignorada por estar suja: {linha}")
                continue

            print(f"Linha {numero_linha} ok: {produto} | quantidade={quantidade} | preco={preco:.2f}")


if __name__ == "__main__":
    ler_vendas("vendas.csv")
