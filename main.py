#Исполнительный файл

from kraskal import algoritm_kraskala
from prim import algoritm_prima
# from graph import visualization_graph





mass = [
    ['A', 'B', 4],
    ['A', 'C', 8],
    ['A', 'D', 5],
    ['B', 'C', 7],
    ['B', 'F', 6],
    ['C', 'F', 3],
    ['C', 'G', 9],
    ['D', 'G', 2],
    ['D', 'H', 4],
    ['E', 'I', 5],
    ['E', 'J', 8],
    ['F', 'J', 6],
    ['F', 'K', 7],
    ['G', 'K', 3],
    ['G', 'L', 10],
    ['H', 'L', 8],
    ['H', 'M', 6],
    ['I', 'N', 7],
    ['I', 'O', 4],
    ['J', 'O', 5],
    ['J', 'P', 9],
    ['K', 'P', 6],
    ['K', 'Q', 5],
    ['L', 'Q', 11],
    ['L', 'R', 7],
    ['M', 'R', 4],
    ['M', 'S', 9],
    ['N', 'T', 6],
    ['O', 'T', 7],
    ['P', 'U', 5],
    ['Q', 'U', 8],
    ['R', 'V', 6],
    ['S', 'V', 5],
    ['T', 'W', 4],
    ['U', 'W', 9],
    ['V', 'X', 7],
    ['W', 'X', 6],
    ['W', 'Y', 8],
    ['X', 'Z', 5],
    ['Y', 'Z', 9]
]

# algoritm_prima(mass)
algoritm_kraskala(mass)
