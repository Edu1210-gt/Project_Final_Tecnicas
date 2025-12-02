"""
Inventory manager: keeps general and ordered lists.
- inventario_general: load order
- inventario_ordenado: maintained sorted by ISBN using insertion sort
"""
import csv
from modelos.Libro import Libro
from algoritmos.Ordenamientos import insercion_ordenada

class Inventario:
    def __init__(self):
        self.inventario_general = []
        self.inventario_ordenado = []

    def cargar_desde_csv(self, ruta_csv: str):
        with open(ruta_csv, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                libro = Libro(
                    fila['ISBN'].strip(),
                    fila['Titulo'].strip(),
                    fila['Autor'].strip(),
                    float(fila['Peso']),
                    float(fila['Valor']),
                    int(fila.get('Stock', 1))
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
