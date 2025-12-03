
from typing import List

def insercion_ordenada(lista: List, libro):

    """
    Inserts a book into a list while keeping the list sorted by ISBN.

    This function appends the new book to the end of the list
    and then shifts it backward until it reaches its correct
    sorted position based on the ISBN attribute. It performs
    the insertion using the logic of the insertion sort algorithm.

    Parameters:
        lista (List): A list of book objects already sorted by ISBN.
        libro: The book object to be inserted into the list.

    Returns:
        None: The list is modified in place.
    """
    lista.append(libro)
    i = len(lista) - 1
    while i > 0 and lista[i].isbn < lista[i-1].isbn:
        lista[i], lista[i-1] = lista[i-1], lista[i]
        i -= 1

def merge_sort_por_valor(lista: List):
    """
    Sorts a list of book objects by their 'valor' attribute using the Merge Sort algorithm.

    This function implements a recursive version of Merge Sort. It divides the list
    into two halves, recursively sorts each half, and then merges the sorted halves
    into a single sorted list based on the 'valor' (value) attribute of each item.

    Parameters:
        lista (List): A list of book objects to be sorted. Each object must contain
                      a 'valor' attribute used for comparison.

    Returns:
        List: A new list containing the same elements sorted in ascending order
              by their 'valor' attribute.
    """
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort_por_valor(lista[:mid])
    right = merge_sort_por_valor(lista[mid:])
    return _merge(left, right)

def _merge(left, right):
    """
    Merges two sorted lists of book objects into a single sorted list.

    This function assumes that both input lists (`left` and `right`)
    are already sorted by the `valor` attribute. It compares the elements
    from each list one by one and builds a new list (`res`) that maintains
    sorted order. Any remaining elements from either list are appended
    at the end.

    Parameters:
        left (List): A sorted list of book objects.
        right (List): Another sorted list of book objects.

    Returns:
        List: A new list containing all elements from `left` and `right`
              sorted in ascending order by their `valor` attribute.
    """
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
