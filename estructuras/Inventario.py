

import csv
from algoritmos.Busquedas import existe_reserva
from estructuras.Cola import Cola
from estructuras.Pila import Pila
from modelos.Libro import Libro
from algoritmos.Ordenamientos import insercion_ordenada
from utils.persistencia import escribir_json, leer_json

class Inventario:
    def __init__(self):
        self.inventario_general = []
        self.inventario_ordenado = []       

    def cargar_desde_json(self, ruta_json: str):
        """
        Loads book data from a JSON file and adds each book to the library.

        This method reads a JSON file containing a list of book dictionaries.
        Each dictionary must include the keys: 'ISBN', 'Titulo', 'Autor',
        'Peso', and 'Valor'. An optional 'Stock' field may also be provided;
        if omitted, the stock defaults to 1.

        The method converts each JSON entry into a `Libro` object and then
        adds it to the library using `self.agregar_libro()`.

        Parameters:
            ruta_json (str): The file path to the JSON file containing book data.

        Returns:
            None: The library is modified in place by adding the loaded books.
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
        """
    Adds a book to the library's inventory.

    This method inserts the given `Libro` object into two internal lists:
    - `inventario_general`: A list containing all books in the order they were added.
    - `inventario_ordenado`: A list kept sorted by ISBN, where the book is inserted
      using the `insercion_ordenada()` function.

    Parameters:
        libro (Libro): The book object to be added to the inventory.

    Returns:
        None: The internal inventories are modified in place.
    """
        self.inventario_general.append(libro)
        
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
    
    def prestar_Libro(self, title, id):
        """
    Attempts to loan a book to a user. If the book is available, the stock is
    reduced, the loan is recorded, and the updated data is written to JSON files.
    If the book is not available, a reservation is created for the user.

    The method performs the following steps:
    1. Loads the current loan history from 'historial_prestamos.json'.
    2. Searches the general inventory for a book matching the given title.
    3. If the book exists and has available stock:
         - Decreases the stock by 1.
         - Records the loan in the history.
         - Saves updated book and history data to their respective JSON files.
         - Returns the ISBN of the loaned book.
    4. If no copies are available:
         - Loads reservation data from 'reservas.json'.
         - Adds a reservation entry for the user.
         - Saves the updated reservations back to the JSON file.

    Parameters:
        title (str): The title of the book requested by the user.
        id (str or int): The ID of the user requesting the loan.

    Returns:
        int or None:
            The ISBN of the loaned book if the loan is successful.
            None if the book was not loaned (i.e., a reservation was created).
    """
        pila_historial = Pila()
        cola_reserva = Cola()
        pila_historial.set_from_list(leer_json('data/historial_prestamos.json'))
        cola_reserva.setfrom(leer_json('data/reservas.json'))
        datos = {"id_usuario": id, "titulo_libro": title}
        existereserva = existe_reserva(cola_reserva.items, datos)
        print(existereserva)
        
        for book in self.inventario_general:
            if book.titulo == title and book.stock > 0:
                book.stock -= 1
                pila_historial.push(datos)
                escribir_json('data/libros.json',self.books_to_dict_list())
                escribir_json('data/historial_prestamos.json', pila_historial.items)

                # Dequeue reservation just if exists
                if existereserva[1] == 0:
                    if existereserva[0]:
                        # Si el usurario está encolado en reservas posicion 3 (Ej.), y el libro
                        # ya está disponible, el libro, se presta, pero, el usuario queda
                        # encolado porque hay mas reservas antes de el ...
                        cola_reserva.dequeue()
                        escribir_json('data/reservas.json', cola_reserva.items)
                else:
                    print('The reservation is not the first in the queue')
                
                return book.isbn
        
        # User and title should be differents
        if not existereserva[0]:
            cola_reserva.enqueue(datos)
            escribir_json('data/reservas.json', cola_reserva.items)
        else:
            print('The reservation already exists, be patient')
                
                
    
    def devolver_Libro(self, title):
        """"The function receives `self` and `titles` as parameters.
            It follows a loop that iterates through the inventory book by book. If `book.title` equals the title entered by the user, 
            it increments the stock and modifies the `libros.json` file to save the changes."""
        for book in self.inventario_general:
            if book.titulo == title:
                book.stock += 1
        escribir_json('data/libros.json',self.books_to_dict_list())
                
                
    def peso_autor_coleccion(self, libros_autor:list[Libro], promedio:list, weight:float = 0.0, posicion:int = 0):
        """
    Recursively calculates the average weight of a collection of books 
    written by the same author.

    This method receives a list of books (`libros_autor`) and accumulates 
    their total weight via recursion. Once the recursion reaches the end 
    of the list, it stores the computed average in the first position of 
    the `promedio` list.

    Args:
        libros_autor (list[Libro]): The list of books written by the author.
        promedio (list): A single-element list used to store the resulting 
            average weight.
        weight (float, optional): The accumulated weight during recursion. 
            Defaults to 0.0.
        posicion (int, optional): The current index in the recursive call. 
            Defaults to 0.

    Returns:
        None: The result is stored directly in `promedio[0]`.
    """
        if posicion < len(libros_autor):
            weight += float(libros_autor[posicion].peso)
            self.peso_autor_coleccion(libros_autor, promedio, weight, posicion+1)
        else:
            promedio[0] = float(weight / len(libros_autor))


    def valor_Total(self, libros_author: list, acount : float =0, posicion : int = 0):
        """
    Recursively computes the total monetary value of a list of books.

    This function iterates recursively through the list `libros_author`,
    accumulating the `valor` attribute of each book. When the recursion
    reaches the end of the list, it returns the final accumulated value.

    Args:
        libros_author (list): A list of book objects, each containing a 
            `valor` attribute representing its value.
        acount (float, optional): The running total of accumulated value 
            during the recursive calls. Defaults to 0.
        posicion (int, optional): Current index of the recursive iteration.
            Defaults to 0.

    Returns:
        float: The total value of all books in the list.
    """

        if posicion == len(libros_author):

            return acount 
        
        acount += float(libros_author[posicion].valor)

        return self.valor_Total(libros_author, acount, posicion+1)