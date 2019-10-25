'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''


def dijkstra(graph, start):
    length = len(graph)
    if (start < length):
        is_visited = [False] * length
        cost = [float('inf')] * length
        parent = [-1] * length
        parents = []
        for i in range(length):
            parents.append([])
        spam_start = start

        cost[start] = 0
        min_cost = 0

        while min_cost < float('inf'):

            is_visited[start] = True

            for i, vertex in enumerate(graph[start]):
                if vertex != 0 and not is_visited[i]:
                    if cost[i] > vertex + cost[start]:
                        cost[i] = vertex + cost[start]
                        parent[i] = start
                        if parents[start] != [] and parents[start] not in parents[i]:
                            for p in parents[start]:
                                if p not in parents[i]:
                                    parents[i].append(p)
                        parents[i].append(start)

            min_cost = float('inf')
            for i in range(length):
                if min_cost > cost[i] and not is_visited[i]:
                    min_cost = cost[i]
                    start = i

        parents[spam_start].append('begin')
        for i, p in enumerate(parents):
            if not p:
                parents[i] = ['unreachable']
        result = []
        result.append(cost)
        result.append(parents)
    else:
        print('Нет такой вершины!')
        result = [[],[]]
    return result


if __name__ == "__main__":
    g = [
        [0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 5, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0]
    ]
    while True:
        # input
        try:
            s = int(input('От какой вершины идти: '))
        except ValueError:
            print('Ошибка ввода!')
            continue
        result = dijkstra(g, s)
        print(f'Стоимости вершин: {result[0]}', sep='\n')
        print(f'Пути к вершинам: {result[1]}', sep='\n')
        break
