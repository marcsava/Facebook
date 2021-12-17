import sys

from facebook import *
from graphProf import *
from facebook import *
'''
V = {'a','b','c','d'}

E = {
    ('a','b') : 9,
    ('a','c') : 8,
    ('b','e') : 4,
    ('b','d') : 4,
    ('c','b') : 2,
    ('c','e') : 3,
    ('c','f') : 5,
    ('e','f') : 6,
    ('d','f') : 5,
}
'''
'''
E = {
    ('a','b') : 2,
    ('a','c') : 5,
    ('a','e') : 4,
    ('b','e') : 1,
    ('b','d') : 3,
    ('c','e') : 2,
    ('c','f') : 3,
    ('e','f') : 6,
    ('f','d') : 4,
    ('f','g') : 6,
    ('d','g') : 5,
}
'''
#D, R = facebook_enmy(V,E)
#print ('Democrats ',D)
#print ('Republicans ',R)
'''
E = {
    ('a','b') : 8,
    ('a','c') : 4,
    ('b','c') : 4,
    ('b','d') : 4,
    ('d','e') : 4,
    ('e','f') : 7,
    ('c','f') : 8,
}

E = {
    ('s','a') : 4,
    ('s','b') : 5,
    ('s','c') : 0,
    ('s','d') : 1,
    
    ('a','b') : 5,
    ('a','c') : 1,
    ('a','d') : 2,
    ('b','c') : 2,
    ('b','d') : 1,
    ('c','d') : 5,
    
    ('b','a') : 5,
    ('c','a') : 1,
    ('d','a') : 2,
    ('c','b') : 2,
    ('d','b') : 1,
    ('d','c') : 5,

    ('a','t') : 1,
    ('b','t') : 0,
    ('c','t') : 5,
    ('d','t') : 4,

}

E = {
    ('a','b') : 5,
    ('a','c') : 1,
    ('a','d') : 2,
    ('b','c') : 2,
    ('b','d') : 1,
    ('c','d') : 5,
}
''' ''' 
V = {
    'a' : (1,0),
    'b' : (3,2),
    'c' : (1,3),
    'd' : (2,1),
    'e' : (2,4),
}
E = {
    ('a','b') : 2,
    ('a','c') : 4,
    ('b','d') : 3,
    ('c','d') : 5,
    ('d','e') : 3,
}
'''
    # -----------------------------------
V = {'a','b','c','d'}
E = {
    ('a','b') : 5,
    ('a','c') : 1,
    ('a','d') : 2,
    ('b','c') : 2,
    ('b','d') : 1,
    ('c','d') : 5,
}
y = {}
G = Graph(directed=True)
for key in V:
    y[key] = G.insert_vertex(key)
for x in E:
    G.insert_edge(y[x[0]], y[x[1]], E[x])
G.getAllPaths(y['a'],y['d'])
#G.modify(y,V)
#order,paths = G.getAllPaths(y['s'],y['t'])
#dem, repu = G.minCut(order,paths,'s','t')
'''
dem, repu=facebook_friend(V,E)
print('dem ', dem)
print('repu ', repu)
'''
