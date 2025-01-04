from graph import visualization_graph


def algoritm_kraskala(edges):
    
    if not edges:
        return print("Граф пуст, минимальное остовное дерево невозможно построить")
    
    edges.sort(key=lambda x: x[2])  # Сортируем рёбра по весу
    vertices = set(v for edge in edges for v in edge[:2])  # Все уникальные вершины
    parent = {v: v for v in vertices}  # Родитель для каждой вершины
    rank = {v: 0 for v in vertices}  # Ранг для каждой вершины
    mst = []  # Список рёбер минимального остовного дерева

    def find(v):
        """Функция поиска с сжатием путей."""
        if parent[v] != v:
            parent[v] = find(parent[v])  # Сжимаем путь
        return parent[v]

    def union(v1, v2):
        """Функция объединения с ранговой оптимизацией."""
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:  # Объединяем только разные компоненты
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True  # Объединение выполнено
        return False  # Цикл, объединение не выполнено

    for v1, v2, weight in edges:
        if union(v1, v2):  # Добавляем ребро, если оно не образует цикл
            mst.append([v1, v2, weight])
    
    # Проверяем, образовалось ли одно связное дерево
    if len(mst) != len(vertices) - 1:
        return print("Минимальное остовное дерево не построить: граф несвязный")
    
    res = mst

    return print(visualization_graph(res))

