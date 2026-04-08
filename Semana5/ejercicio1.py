"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    resultado = []
    for i in range(n, n+1):
        resultado.append(i)
    return resultado


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    if n == 0:
        return []
    else:
        lista_ant = recursivo(n - 1)
        lista_ant.append(n)
        return lista_ant

print(contar_ciclo(6))
print(contar_recursivo(6))
