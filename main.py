from graph import *
from maxcut import *

# graf of marc
G = Graph()
G.add_edge('A', 'B', weight=20)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'D', weight=30)
G.add_edge('C', 'D', weight=5)
G.add_edge('D', 'E', weight=300)
G.add_edge('A', 'D', weight=94)
current, partition = one_exchange(G, weight='weight')
print(current, partition)

#graf of professores
P = Graph()
P.add_edge('A', 'B', weight=2)
P.add_edge('A', 'C', weight=4)
P.add_edge('B', 'D', weight=3)
P.add_edge('C', 'D', weight=5)
P.add_edge('D', 'E', weight=3)
current2, partition2 = one_exchange(P, weight='weight')
print(current2, partition2)