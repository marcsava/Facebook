from graph import *
from maxcut import *

# graf of marc
'''
G = Graph()
G.add_edge('A', 'B', weight=20)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'D', weight=30)
G.add_edge('C', 'D', weight=5)
G.add_edge('D', 'E', weight=300)
G.add_edge('A', 'D', weight=94)
current, partition = maxcut(G, weight='weight')
print(current, partition)
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

