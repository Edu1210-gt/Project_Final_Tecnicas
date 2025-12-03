"""
Linear search (by title or author) and binary search (by ISBN)
"""

from typing import List

from estructuras.Pila import Pila
from modelos.Usuario import Usuario


def busqueda_lineal(lista: List, atributo: str, valor: str):
    """Return list of matches (case-insensitive contains)."""
    valor = valor.lower()
    resultado = []
    for item in lista:
        attr = getattr(item, atributo, '')
        if attr and attr.lower() == valor:
            resultado.append(item)
    return resultado

def busqueda_binaria(lista: List, isbn: int):
    """Assume lista sorted by ISBN. Return index or -1."""
    low, high = 0, len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid].isbn == isbn:
            return mid
        elif lista[mid].isbn < isbn:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def busqueda_lineal_usuario(lista: list, atributo: str, id: str):
    """Return list of matches (case-insensitive contains)."""
    resultado = None
    for i,item in enumerate(lista):
        attr = item.get(atributo)
        if attr and attr == id:
            historial = Pila()
            for h in item['historial']:
                historial.push(h)
            resultado = [Usuario(item['id'], item['nombre'], historial),i]
    return resultado
