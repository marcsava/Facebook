from itertools import chain
from graph import *

def edge_boundary(G, nbunch1, nbunch2=None, data=False, keys=False, default=None):
    nset1 = {n for n in nbunch1 if n in G}
    edges = G.edges(nset1, data=data, default=default)
    return (e for e in edges if (e[0] in nset1) ^ (e[1] in nset1))


def cut_size(G, S, T=None, weight=None):
    edges = edge_boundary(G, S, T, data=weight, default=1)
    return sum(weight for u, v, weight in edges)

def _swap_node_partition(cut, node):
    return cut - {node} if node in cut else cut.union({node})

def maxcut(G, initial_cut=None, weight=None):
    if initial_cut is None:
        initial_cut = set()
    cut = set(initial_cut)
    current_cut_size = cut_size(G, cut, weight=weight)
    while True:
        nodes = list(G.nodes())
        # Shuffling the nodes ensures random tie-breaks in the following call to max
        #seed.shuffle(nodes)
        best_node_to_swap = max(
            nodes,
            key=lambda v: cut_size(
                G, _swap_node_partition(cut, v), weight=weight
            ),
            default=None,
        )
        potential_cut = _swap_node_partition(cut, best_node_to_swap)
        potential_cut_size = cut_size(G, potential_cut, weight=weight)
        if potential_cut_size > current_cut_size:
            cut = potential_cut
            current_cut_size = potential_cut_size
        else:
            break

    partition = (cut, G.nodes - cut)
    return current_cut_size, partition

def facebook_enmy(V,E):
    G = Graph()
    for key in E:
        if key[0] in V and key[1] in V:
            G.add_edge((key[0]),(key[1]), weight = E[key])
    sum_weight , partition = maxcut(G, weight='weight')
    print('The sum_weight is', sum_weight)
    return partition[0], partition[1]

