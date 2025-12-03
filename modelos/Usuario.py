"""
Clase Usuario
Contains a simple user model and a loan history stack.
"""
from estructuras.Pila import Pila
from uuid import uuid4 as uuid

class Usuario:
    def __init__(self, nombre: str):
        self.id = str(uuid()) #user_id
        self.nombre = nombre
        self.historial = Pila()  # stores dicts {"isbn":..., "fecha":...}

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "historial": self.historial.items}
    
    def add_historial(self, data:dict):
        self.historial.push(data)

    def __str__(self):
        return f"Usuario {self.nombre} (ID: {self.id})"
