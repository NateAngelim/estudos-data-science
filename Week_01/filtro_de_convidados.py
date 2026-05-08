from typing import Iterable, List


def confirmados_que_nao_chegaram(confirmados: Iterable[str], chegaram: Iterable[str]) -> List[str]:
	"""Retorna lista de nomes que confirmaram mas ainda não chegaram.
	Ordem alfabética.
	"""
	falta = set(confirmados) - set(chegaram)
	return sorted(falta)


def chegaram_sem_confirmar(confirmados: Iterable[str], chegaram: Iterable[str]) -> List[str]:
	"""Retorna lista de nomes que chegaram sem estar na lista de confirmados.
	Ordem alfabética.
	"""
	extra = set(chegaram) - set(confirmados)
	return sorted(extra)


def presentes_unicos(chegaram: Iterable[str]) -> List[str]:
	"""Retorna lista única de nomes que estiveram presentes (chegaram).
	Ordem alfabética.
	"""
	presentes = set(chegaram)
	return sorted(presentes)


def _exemplo() -> None:
	confirmados = ["Ana", "Beto", "Cris", "Davi"]
	chegaram = ["Cris", "Eduardo", "Ana", "Ana"]

	print("Confirmados que não chegaram:")
	print(confirmados_que_nao_chegaram(confirmados, chegaram))

	print("Chegaram sem confirmar:")
	print(chegaram_sem_confirmar(confirmados, chegaram))

	print("Lista final de presentes (únicos):")
	print(presentes_unicos(chegaram))


if __name__ == "__main__":
	_exemplo()

