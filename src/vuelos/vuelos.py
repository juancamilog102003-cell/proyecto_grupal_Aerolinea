# ===== DEVELOPER 1: estructura de datos =====
vuelos = {}


# ===== DEVELOPER 2: ingresos y descuento =====
def calcular_precio_final(precio):
    pass


def calcular_ingreso(pasajeros, precio):
    pass


# ===== DEVELOPER 3: baja ocupación y resultados =====
def es_baja_ocupacion(pasajeros):
    pass


def procesar_vuelos(vuelos):
    pass


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