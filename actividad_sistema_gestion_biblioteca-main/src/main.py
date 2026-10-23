
from data.biblioteca import libros, categorias
from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    contar_libros,
    promedio_paginas,
    agregar_categoria
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_disponibles(libros)

    elif opcion == "2":
        buscar_por_paginas(libros, 400)

    elif opcion == "3":
        print(f"Total de libros: {contar_libros(libros)}")
        print(f"Promedio de páginas: {promedio_paginas(libros):.2f}")

    elif opcion == "4":
        print("Categorías actuales:", categorias)
        nueva = input("Escribe la nueva categoría: ")
        agregar_categoria(categorias, nueva)
        print("Categorías:", categorias)

    elif opcion == "5":
        print("Gracias por usar el sistema de biblioteca.")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
