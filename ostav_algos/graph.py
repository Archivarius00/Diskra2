# Отрисовка графов, в котором происходит перебор массива остовного дерева и их последующий вывод
def visualization_graph(mass):
    vertices = set()
    edges = []


    for edge in mass:
        u, v, weight = edge
        vertices.add(u)
        vertices.add(v)
        edges.append((u, v, weight))


    print("\nРёбра графа минимального остовного дерева:")
    for u, v, weight in edges:
        print(f"{u} -- {v} (дистанция: {weight})")
