"""
Clase Usuario
Contains a simple user model and a loan history stack.
"""
from estructuras.Pila import Pila

class Usuario:
    def __init__(self, id: str, nombre: str, historial: Pila = Pila()):
        self.id = id
        self.nombre = nombre
        self.historial = historial # stores dicts {"isbn":..., "fecha":...}
        
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "historial": self.historial.items}
    
    def add_historial(self, data:dict):
        self.historial.push(data)

    def __str__(self):
        return f"Usuario {self.nombre} (ID: {self.id})"
