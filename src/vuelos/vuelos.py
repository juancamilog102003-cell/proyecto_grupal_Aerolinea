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
    pass


def procesar_vuelos(vuelos):
    pass


# ===== DEVELOPER 4: orden, total global y reporte =====
def ordenar_por_ingreso(resultados):
    pass


def calcular_ingreso_global(resultados):
    pass


def mostrar_reporte(ordenados, total_global):
    pass


# ===== PROGRAMA PRINCIPAL =====
if __name__ == "__main__":
    resultados = procesar_vuelos(vuelos)
    ordenados = ordenar_por_ingreso(resultados)
    total = calcular_ingreso_global(resultados)
    mostrar_reporte(ordenados, total)