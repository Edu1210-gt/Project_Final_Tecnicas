"""
Fuerza bruta: list all combinations of 4 books whose total weight > 8 kg.
Backtracking: 0/1 knapsack maximizing value with weight capacity 8 kg.
"""
from itertools import combinations

def combinaciones_riesgo(lista_libros, r=4, umbral=8.0):
    """Return list of tuples (combination, total_weight) where total_weight > umbral."""
    resultados = []
    for comb in combinations(lista_libros, r):
        peso = sum(l.peso for l in comb)
        if peso > umbral:
            resultados.append((comb, peso))
    return resultados

def knapsack_backtracking(libros, capacidad=8.0):
    """Return best subset maximizing total valor without exceeding capacidad.
    Uses simple recursive backtracking (exponential but fine for small n).
    Returns (best_list, best_value)
    """
    n = len(libros)
    best_value = 0
    best_set = []

    def backtrack(i, current_set, current_weight, current_value):
        nonlocal best_value, best_set
        # If weight exceeded, prune
        if current_weight > capacidad:
            return
        # Update best
        if current_value > best_value:
            best_value = current_value
            best_set = current_set.copy()
        # If reached end
        if i >= n:
            return
        # Choice: include libros[i]
        backtrack(i+1, current_set + [libros[i]], current_weight + libros[i].peso, current_value + libros[i].valor)
        # Choice: exclude
        backtrack(i+1, current_set, current_weight, current_value)

    backtrack(0, [], 0.0, 0.0)
    return best_set, best_value
