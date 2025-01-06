import random
import string
import timeit

from kraskal import algoritm_kraskala
from prim import algoritm_prima
from time import time as t 


#  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ФУНКЦИИ ИЗМЕРЕНИЯ ВРЕМЕНИ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

 
def measure_kraskal(graph):
    setup_code = "from __main__ import algoritm_kraskala, graph"
    code = "algoritm_kraskala(graph)"
    execution_time = timeit.timeit(stmt=code, setup=setup_code, number=10)
    return execution_time/10

# Функция для измерения времени выполнения алгоритма Прима
def measure_prima(graph):
  setup_code = "from __main__ import algoritm_prima, graph"
  code = "algoritm_prima(graph)"
  execution_time = timeit.timeit(stmt=code, setup=setup_code, number=10)
  return execution_time/10




#  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ГЕНЕРАТОР ГРАФОВ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



def generate_graph(num_vertices=1000, max_weight=20):
    """
    Генерирует связный граф с заданным количеством вершин.

    Args:
        num_vertices (int): Количество вершин в графе.
        max_weight (int): Максимальный вес ребра.

    Returns:
        list: Список ребер, представляющих граф.
    """

    vertices = [chr(ord('A') + i) for i in range(num_vertices)]  # Генерируем вершины (буквами)
    edges = []

    # 1. Создаем "скелет" графа, чтобы он был связным
    for i in range(num_vertices - 1):
        edges.append([vertices[i], vertices[i + 1], random.randint(1, max_weight)])

    # 2. Добавляем дополнительные случайные ребра, чтобы граф был "плотнее"
    for _ in range(num_vertices * 3):  # Добавим примерно 3 ребра на вершину, чтобы граф был более связным
        u = random.choice(vertices)
        v = random.choice(vertices)
        if u != v and [u, v, 0] not in edges and [v, u, 0] not in edges:
          edges.append([u, v, random.randint(1, max_weight)])

    return edges


# Генерируем граф с n = num_vertices вершинами
graph = generate_graph(num_vertices=1000)

for edge in graph:
    print(edge)


# Измеряем время выполнения и выводим результаты
kraskal_time = measure_kraskal(graph)
prima_time = measure_prima(graph)

print(f"Среднее время выполнения алгоритма Краскала: {kraskal_time:.6f} секунд")
print(f"Среднее время выполнения алгоритма Прима: {prima_time:.6f} секунд")