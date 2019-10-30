'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
from binarytree import tree, bst, Node, build
from collections import Counter

# while True:
#     s = input('Введите строку: ')
#     if len(s) == 0:
#         print('Строка не может быть пустой!')
#         continue
#     c = Counter(s)
#     print(c)
#     sorted_c = sorted(c.most_common(), key=lambda c:c[1])
#     print(sorted_c)
#     print(sorted_c[0][0])
#     #print(type(most_common))
#     #for cc in c.keys()
#     # n = Node(sorted_c[0][1]+sorted_c[1][1])
#     # n.left = Node(sorted_c[0][1])
#     # n.right = Node(sorted_c[1][1])
#     # print(n)
#     # sorted_c.insert(2, (None, sorted_c[0][1] + sorted_c[1][1]))
#     # sorted_c = sorted_c[2:]
#     # sorted_c = sorted(sorted_c, key=lambda c: c[1])
#     # print(sorted_c)
#     i = 0
#     trees = []
#     while True:
#         if len(sorted_c) < 2:
#             break
#         n = Node(sorted_c[i][1]+sorted_c[i][1])
#         n.left = Node(sorted_c[i][1])
#         n.right = Node(sorted_c[i][1])
#         print(n)
#         print(type(n))
#         sorted_c.insert(2, (n, sorted_c[i][1] + sorted_c[i][1]))
#         sorted_c = sorted_c[2:]
#         sorted_c = sorted(sorted_c, key=lambda c: c[1])
#         print(sorted_c)
#         trees.append(n)
#         print(trees[0])
#         print(sorted_c[0][0])
#     break
#
# def left_tree(n, elem):
#     if type(elem) != 'binarytree.Node':
#         n.left = Node(elem)
#     else
#         n.left.left = Node(elem)
#         left_tree(n)

from heapq import heappush, heappop, heapify
from collections import defaultdict


def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    print(heap)
    heapify(heap)
    print(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        print(lo)
        hi = heappop(heap)
        print(hi)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


txt = "beep boop beer!"

symb2freq = Counter(txt)
huff = encode(symb2freq)
print("Symbol\tWeight\tHuffman Code")
for p in huff:
    print("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))
