"""
Main menu and glue code to use all modules.
"""
import datetime
from estructuras.Inventario import Inventario
from algoritmos.Busquedas import busqueda_lineal, busqueda_binaria
from algoritmos.Ordenamientos import merge_sort_por_valor
from algoritmos.Estanteria import combinaciones_riesgo, knapsack_backtracking
from modelos.Libro import Libro
from utils.persistencia import leer_json, escribir_json

DATA_LIBROS = 'data/libros.json'
DATA_HISTORIAL = 'data/historial_prestamos.json'
DATA_RESERVAS = 'data/reservas.json'

def mostrar_menu():
    print('\n=== Library Management System ===')
    print('1. List general inventory')
    print('2. List ordered inventory (by ISBN)')
    print('3. Search by title/author (linear)')
    print('4. Search by ISBN (binary)')
    print('5. Generate value report (merge sort)')
    print('6. Shelving: brute force (combinations of 4 > 8kg)')
    print('7. Shelving: backtracking (max value <= 8kg)')
    print('8. Save/Show reservations and historials')
    print('9. Add Book')
    print('0. Exit')

def main():
    inv = Inventario()
    historiales = leer_json(DATA_HISTORIAL)
    reservas = leer_json(DATA_RESERVAS)
    inv.cargar_desde_json(DATA_LIBROS)
    print('Inventory loaded.')
    while True:
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
                print('--- combo (peso=', peso, ')')
                for b in comb:
                    print('  ', b)
        elif opc == '7':
            best_set, best_value = knapsack_backtracking(inv.inventario_general, capacidad=8.0)
            print(f'Best value: {best_value} COP with {len(best_set)} books')
            for b in best_set:
                print('  ', b)
        elif opc == '8':
            print('Historias (first 10):')
            for h in historiales[:10]:
                print(h)
            print('\nReservas (first 10):')
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
        elif opc == '0':
            print('Bye')
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
