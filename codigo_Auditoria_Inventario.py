# -*- coding: utf-8 -*-
# ============================================================================
# Nombre Estudiante: Jhon Jaiver Supelano Rojas
# Grupo: 213022_969
# Programa: Problema 3 - Herramienta de Auditoria de Inventario y Reabastecimiento
# Descripcion: Auditar una matriz de inventario [Codigo, Nombre, Stock Actual,
#              Stock Minimo Requerido] y generar la lista de pedidos con la
#              cantidad exacta a solicitar por cada articulo, aplicando la
#              regla: si Stock Actual < Stock Minimo => pedir la diferencia,
#              en caso contrario => pedir 0.
#
# Codigo Fuente: autoria propia
# ============================================================================


def calcular_cantidad_pedido(stock_actual: int, stock_minimo: int) -> int:
    """Determina la cantidad exacta a pedir para un articulo.

    Reglas de negocio:
      - Si stock_actual < stock_minimo  -> pedir (stock_minimo - stock_actual)
      - Si stock_actual >= stock_minimo -> pedir 0
    """
    if stock_actual < 0 or stock_minimo < 0:
        raise ValueError("Los valores de stock no pueden ser negativos.")

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def imprimir_tabla_inventario(inventario):
    """Imprime la matriz completa de inventario con la cantidad calculada."""
    print("=" * 70)
    print("AUDITORIA DE INVENTARIO")
    print("=" * 70)
    print(f"{'Codigo':<8} {'Articulo':<28} {'Actual':>8} {'Minimo':>8} {'Pedir':>8}")
    print("-" * 70)
    for codigo, nombre, actual, minimo in inventario:
        cantidad = calcular_cantidad_pedido(actual, minimo)
        print(f"{codigo:<8} {nombre:<28} {actual:>8} {minimo:>8} {cantidad:>8}")
    print("-" * 70)


def generar_lista_pedidos(inventario):
    """Genera la lista de pedidos a partir de la matriz de inventario.

    Solo se incluyen los articulos cuya cantidad a pedir sea mayor que cero.
    Cada pedido es una tupla (codigo, nombre, cantidad).
    """
    pedidos = []
    for codigo, nombre, stock_actual, stock_minimo in inventario:
        cantidad = calcular_cantidad_pedido(stock_actual, stock_minimo)
        if cantidad > 0:
            pedidos.append((codigo, nombre, cantidad))
    return pedidos


def imprimir_lista_pedidos(pedidos):
    """Imprime la lista final de pedidos formateada."""
    print()
    print("=" * 70)
    print("LISTA DE PEDIDOS DE REABASTECIMIENTO")
    print("=" * 70)

    if not pedidos:
        print("Todos los articulos cumplen el stock minimo. No se requieren pedidos.")
        print("=" * 70)
        return

    print(f"{'#':<3} {'Codigo':<8} {'Articulo':<35} {'Cantidad a pedir':>18}")
    print("-" * 70)
    for i, (codigo, nombre, cantidad) in enumerate(pedidos, start=1):
        print(f"{i:<3} {codigo:<8} {nombre:<35} {cantidad:>18}")
    print("-" * 70)
    print(f"Total de articulos a reabastecer: {len(pedidos)}")
    print("=" * 70)


def main():
    # Matriz de inventario: [Codigo Articulo, Nombre, Stock Actual, Stock Minimo Requerido]
    inventario = [
        ["A001", "Resma de papel carta",        12,  20],
        ["A002", "Boligrafos azules",          150, 100],
        ["A003", "Cuadernos universitarios",     8,  25],
        ["A004", "Memorias USB 32GB",           30,  30],
        ["A005", "Audifonos con microfono",      5,  15],
        ["A006", "Cables HDMI 1.5m",            18,  20],
    ]

    imprimir_tabla_inventario(inventario)
    pedidos = generar_lista_pedidos(inventario)
    imprimir_lista_pedidos(pedidos)


if __name__ == "__main__":
    main()
