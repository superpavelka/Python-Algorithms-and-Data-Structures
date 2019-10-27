'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''
'''
Для хранения использую граф, который хранится в виде списков,
каждый из которых содержит номер вершины(друга) и саму себя,
вершины в списках упорядочены по своим порядковым номерам по возрастанию,
вершина означающая саму себя обозначается нулем.
Каждый список по сути представляет вершину и все ее связи.
'''
while True:
    # input
    try:
        n = int(input('Введите количество друзей: '))
    except ValueError:
        print('Ошибка ввода!')
        continue
    graph = []
    handshakes = 0
    # graph initialize and count
    for i in range(n):
        friend = [i + 1 for i in range(n)]
        friend[i] = 0
        graph.append(friend)
    print('Граф: ', sep="/n")
    print(graph, sep="/n")
    for i, friend in enumerate(graph):
        for handshake in friend:
            if handshake != 0:
                handshakes += 1
                graph[handshake - 1][i] = 0
    print(f'Количество рукопожатий: {handshakes}')
    break
