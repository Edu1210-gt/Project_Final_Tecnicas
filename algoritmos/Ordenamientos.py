"""
Insertion to keep inventory sorted and merge sort to produce a report by value.
"""
from typing import List

def insercion_ordenada(lista: List, libro):
    """Insert 'libro' into lista sorted by isbn (ascending). In-place."""
    lista.append(libro)
    i = len(lista) - 1
    while i > 0 and lista[i].isbn < lista[i-1].isbn:
        lista[i], lista[i-1] = lista[i-1], lista[i]
        i -= 1

def merge_sort_por_valor(lista: List):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort_por_valor(lista[:mid])
    right = merge_sort_por_valor(lista[mid:])
    return _merge(left, right)

def _merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].valor <= right[j].valor:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
