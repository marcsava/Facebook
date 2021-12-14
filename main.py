from maxcut import *
from graph import *


G = Graph()
G.add_edge('A','B', capacity=2)
G.add_edge('A','C', capacity=4)
G.add_edge('B','D', capacity=2)
G.add_edge('C','D', capacity=5)
G.add_edge('D','E', capacity=3)

current_cut_size, partition = one_exchange(G, weight= 'weight')

print(G)
print(current_cut_size, partition)
