"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""

def ahorro_total_ciclo(ahorros):
    """
    Retorna el ahorro total usando iteración.
    """
    total = 0
    for monto in ahorros:
        total += monto
    return total


def ahorro_total_recursivo(ahorros):
    """
    Retorna el ahorro total usando recursividad.
    """
    if len(ahorros) == 0:
        return 0
    else:
        return ahorros[0] + ahorro_total_recursivo(ahorros[1:])

print(ahorro_total_ciclo([20000, 80000, 250000]))    
print(ahorro_total_recursivo([20000, 80000, 250000]))