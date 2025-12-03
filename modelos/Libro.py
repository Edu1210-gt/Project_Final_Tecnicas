

class Libro:
    """
    Represents a book with basic attributes such as ISBN, title, author,
    weight, value, and stock quantity.

    This class is used throughout the system to store and manage book
    information. It also provides a method to convert the book's data
    into a dictionary, useful for JSON serialization.

    Attributes:
        isbn (int): Unique identifier for the book.
        titulo (str): Title of the book.
        autor (str): Author's name.
        peso (float): Weight of the book in kilograms.
        valor (float): Monetary value of the book.
        stock (int): Number of available copies.

    Methods:
        to_dict(): Returns a dictionary representation of the book.
        __str__(): Returns a human-readable string describing the book.
    """
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
