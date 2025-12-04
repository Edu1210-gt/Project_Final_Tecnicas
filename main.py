
import datetime
from estructuras.Inventario import Inventario
from algoritmos.Busquedas import busqueda_lineal, busqueda_binaria, busqueda_lineal_usuario
from algoritmos.Ordenamientos import merge_sort_por_valor
from algoritmos.Estanteria import combinaciones_riesgo, estante_backtracking
from modelos.Usuario import Usuario
from modelos.Libro import Libro
from utils.persistencia import file_exists, get_filename_from_path, leer_json, escribir_json

DATA_LIBROS = 'data/libros.json'
DATA_HISTORIAL = 'data/historial_prestamos.json'
DATA_RESERVAS = 'data/reservas.json'
DATA_USUARIOS = 'data/usuarios.json'

def create_initial_files():
    files_paths = [DATA_LIBROS, DATA_HISTORIAL, DATA_RESERVAS, DATA_USUARIOS]
    for path in files_paths:
        if not file_exists(path):
            escribir_json(path, [])
            print(f"File {get_filename_from_path(path)}")

def mostrar_menu():
    print('\n=== Library Management System ===')
    print('1.  List general inventory')
    print('2.  List ordered inventory (by ISBN)')
    print('3.  Search by title/author (linear)')
    print('4.  Search by ISBN (binary)')
    print('5.  Generate value report (merge sort)')
    print('6.  Shelving: brute force (combinations of 4 > 8kg)')
    print('7.  Shelving: backtracking (max value <= 8kg)')
    print('8.  Save/Show reservations and historials')
    print('9.  Add Book')
    print('10. Average by author')
    print('11. Total value of book by author')
    print('12. Add User')
    print('13. List Users')
    print('14. lend book')
    print('15. return book')
    print('0. Exit')

def main():
    create_initial_files()
    inv = Inventario()
    inv.cargar_desde_json(DATA_LIBROS)
    print('Inventory loaded.')
    while True:
        usuarios = leer_json(DATA_USUARIOS)
        historiales = leer_json(DATA_HISTORIAL)
        reservas = leer_json(DATA_RESERVAS)
        mostrar_menu()
        
        opc = input('Choose an option: ').strip()
        if opc == '1':
            for l in inv.listar_general():
                print(l)
        elif opc == '2':
            for l in inv.listar_ordenado():
                print(l)
        elif opc == '3':
            campo = input('Search by (titulo/autor): ').strip()
            atribute_name = input('Query (titulo/autor): ').strip()
            res = busqueda_lineal(inv.inventario_general, atribute_name, campo)
            for r in res:
                print(r)
            if not res:
                print('No matches')
        elif opc == '4':
            isbn = int(input('ISBN: '))
            idx = busqueda_binaria(inv.inventario_ordenado, isbn)
            if idx >= 0:
                print('Found:', inv.inventario_ordenado[idx])
            else:
                print('Not found')
        elif opc == '5':
            sorted_by_value = merge_sort_por_valor(inv.inventario_general)
            for l in sorted_by_value:
                print(l)
        elif opc == '6':
            combos = combinaciones_riesgo(inv.inventario_general, r=4, umbral=8.0)
            print(f'Found {len(combos)} risky combinations:')
            for comb, peso in combos:
                print(' peso total: (peso: ', peso, ')')
                for b in comb:
                    print('  ', b)
        elif opc == '7':
            best_set, best_value = estante_backtracking(inv.inventario_general, capacidad=8.0)
            print(f'Best value: {best_value} COP with {len(best_set)} books')
            for b in best_set:
                print('  ', b)
        elif opc == '8':
            print('Historiasles:')
            for h in historiales[:10]:
                print(h)
            print('\nReservas:')
            for r in reservas[:10]:
                print(r)
            # Save them back (no change) to ensure files exist
            escribir_json(DATA_HISTORIAL, historiales)
            escribir_json(DATA_RESERVAS, reservas)
        elif opc == '9':

            print("Adding a ne book to inventory.")
            isbn =  int(input("ISBN: ").strip())
            titulo = input("Title: ").strip()
            autor = input("Author: ").strip()
            peso = float(input("Weight (kg): ").strip())
            valor = float(input("Value (COP): ").strip())
            stock = int(input("Stock (default 1): ").strip())
            book = Libro(isbn,titulo,autor, peso,valor,stock)
            inv.agregar_libro(book)
            escribir_json(DATA_LIBROS, inv.books_to_dict_list())
            print('The book has been added successfully!')
        elif opc == '10':
            autor = input('Type the author name: ').strip()
            autor_libros = busqueda_lineal(inv.inventario_general, 'autor', autor)
            if len(autor_libros):
                promedio = [None]
                inv.peso_autor_coleccion(autor_libros, promedio)
                print(f'The average is: {promedio[0]}')
            else:
                print("The author don't exists or don't have books, type a valid author")
        elif opc == '11':
            author = input('Type the author name: ').strip()
            author_libros = busqueda_lineal(inv.inventario_general, 'autor', author)
            if len(author_libros):
                total = inv.valor_Total(author_libros)
                print(f"The total is: {total}")
        elif opc == '12':
            nombre = input('Type your name: ').strip()
            id = input('Type your ID: ').strip()
            usuario = Usuario(id, nombre) 
            usuarios.append(usuario.to_dict())
            escribir_json(DATA_USUARIOS, usuarios)
            print('User added successfully!')
        elif opc =='13':
            print('List of users:')
            for u in usuarios:
                user = Usuario()
                user.from_dict(u)
                print(user)
        elif opc == '14':
            id_usuario = input('Type your user ID: ').strip()
            titulo_libro = input('Type the book title: ').strip()
            
            libro_prestado = inv.prestar_Libro(titulo_libro, id_usuario)
            if libro_prestado:
                print(f'The book has been lent successfully! ISBN: {libro_prestado}')
                users = leer_json(DATA_USUARIOS)
                user = busqueda_lineal_usuario(users, 'id', id_usuario)
                if user:
                    user[0].add_historial({'Title': titulo_libro, 'fecha': str(datetime.date.today())})
                    users[user[1]]= user[0].to_dict()
                    escribir_json(DATA_USUARIOS, users)
            else:
                print('Book not available, you have been added to the reservation list.')
            
            
        
        elif opc == '15':
            titulo_libro = input('Type the book title to return: ').strip()
            inv.devolver_Libro(titulo_libro)
            escribir_json(DATA_LIBROS, inv.books_to_dict_list())
            print('The book has been returned successfully!')

        elif opc == '0':
            print('Bye')
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    create_initial_files()
    main()