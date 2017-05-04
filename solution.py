import sys
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = set()
    def __repr__(self):
        return str(self.value)
    def add_edge(self, node):
        self.edges.add(node)

def read_input():
    stream = sys.stdin
    n = int(stream.readline()[0])
    pyramid = []
    for i in xrange(n):
        pyramid.append([])
        for _ in xrange(i + 1):
            row = stream.readline().rstrip("\n")
            row = [int(x) for x in line.split()]
            pyramid[-1].append(row)
    return pyramid

def make_graph(pyramid):
    # make nodes
    pyramid = deque([[[Node(x) for x in row]
        for row in level]
        for level in pyramid])
    # add edges
    for i, level in enumerate(pyramid):
        if i == len(pyramid) - 1:
            continue
        for j, row in enumerate(level):
            for k, wombat in enumerate(row):
                dependents = [
                    pyramid[i + 1][j][k],
                    pyramid[i + 1][j][k + 1],
                    pyramid[i + 1][j + 1][k]
                ]
                for dependent in dependents:
                    dependent.add_edge(wombat)
    # add sink
    sink = Node(0)
    pyramid[0][0][0].add_edge(sink)
    pyramid.appendleft([[sink]])
    # add source
    source = Node(0)
    for i, level in enumerate(pyramid):
        for j, row in enumerate(level):
            for wombat in row:
                source.add_edge(wombat)
    pyramid.append([[source]])
    return [source, sink]

def edmonds_karp(source, sink):
    path = set([source])
    queue = deque([[path, source]])
    added = set()
    while len(queue) != 0:
        path, last_node = queue.popleft()
        if last_node == sink:
            added = update(path, added)
        else:
            for neighbor in last_node.edges - path:
                new_path = path | set([neighbor])
                queue.append([new_path, neighbor])
    print added
    return flow(added)

def update(path, added):
    new_nodes = path - added
    if flow(new_nodes) >= 0:
        print added
        added = path | added
    return added

def flow(nodes):
    return reduce(lambda x, y: x + y.value, nodes, 0)

def solution(pyramid):
    # pyramid = read_input()
    source, sink = make_graph(pyramid)
    print edmonds_karp(source, sink)

solution([[[5]], [[-2, -7], [-3]], [[1, 0, 8], [0, 3], [2]]])
