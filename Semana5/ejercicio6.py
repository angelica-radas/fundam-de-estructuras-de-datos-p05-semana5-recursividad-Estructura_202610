"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
    """
    Retorna el total de ventas usando ciclos.
    """
    total = 0
    for monto in ventas:
        total += monto
    return total


def total_ventas_recursivo(ventas):
    """
    Retorna el total de ventas usando recursividad.
    """
    if len(ventas) == 0:
        return 0
    else:
        return ventas[0] + total_ventas_recursivo(ventas[1:])

print(total_ventas_ciclo([200, 650, 100, 25]))
print(total_ventas_recursivo([200, 650, 100, 25]))
