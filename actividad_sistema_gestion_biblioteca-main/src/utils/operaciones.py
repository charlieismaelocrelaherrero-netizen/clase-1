
from models.libro import Libro


def promedio_paginas(libros: list[Libro]):
    """Calcula el promedio de páginas de todos los libros"""
    if len(libros) == 0:
        return 0

    total_paginas = 0

    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)


def contar_libros(libros: list[Libro]):
    """Retorna la cantidad total de libros"""
    return len(libros)


def mostrar_disponibles(lista_libros: list[Libro]):
    """Muestra solo los libros que están disponibles"""

    encontrados = False

    for libro in lista_libros:
        if libro["disponible"]:
            print(
                f'Título: {libro["titulo"]} | '
                f'Autor: {libro["autor"]} | '
                f'Páginas: {libro["paginas"]}'
            )
            encontrados = True

    if not encontrados:
        print("No hay libros disponibles.")


def buscar_por_paginas(lista_libros: list[Libro], max_paginas: int):
    """Muestra libros con menos páginas que max_paginas"""

    encontrados = False

    for libro in lista_libros:
        if libro["paginas"] < max_paginas:
            print(
                f'Título: {libro["titulo"]} | '
                f'Autor: {libro["autor"]} | '
                f'Páginas: {libro["paginas"]}'
            )
            encontrados = True

    if not encontrados:
        print(f"No hay libros con menos de {max_paginas} páginas.")


def agregar_categoria(set_categorias: set[str], nueva_categoria: str):
    """Agrega una nueva categoría al set"""

    nueva_categoria = nueva_categoria.strip()

    if not nueva_categoria:
        print("La categoría no puede estar vacía.")
        return

    if nueva_categoria in set_categorias:
        print("Esa categoría ya existe.")
    else:
        set_categorias.add(nueva_categoria)
        print(f"Categoría '{nueva_categoria}' agregada correctamente.")
