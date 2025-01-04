# Отрисовка графов
# Я бы юзал networkx, но мне кажется, что татьянка не будет качать нашу бибилиотеку с pypi, а следовательно нам не автоматизировать это дело, а значит, что лучше не юзать ее





# Функция для создания текстового представления графа
def not_graph(mass):
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





