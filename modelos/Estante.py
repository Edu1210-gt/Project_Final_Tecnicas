

class Estante:
    """
    Represents a shelf that can hold a collection of books up to a maximum
    weight capacity.

    The shelf stores `Libro` objects and ensures that the combined weight
    of all books never exceeds the defined limit. It provides methods to
    check the current weight, verify if a new book can be added, and add
    books safely.

    Attributes:
        capacidad (float): Maximum allowed weight for the shelf.
        libros (list): List of `Libro` instances currently stored.

    Methods:
        peso_actual(): Returns the total weight of all books on the shelf.
        puede_agregar(libro): Returns True if the book can be added without
                              exceeding the weight limit.
        agregar(libro): Adds the book to the shelf if possible.
                        Returns True if added successfully, False otherwise.
        __str__(): Returns a readable string representation of the shelf.
    """
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
