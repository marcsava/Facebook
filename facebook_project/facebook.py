from graph import *
def facebook_enmy(V,E):
        d = set()
        r = set()
        vertex = []
        for edge in OrderedDict(sorted(E.items(), key = lambda kv :kv[1], reverse= True)):
                if edge[0] not in V or edge[1] not in V:
                        raise Exception('the arc in E is not present in V.')
                if (edge[0] not in vertex):
                        if(edge[1] not in vertex):
                                vertex.append(edge[0])
                                vertex.append(edge[1])
                                r.add(edge[0])
                                d.add(edge[1])
                        else:
                                if(edge[1] not in r):
                                        vertex.append(edge[0])
                                        r.add(edge[0])
                                else:
                                        vertex.append(edge[0])
                                        d.add(edge[0])
                else:
                        if (edge[1] not in vertex):
                                if(edge[0] not in r):
                                        vertex.append(edge[1])
                                        r.add(edge[1])
                                else:
                                        vertex.append(edge[1])
                                        d.add(edge[1])
        return d, r

def facebook_friend(V,E):
        y = {}
        G = Graph(directed=True)
        for v in V:
                y[v] = G.insert_vertex(v)
        for x in E:
                G.insert_edge(y[x[0]], y[x[1]], E[x])
        G.modify(y,V)
        order,paths = G.getAllPaths(y['s'],y['t'])
        dem, repu = G.maxFlow(order,paths,'s','t')
        return dem,repu
