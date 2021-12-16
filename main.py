from collections import defaultdict

from graph import *
from graphProf import *
from maxCutProf import *

# graf of marc
'''
G = Graph()
G.add_edge('A', 'B', weight=20)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'D', weight=30)
G.add_edge('C', 'D', weight=5)
G.add_edge('D', 'E', weight=300)
G.add_edge('A', 'D', weight=94)
'''

V = {'a','b','c','d','e'}
E = {
    ('a','b') : 2,
    ('a','c') : 4,
    ('b','d') : 3,
    ('c','d') : 5,
    ('d','e') : 3,
}
D, R = facebook_enmy(V,E)
print ('Democrats ',D)
print ('Republicans ',R)

'''
g = Graph()

a = g.insert_vertex('a')
b = g.insert_vertex('b')
c = g.insert_vertex('c')
d = g.insert_vertex('d')
e = g.insert_vertex('e')
g.insert_edge(a,b,2)
g.insert_edge(a,c,4)
g.insert_edge(b,d,3)
g.insert_edge(c,d,5)
g.insert_edge(d,e,3)
'''
