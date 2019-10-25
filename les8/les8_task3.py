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
    # Mark all the vertices as not visited
    visited = [False] * (len(graph))

    # Call the recursive helper function
    # to print DFS traversal
    DFSUtil(graph,v, visited)

def DFSUtil(graph, v, visited):
     # Mark the current node as visited
    # and print it
    visited[v] = True
    print(v, end=' ')
     # Recur for all the vertices
    # adjacent to this vertex
    for i in graph[v]:
        if visited[i] == False:
            DFSUtil(graph,i, visited)


if __name__ == "__main__":
    g = graph_init(5)
    print(g)
    DFS(g,0)

