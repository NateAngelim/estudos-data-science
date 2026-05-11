import numpy as np


temperaturas = [25.5, 28.0, 31.2, 22.1, 19.8, 27.4, 30.0]
array_temperaturas = np.array(temperaturas)

media = np.mean(array_temperaturas)
mediana = np.median(array_temperaturas)
desvio_padrao = np.std(array_temperaturas)

print("Temperaturas:", array_temperaturas)
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")

mascara_acima_da_media = array_temperaturas > media
temperaturas_acima_da_media = array_temperaturas[mascara_acima_da_media]

print("Temperaturas acima da média:", temperaturas_acima_da_media)
