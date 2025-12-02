"""
Clase Libro
Represents a book entry for the system.
"""

class Libro:
    def __init__(self, isbn: int, titulo: str, autor: str, peso: float, valor: float, stock: int = 1):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.peso = float(peso)
        self.valor = float(valor)
        self.stock = int(stock)

    def to_dict(self):
        return {
            "ISBN": self.isbn,
            "Titulo": self.titulo,
            "Autor": self.autor,
            "Peso": self.peso,
            "Valor": self.valor,
            "Stock": self.stock,
        }

    def __str__(self):
        return f"{self.isbn} | {self.titulo} — {self.autor} | Peso: {self.peso} kg | Valor: {self.valor} COP | Stock: {self.stock}"
