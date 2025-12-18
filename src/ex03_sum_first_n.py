"""
Ejercicio 3:
Suma de los primeros n números.
"""

def sum_first_n(n: int) -> int:
    """
    Devuelve la suma 1 + 2 + ... + n.

    - Si n <= 0, devuelve 0.
    - Debe resolverse usando un bucle (for o while).
    """

    suma=0
    while n > 0:
        for n in range(1, n + 1):
            suma += n
        return suma
    return 0
    raise NotImplementedError("Implementa sum_first_n(n)")
