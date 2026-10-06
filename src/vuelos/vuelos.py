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