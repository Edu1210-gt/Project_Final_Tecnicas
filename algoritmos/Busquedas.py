"""
Linear search (by title or author) and binary search (by ISBN)
"""

from typing import List

from estructuras.Pila import Pila
from modelos.Usuario import Usuario


def busqueda_lineal(lista: List, atributo: str, valor: str):
    """List: a list of objects, attribute: the name of the atrribute yo want to check(for example: 'name' , 'id')
    value: the value that attribute must have to be considered a match"""
    valor = valor.lower()
    """Convert the searched value to lowercase to make the search case-insensitive"""
    resultado = []
    """The found items will be stored here"""
    for item in lista:
        """Go thorugh each item in the list"""
        attr = getattr(item, atributo, '')
        """"Getattr dynamically gets the attribute of the item based on the provided attribute name"""
        if attr and attr.lower() == valor:
            """"Check that the attribute existe and is not empty
            convert it to lowercase 
            compare it to the searched value"""
            resultado.append(item)
    return resultado
    """"Return the list of found items"""

def busqueda_binaria(lista: List, isbn: int):
    """Binary search for an item with the given ISBN in a sorted list."""
    low, high = 0, len(lista) - 1
    """"Initialize the low and high indices for the search range."""
    while low <= high:
        """"While the search range is valid."""
        mid = (low + high) // 2
        """Calculate the middle index."""
        if lista[mid].isbn == isbn:
            return mid
            """"If the middle item's ISBN matches the searched ISBN, return the index."""
        elif lista[mid].isbn < isbn:
            low = mid + 1
            """"If the middle item's ISBN is less than the searched ISBN, adjust the low index."""
        else:
            high = mid - 1
            """"If the middle item's ISBN is greater than the searched ISBN, adjust the high index."""
    return -1
    """"If no match is found, return -1.""" 

def busqueda_lineal_usuario(lista: list, atributo: str, id: str):
    """Linear search for a user by a specific attribute and return the user object along with its index."""
    resultado = None
    """Initialize the result variable to None."""
    for i,item in enumerate(lista):
        """Iterate through the list with index."""
        attr = item.get(atributo)
        """Get the attribute value from the item."""
        if attr and attr == id:
            """Check if the attribute exists and matches the searched ID."""
            historial = Pila()
            """Create a stack to hold the user's history."""
            for h in item['historial']:
                """"Push each history entry onto the stack."""
                historial.push(h)
            resultado = [Usuario(item['id'], item['nombre'], historial),i]
    return resultado
    """Return the found user object and its index, or None if not found."""
def actualizarUsuario(id:str, obj: dict):
    dict.update
    pass

def existe_reserva(reservas: list[dict], obj: dict):
    for i, reserva in enumerate(reservas):
        __id_usuario = reserva.get('id_usuario')
        __title_book = reserva.get('titulo_libro')
        if __id_usuario and __id_usuario == obj.get('id_usuario') and __title_book and __title_book == obj.get('titulo_libro'):
            return [True, i]
    return [False, -1]