from collections import OrderedDict

def facebook_enmy(V,E):
        d = []
        r = []
        vertex = []
        e_desc = OrderedDict(sorted(E.items(), key = lambda kv :kv[1], reverse= True))
        for edge in e_desc:
                if (edge[0] not in vertex):
                        if(edge[1] not in vertex):
                                vertex.append(edge[0])
                                vertex.append(edge[1])
                                r.append(edge[0])
                                d.append(edge[1])
                        else:
                                if(edge[1] not in r):
                                        vertex.append(edge[0])
                                        r.append(edge[0])
                                else:
                                        vertex.append(edge[0])
                                        d.append(edge[0])
                else:
                        if (edge[1] not in vertex):
                                if(edge[0] not in r):
                                        vertex.append(edge[1])
                                        r.append(edge[1])
                                else:
                                        vertex.append(edge[1])
                                        d.append(edge[1])

        return d, r
