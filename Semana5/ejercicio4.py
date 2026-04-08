"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    contador = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            contador +=1
    return contador


def contar_pares_recursivo(n):
    if n <= 1:
        return 0
    else: 
        es_par = 1 if n % 2 == 0 else 0
        return es_par + contar_pares_recursivo(n - 1)    

print(contar_pares_ciclo(9))
print(contar_pares_recursivo(9))