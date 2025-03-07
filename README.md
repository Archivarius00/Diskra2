# НИЖЕ ПРЕДСТАВЛЕНА ДОКУМЕНТАЦИЯ ПРОЕКТА
# Выполнено 04.01.2024

# Авторы
    Гончаров Александр - разработка алгоритма Прима и помощь в дорабтке
    Сивов Александр - разработка алгоритма Краскала
    Украинец Георгий - доработка алгоритов и их внедрение в формат библиотеки для Python

# Технические хар-ки
    Проект выполнен на языке Python 3.12
    Использовалась встроенная библиотека "heapq"


# Инструкция использования
    Библиотека требует на вход многомерный массив, содержащий в каждой строке две вершины, между которыми располагается ребро, и длину этого ребра, пример ниже:
    ```
    mass = [ 
        ['A', 'B', 13],
        ['C', 'B', 5],
        ['A', 'C', 10] 
        ]
    ```

    Поскольку алгоритм Краскала и Прима работают только для неопределенных графов, вышеуказанный массив отображает именно такой граф. 
    Изначально преполагается использование библиотеки через скачивание с помощью консольной команды "pip install ostav_algos" с PyPi, куда была загружена данная библиотека
    Но для проверки ее работоспособности существует возможность вызвать функции через файл main.py. Для этого нужно раскомментировать соотвествующую алгоритму строку и добавить массив формата указанного выше.


# Результаты тестов
    Время выполнения алгоритмов при больших значениях n (количество вершин или рёбер графа): представлено в виде графа/таблицы в папке "tests"  
    Сравнение асимптотической сложности алгоритмов:
    Тестирование алгоритма на графах слудующих типов: нормально
        • Ориентированные и неориентированные графы: нормально
        • Связные и несвязные графы: нормально
        • Графы с различными весами рёбер (включая отрицательные веса, где это применимо): нормально
        • Циклические и ациклические графы: нормально там, где это разрешено алгоритмом

    Примечание: была предусмотрена обработка ошибок (например, отсутствие пути между вершинами, невозможность выполнения алгоритма)
