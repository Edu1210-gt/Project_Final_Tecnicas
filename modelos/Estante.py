"""
Clase Estante — used in shelving module
"""

class Estante:
    def __init__(self, capacidad_peso: float = 8.0):
        self.capacidad = float(capacidad_peso)
        self.libros = []  # list of Libro instances

    def peso_actual(self):
        return sum(l.peso for l in self.libros)

    def puede_agregar(self, libro):
        return (self.peso_actual() + libro.peso) <= self.capacidad

    def agregar(self, libro):
        if self.puede_agregar(libro):
            self.libros.append(libro)
            return True
        return False

    def __str__(self):
        return f"Estante({len(self.libros)} libros, peso={self.peso_actual():.2f}/{self.capacidad})"
