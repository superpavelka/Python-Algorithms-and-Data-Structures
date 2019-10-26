'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель
, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''
import random


def graph_init(size):
    graph = []
    edge = []
    if size > 1:
        for vertex in range(size):
            for e in range(size):
                if e != vertex:
                    if not edge:
                        edge.append(e)
                    if random.randint(0,1):
                        if e not in edge:
                            edge.append(e)
            graph.append(edge.copy())
            edge.clear()
    return graph

def DFS(graph, v):
    # пометить все вершины непройденными
    visited = [False] * (len(graph))

    # вызываем рекурсивную функцию
    # для печати обхода в глубину
    DFSUtil(graph,v, visited)

def DFSUtil(graph, v, visited):
   # помечает текущую вершину как пройденную
   # и печатает его
    visited[v] = True
    print(f'Зашли в {v} вершину. Она ведет в вершины: {graph[v]}', end='\n')
    # повторить для всех вершин
    # смежных с этой вершиной
    for i in graph[v]:
        if visited[i] == False:
            DFSUtil(graph,i, visited)

def s_input_int(message):
    while True:

        try:
            val = int(input(message))
        except ValueError:
            print('Ошибка ввода!')
            continue
        return  val

if __name__ == "__main__":
    n = s_input_int('Введите количество вершин: ')
    g = graph_init(n)
    print(g)
    v = s_input_int('Введите вершину, с которой начинаем обход(счет вершин идет с нуля): ')
    if v <= n - 1:
        DFS(g,v)
    else:
        print('Ошибка нет такой вершины!')

