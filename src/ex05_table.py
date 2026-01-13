"""
Ejercicio 5:
Tabla de multiplicar.
"""

def multiplication_table(n: int) -> list[int]:
    """
    Devuelve una lista con 10 elementos:
    [n*1, n*2, ..., n*10]
    """
    l=[]
    for i in range(1, 11):
        l.append(n*i)
    return l
    raise NotImplementedError("Implementa multiplication_table(n)")

