"""
Inventory manager: keeps general and ordered lists.
- inventario_general: load order
- inventario_ordenado: maintained sorted by ISBN using insertion sort
"""
import csv
from modelos.Libro import Libro
from algoritmos.Ordenamientos import insercion_ordenada
from utils.persistencia import leer_json

class Inventario:
    def __init__(self):
        self.inventario_general = []
        self.inventario_ordenado = []       

    def cargar_desde_json(self, ruta_json: str):
        """Load initial data from a json file
        
        :param ruta_json: Path to json file
        :type ruta_json: str
        """
        __books_data: list[dict] = leer_json(ruta_json)
        for data in __books_data:
            libro = Libro(
                data['ISBN'],
                data['Titulo'].strip(),
                data['Autor'].strip(),
                float(data['Peso']),
                float(data['Valor']),
                int(data.get('Stock', 1))
            )
            self.agregar_libro(libro)

    def agregar_libro(self, libro: Libro):
        # add to general (preserve load order)
        self.inventario_general.append(libro)
        # insert into ordered list by ISBN using insertion algorithm
        insercion_ordenada(self.inventario_ordenado, libro)

    def eliminar_por_isbn(self, isbn: str):
        self.inventario_general = [l for l in self.inventario_general if l.isbn != isbn]
        self.inventario_ordenado = [l for l in self.inventario_ordenado if l.isbn != isbn]

    def listar_general(self):
        return list(self.inventario_general)

    def listar_ordenado(self):
        return list(self.inventario_ordenado)
    
    def books_to_dict_list(self):
        books = []
        for book in self.inventario_general:
            books.append(book.to_dict())

        return books
