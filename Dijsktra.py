from collections import defaultdict
from graphProf import *
# This class represents a directed graph
# using adjacency list representation

if __name__ == "__main__":
    G = Graph()
    V = {'a','b','c','d','e','z'}
    E = {
        ('a','b') : 9,
        ('a','c') : 8,
        ('b','e') : 4,
        ('b','d') : 4,
        ('c','b') : 2,
        ('c','e') : 3,
        ('c','z') : 5,
        ('e','z') : 6,
        ('d','z') : 5,
    }
    y = {}
    for v in V:
        y[v] = G.insert_vertex(v)

    for x in E:
      G.insert_edge(y[x[0]], y[x[1]], E[x])
    paths = G.printAllPaths(y['a'],y['z'])
    for key in paths:
        print (key, paths[key])
