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

def kraskal(edges):
    
    if not edges:
        return "Граф пуст, минимальное остовное дерево невозможно построить"
    
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
        return "Минимальное остовное дерево не построить: граф несвязный"
    
    return mst

result = kraskal(mass)
print("Результат нахождения минимального остовного дерева алгоритмом Краскала:", result)
