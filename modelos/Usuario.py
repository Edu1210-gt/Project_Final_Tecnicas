"""

"""
from estructuras.Pila import Pila

class Usuario:
    
    """
    Represents a user within the system, storing basic identification
    data along with a stack-based search or activity history.

    This class supports converting user data to and from dictionary 
    format, which is useful for JSON serialization and persistence. 
    The user's history is stored using a Pila (stack) structure.

    Attributes:
        id (str): Unique identifier for the user.
        nombre (str): Full name of the user.
        historial (Pila): Stack containing the user's activity or search history.

    Methods:
        to_dict(): Returns a dictionary representation of the user.
        from_dict(data): Loads user data from a dictionary, rebuilding the history stack.
        add_historial(data): Adds a new entry to the user's history.
        __str__(): Returns a formatted string with user information.
    """
    def __init__(self, id: str = '', nombre: str = '', historial: Pila = Pila()):
        
        self.id = id
        self.nombre = nombre
        self.historial = historial # Pila of search history
        
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "historial": self.historial.items}
    
    def from_dict(self, data:dict):
        self.id = data["id"]    
        self.nombre = data["nombre"]
        self.historial = Pila()
        for item in data["historial"]:
            self.historial.push(item)

            
    def add_historial(self, data:dict):
        self.historial.push(data)

    def __str__(self):
        return f"| {self.id} | {self.nombre} |"
