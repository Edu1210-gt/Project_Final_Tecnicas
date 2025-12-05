
from itertools import combinations

def combinaciones_riesgo(lista_libros, r=4, umbral=8.0):
    """The function receives a list of books, the size of the combinations (r), "
    and a risk threshold. It iterates through all possible combinations of the list with r books each. 
    For every combination, it calculates a variable called weight, which is the sum of the individual weight of each book. 
    Then, a conditional statement checks whether this total weight exceeds the threshold. If it does, the combination is added to the result list. After evaluating all combinations, 
    the function returns the list of risky combinations."""
    resultados = []
    for comb in combinations(lista_libros, r):
        peso = sum(lib.peso for lib in comb)
        if peso > umbral:
            resultados.append((comb, peso))
    return resultados

def estante_backtracking(libros, capacidad=8.0):
   
    """
    Solves the 0/1 Knapsack problem using a backtracking approach.

    Parameters:
        libros (list): A list of book objects, each containing 'peso' (weight) and 'valor' (value) attributes.
        capacidad (float): The maximum allowed total weight.

    Returns:
        tuple: (best_set, best_value)
            - best_set: The list of selected books that produces the highest value.
            - best_value: The maximum total value obtained.

    The algorithm explores all possible combinations of books.
    For each book, it decides whether to include it or skip it.
    Any branch that exceeds the weight capacity is immediately discarded.
    After evaluating all valid combinations, the function returns the one with the highest value.
    """
    total_libros = len(libros)
    best_value = 0
    best_set = []

    def backtrack(i, current_set, current_weight, current_value):
        nonlocal best_value, best_set
        
        if current_weight > capacidad:
            return

        if current_value > best_value:
            best_value = current_value
            best_set = current_set
        
        if i >= total_libros:
            return
    
        backtrack(i+1, current_set + [libros[i]], current_weight + libros[i].peso, current_value + libros[i].valor)
        
        backtrack(i+1, current_set, current_weight, current_value)

    backtrack(0, [], 0.0, 0.0)
    return best_set, best_value
