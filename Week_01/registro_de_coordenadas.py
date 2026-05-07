# Criar a lista de sensores
sensores = [
    (1, -23.55, -46.63),
    (2, -22.90, -43.17),
    (3, -30.03, -51.20)
]

# Percorrer a lista e imprimir ID e Latitude de cada sensor
print("ID do Sensor | Latitude")
print("-" * 25)
for sensor in sensores:
    id_sensor = sensor[0]
    latitude = sensor[1]
    print(f"{id_sensor:13} | {latitude}")
