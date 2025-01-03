# Отрисовка графов
# Я бы юзал networkx, но мне кажется, что татьянка не будет качать нашу бибилиотеку с pypi, а следовательно нам не автоматизировать это дело, а значит, что лучше не юзать ее



# Исходные данные /////////////// НЕ ЗАБУДЬТЕ ИХ УБРАТЬ
mass = [
    ['A', 'B', 13],
    ['C', 'B', 5],
    ['A', 'C', 10]
]

# Функция для создания текстового представления графа
def draw_graph(mass):
    vertices = set()
    edges = []


    for edge in mass:
        u, v, weight = edge
        vertices.add(u)
        vertices.add(v)
        edges.append((u, v, weight))


    print("Вершины графа:")
    for vertex in sorted(vertices):
        print(vertex)


    print("\nРёбра графа:")
    for u, v, weight in edges:
        print(f"{u} -- {v} (дистанция: {weight})")


draw_graph(mass)



