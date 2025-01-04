from graph import not_graph
import heapq  # Куча для быстрого поиска минимальных рёбер


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











