"""
Ejercicio 4 (un poco más complejo):
Factorial de un número.
"""

def factorial(n: int) -> int:
    """
    Devuelve n! (n factorial).

    Reglas:
    - 0! = 1
    - Si n < 0, lanza ValueError.
    - Debe resolverse usando un bucle (no recursión).
    """
    if n < 0:
        raise ValueError("Un facotrial no está definido para números negativos, inserta un numero entero positivo")
    if n==0:
        return 1
    
    while n > 0:
        resultado=1
        for i in range(1, n + 1): #Establecemos un rango desde 1 hasta n+1 para incluir n
            resultado = resultado * i # Multiplicamos resultado por i en cada iteración para hacer el factorial
        return resultado
    raise NotImplementedError("Implementa factorial(n)")
