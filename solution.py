import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
    def __repr__(self):
        return str(self.value)
    def add_edge(self, node):
        self.edges.append(node)

def read_input():
    stream = sys.stdin
    n = int(stream.readline()[0])
    pyramid = []
    for i in xrange(n):
        pyramid.append([])
        for _ in xrange(i + 1):
            row = stream.readline().rstrip("\n")
            row = [Node(int(x)) for x in line.split()]
            pyramid[-1].append(row)
    return pyramid

def make_graph(pyramid):
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

def solution(pyramid):
    # pyramid = read_input()
    make_graph(pyramid)

solution([[[5]], [[-2, -7], [-3]], [[1, 0, 8], [0, 3], [2]]])
