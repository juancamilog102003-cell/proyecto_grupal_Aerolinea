# ===== DEVELOPER 1: estructura de datos =====
vuelos = {
    "AV101": {"pasajeros": 120, "precio": 450},
    "LA202": {"pasajeros": 45, "precio": 620},
    "AA303": {"pasajeros": 80, "precio": 500},
    "CM404": {"pasajeros": 30, "precio": 800},
    "VV505": {"pasajeros": 150, "precio": 380},
}


# ===== DEVELOPER 2: ingresos y descuento =====
def calcular_precio_final(precio):
    if precio > 500:
        return precio * 0.85
    return precio


def calcular_ingreso(pasajeros, precio):
    return pasajeros * calcular_precio_final(precio)


# ===== DEVELOPER 3: baja ocupación y resultados =====
def es_baja_ocupacion(pasajeros):
    return pasajeros < 50


def procesar_vuelos(vuelos):
    resultados = {}
    for codigo, datos in vuelos.items():
        pasajeros = datos["pasajeros"]
        precio = datos["precio"]
        resultados[codigo] = {
            "pasajeros": pasajeros,
            "precio_original": precio,
            "precio_final": calcular_precio_final(precio),
            "ingreso": calcular_ingreso(pasajeros, precio),
            "baja_ocupacion": es_baja_ocupacion(pasajeros),
        }
    return resultados

# ===== DEVELOPER 4: orden, total global y reporte =====
def ordenar_por_ingreso(resultados):
    return sorted(resultados.items(), key=lambda item: item[1]["ingreso"], reverse=True)


def calcular_ingreso_global(resultados):
    return sum(datos["ingreso"] for datos in resultados.values())


def mostrar_reporte(ordenados, total_global):
    print("=== REPORTE DE VUELOS ===")
    for codigo, d in ordenados:
        descuento = d["precio_final"] != d["precio_original"]
        print(f"Vuelo: {codigo}")
        print(f"  Pasajeros: {d['pasajeros']}")
        print(f"  Precio original: {d['precio_original']}")
        if descuento:
            print(f"  Precio con descuento: {d['precio_final']:.2f}")
        print(f"  Ingreso: {d['ingreso']:.2f}")
        print(f"  Baja ocupación: {'Sí' if d['baja_ocupacion'] else 'No'}")
        print("-" * 30)
    print(f"INGRESO TOTAL GLOBAL: {total_global:.2f}")

# ===== PROGRAMA PRINCIPAL =====
if __name__ == "__main__":
    resultados = procesar_vuelos(vuelos)
    ordenados = ordenar_por_ingreso(resultados)
    total = calcular_ingreso_global(resultados)
    mostrar_reporte(ordenados, total)