from graph import not_graph
import heapq  # Куча для быстрого поиска минимальных рёбер




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

def algoritm_prima(edges):
    if not edges:
        return print("Граф пуст, минимальное остовное дерево невозможно построить")

    # Словарь смежности для графа
    graph = {}
    for vertex1, vertex2, weight in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
        graph[vertex1].append((weight, vertex2))
        graph[vertex2].append((weight, vertex1))

    starting_vertex = next(iter(graph))  # Выбираем произвольную стартовую вершину
    mst_edges = []  # Список рёбер минимального остовного дерева
    visited_vertices = set()  # Множество посещённых вершин
    priority_queue = [(0, starting_vertex, None)]  # Куча для хранения рёбер по минимальному весу (вес, вершина, родитель)

    while priority_queue:
        edge_weight, current_vertex, parent_vertex = heapq.heappop(priority_queue)  # Извлекаем из кучи рёбро с минимальным весом
        if current_vertex not in visited_vertices:
            visited_vertices.add(current_vertex)
            if parent_vertex is not None:
                mst_edges.append([parent_vertex, current_vertex, edge_weight])

            # Добавляем соседние рёбра в кучу
            for neighbor_weight, neighbor_vertex in graph[current_vertex]: # Для всех соседей текущей вершины добавляем рёбра в кучу
                if neighbor_vertex not in visited_vertices: # Если сосед ещё не посещён, добавляем его в кучу
                    heapq.heappush(priority_queue, (neighbor_weight, neighbor_vertex, current_vertex))

    # Проверяем связность графа
    if len(visited_vertices) != len(graph):
        return print("Минимальное остовное дерево не построить: граф несвязный")
    
    
    result = mst_edges

    return print(not_graph(result))

algoritm_prima(mass)










