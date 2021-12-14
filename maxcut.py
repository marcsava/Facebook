from itertools import chain

def edge_boundary(G, nbunch1, nbunch2=None, data=False, keys=False, default=None):

    nset1 = {n for n in nbunch1 if n in G}
    if G.is_multigraph():
        edges = G.edges(nset1, data=data, keys=keys, default=default)
    else:
        edges = G.edges(nset1, data=data, default=default)
    if nbunch2 is None:
        return (e for e in edges if (e[0] in nset1) ^ (e[1] in nset1))
    nset2 = set(nbunch2)
    return (
        e
        for e in edges
        if (e[0] in nset1 and e[1] in nset2) or (e[1] in nset1 and e[0] in nset2)
    )

def cut_size(G, S, T=None, weight=None):
    edges = edge_boundary(G, S, T, data=weight, default=1)
    if G.is_directed():
        edges = chain(edges, edge_boundary(G, T, S, data=weight, default=1))
    return sum(weight for u, v, weight in edges)

def _swap_node_partition(cut, node):
    return cut - {node} if node in cut else cut.union({node})

def one_exchange(G, initial_cut=None, seed=None, weight=None):
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
