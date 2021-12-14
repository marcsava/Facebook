def _swap_node_partition(cut, node):
    return cut - {node} if node in cut else cut.union({node})

def one_exchange(G, initial_cut=None, seed=None, weight=None):
    if initial_cut is None:
        initial_cut = set()
    cut = set(initial_cut)
    current_cut_size = nx.algorithms.cut_size(G, cut, weight=weight)
    while True:
        nodes = list(G.nodes())
        # Shuffling the nodes ensures random tie-breaks in the following call to max
        seed.shuffle(nodes)
        best_node_to_swap = max(
            nodes,
            key=lambda v: nx.algorithms.cut_size(
                G, _swap_node_partition(cut, v), weight=weight
            ),
            default=None,
        )
        potential_cut = _swap_node_partition(cut, best_node_to_swap)
        potential_cut_size = nx.algorithms.cut_size(G, potential_cut, weight=weight)
        if potential_cut_size > current_cut_size:
            cut = potential_cut
            current_cut_size = potential_cut_size
        else:
            break

    partition = (cut, G.nodes - cut)
    return current_cut_size, partition
