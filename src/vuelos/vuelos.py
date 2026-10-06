# ===== DEVELOPER 1: estructura de datos =====
vuelos = {}


# ===== DEVELOPER 2: ingresos y descuento =====
def calcular_precio_final(precio):
    pass


def calcular_ingreso(pasajeros, precio):
    pass


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