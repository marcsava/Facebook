from FacebookDE.graphProf import *

if __name__ == "__main__":
    G = Graph()
    V = {1,2,3,4,5,6,7,8,9}
    E = {
        (1,2) : 5,
        (1,3) : 4,
        (1,4) : 5,
        (1,8) : 6,
        (3,2) : 3,
        (3,4) : 4,
        (4,2) : 2,
        (8,2) : 2,
        (8,6) : 7,
        (2,6) : 3,
        (2,9) : 4,
        (2,7) : 7,
        (4,7) : 3,
        (7,5) : 2,
        (5,6) : 4,
        (9,6) : 6,
        (9,5) : 2,
        (7,9) : 4,
    }
    '''
    D, R = facebook_enmy(V,E)
    print ('Democrats ',D)
    print ('Republicans ',R)
    '''
    y = {}
    for v in V:
        y[v] = G.insert_vertex(v)

    for x in E:
      G.insert_edge(y[x[0]], y[x[1]], E[x])
    order,paths = G.getAllPaths(y[1],y[6])
    G.maxFlow(order,paths,V)
