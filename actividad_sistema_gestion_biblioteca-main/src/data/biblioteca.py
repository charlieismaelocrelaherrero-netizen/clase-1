"""Libros y categorías almacenadas"""
from models.libro import Libro

libros: list[Libro] = [
    {"titulo": "Cien años de soledad", "autor": "García Márquez",
        "paginas": 471, "disponible": True},
    {"titulo": "Don Quijote", "autor": "Cervantes",
        "paginas": 863, "disponible": False},
    {"titulo": "El principito", "autor": "Saint-Exupéry",
        "paginas": 96, "disponible": True},
    {"titulo": "1984", "autor": "George Orwell", "paginas": 328, "disponible": True}
]

categorias = {"Ficción", "Ciencia", "Historia", "Poesía"}
