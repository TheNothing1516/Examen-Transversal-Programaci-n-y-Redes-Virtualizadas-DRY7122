# distancia_chile_argentina.py

import random

print("Bienvenido al medidor de distancias entre ciudades de Chile y Argentina.")
print("Escriba 's' en cualquier momento para salir.\n")

while True:
    # 1. Solicitar ciudad de origen y destino
    origen = input("Ingrese ciudad de origen (Chile): ").strip()
    if origen.lower() == 's':
        break

    destino = input("Ingrese ciudad de destino (Argentina): ").strip()
    if destino.lower() == 's':
        break

    # 2. Elegir medio de transporte
    print("\nSeleccione el medio de transporte:")
    print("1. Auto (driving)")
    print("2. Caminando (walking)")
    print("3. Bicicleta (bicycling)")
    print("4. Transporte público (transit)")
    tipo = input("Ingrese número de opción: ").strip()

    if tipo.lower() == 's':
        break

    medios = {
        "1": "Auto",
        "2": "Caminando",
        "3": "Bicicleta",
        "4": "Transporte público"
    }

    medio = medios.get(tipo)

    if not medio:
        print("Opción inválida. Intente nuevamente.\n")
        continue

    # 3. Simular distancia y duración
    distancia_km = random.randint(500, 1600)  # Distancia simulada en km
    distancia_millas = distancia_km * 0.621371
    duracion_horas = distancia_km / {
        "Auto": 90,
        "Caminando": 5,
        "Bicicleta": 15,
        "Transporte público": 60
    }[medio]
    duracion_aproximada = f"{int(duracion_horas)} horas y {int((duracion_horas % 1) * 60)} minutos"

    # 4. Mostrar resultados
    print("\n========== RESULTADO ==========")
    print(f"Origen: {origen} (Chile)")
    print(f"Destino: {destino} (Argentina)")
    print(f"Medio de transporte: {medio}")
    print(f"Distancia aproximada: {distancia_km} km | {distancia_millas:.2f} millas")
    print(f"Duración estimada: {duracion_aproximada}")
    print("Narrativa: Este viaje cruza la cordillera de Los Andes conectando dos ciudades hermanas de Sudamérica.")
    print("================================\n")
