from reportviews import *
__all__ = ["Graph"]

class Graph:
    node_dict_factory = dict
    adjlist_outer_dict_factory = dict
    graph_attr_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict


    def __init__(self):
        '''
        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory
        '''
        self.graph = self.graph_attr_dict_factory()  # dictionary for graph attributes
        self._node = self.node_dict_factory()  # empty node attribute dict
        self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict

#--
    def __contains__(self, n):
        try:
            return n in self._node
        except TypeError:
            return False

#--
    @property
    def nodes(self):
        nodes = NodeView(self)
        # Lazy View creation: overload the (class) property on the instance
        # Then future G.nodes use the existing View
        # setattr doesn't work because attribute already exists
        #Crea un dizionario di nodi
        #https://www.geeksforgeeks.org/get-a-dictionary-from-an-objects-fields/
        self.__dict__["nodes"] = nodes
        return nodes


    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        if u not in self._node:
            if u is None:
                raise ValueError("None cannot be a node")
            self._adj[u] = self.adjlist_inner_dict_factory()
            self._node[u] = self.node_attr_dict_factory()
        if v not in self._node:
            if v is None:
                raise ValueError("None cannot be a node")
            self._adj[v] = self.adjlist_inner_dict_factory()
            self._node[v] = self.node_attr_dict_factory()
        # add the edge
        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict
#--
    @property
    def edges(self):
        return EdgeView(self)
#--
    def nbunch_iter(self, nbunch=None):
        if nbunch is None:  # include all nodes via iterator
            bunch = iter(self._adj)
        elif nbunch in self:  # if nbunch is a single node
            bunch = iter([nbunch])
        else:  # if nbunch is a sequence of nodes

            def bunch_iter(nlist, adj):
                for n in nlist:
                        if n in adj:
                            yield n
                '''
                try:
                    for n in nlist:
                        if n in adj:
                            yield n
                
                except TypeError as err:
                    exc, message = err, err.args[0]
                    # capture error for non-sequence/iterator nbunch.
                    if "iter" in message:
                        exc = NetworkXError(
                            "nbunch is not a node or a sequence of nodes."
                        )
                    # capture error for unhashable node.
                    if "hashable" in message:
                        exc = NetworkXError(
                            f"Node {n} in sequence nbunch is not a valid node."
                        )
                    raise exc
                '''
            bunch = bunch_iter(nbunch, self._adj)
        return bunch


