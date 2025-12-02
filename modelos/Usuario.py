"""
Clase Usuario
Contains a simple user model and a loan history stack.
"""
from estructuras.Pila import Pila

class Usuario:
    def __init__(self, user_id: str, nombre: str):
        self.id = user_id
        self.nombre = nombre
        self.historial = Pila()  # stores dicts {"isbn":..., "fecha":...}

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre}

    def __str__(self):
        return f"Usuario {self.nombre} (ID: {self.id})"
