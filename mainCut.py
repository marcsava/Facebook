from graph import *
from graphProf import *
from maxcut import *

#super mega grafo
V = {'a','b','c','d','e','f','g'}
E = {
    ('a','b') : 36,
    ('a','g') : 17,
    ('a','f') : 1,
    ('a','e') : 90,
    ('g','f') : 5,
    ('d','f') : 17,
    ('d','c') : 40,
    ('g','c') : 48,
    ('d','b') : 15,
    ('d','e') : 25,
}
D, R = facebook_enmy(V,E)
print ('Democrats ',D)
print ('Republicans ',R)

# -----------------------------------

