# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from collections import defaultdict
from collections import OrderedDict
from store_for_pathAll import *
class Graph:
  """Representation of a simple graph using an adjacency map."""
  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_element'

    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._element = x

    def element(self):
      """Return element associated with this vertex."""
      return self._element

    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return str(self._element)

  #------------------------- nested Edge class -------------------------
  class Edge:
    """Lightweight edge structure for a graph."""
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
      """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
      self._origin = u
      self._destination = v
      self._element = x

    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)

    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      if v is self._origin:
        return self._destination
      elif v is self._destination:
          return self._origin
      raise ValueError('v not incident to edge')

    def element(self):
      """Return element associated with this edge."""
      return self._element

    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)

  #------------------------- Graph methods -------------------------
  def __init__(self, directed=False):
    """Create an empty graph (undirected, by default).

    Graph is directed if optional paramter is set to True.
    """
    self._outgoing = {}
    # only create second map for directed graph; use alias for undirected
    self._incoming = {} if directed else self._outgoing
    self.graph = defaultdict(list)
    self.pathAll = []

  def _validate_vertex(self, v):
    """Verify that v is a Vertex of this graph."""
    if not isinstance(v, self.Vertex):
      raise TypeError('Vertex expected')
    if v not in self._outgoing:
      raise ValueError('Vertex does not belong to this graph.')

  def is_directed(self):
    """Return True if this is a directed graph; False if undirected.

    Property is based on the original declaration of the graph, not its contents.
    """
    return self._incoming is not self._outgoing # directed if maps are distinct

  def vertex_count(self):
    """Return the number of vertices in the graph."""
    return len(self._outgoing)

  def vertices(self):
    """Return an iteration of all vertices of the graph."""
    return self._outgoing.keys()

  def edge_count(self):
    """Return the number of edges in the graph."""
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    # for undirected graphs, make sure not to double-count edges
    return total if self.is_directed() else total // 2

  def edges(self):
    """Return a set of all edges of the graph."""
    result = set()       # avoid double-reporting edges of undirected graph
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())    # add edges to resulting set
    return result

  def get_edge(self, u, v):
    """Return the edge from u to v, or None if not adjacent."""
    self._validate_vertex(u)
    self._validate_vertex(v)
    return self._outgoing[u].get(v)        # returns None if v not adjacent

  def degree(self, v, outgoing=True):
    """Return number of (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to count incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])

  def incident_edges(self, v, outgoing=True):
    """Return all (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to request incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    v = self.Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}        # need distinct map for incoming edges
    return v

  def insert_edge(self, u, v, x=None):
    """Insert and return a new Edge from u to v with auxiliary element x.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """

    if self.get_edge(u, v) is not None:      # includes error checking
      raise ValueError('u and v are already adjacent')
    e = self.Edge(u, v, x)
    self._outgoing[u][v] = e
    self._incoming[v][u] = e
    self.graph[u].append(v)


  def BFS(self,s,d, q = MyQUEUE()):
    temp_path = [s]

    q.enqueue(temp_path)

    while q.IsEmpty() == False:
        tmp_path = q.dequeue()
        last_node = tmp_path[len(tmp_path)-1]
        if last_node == d:
          n = 0
          path = []
          while True:
            path.append(self.get_edge(tmp_path[n],tmp_path[n+1]))
            if (tmp_path[n+1] == last_node):
              break
            n += 1
          self.pathAll.append(path.copy())
        for link_node in self.graph[last_node]:
            if link_node not in tmp_path:
                new_path = []
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)

  def getAllPaths(self, s, d):
          visited = {}
          
          for vertex in self.vertices():
            visited[vertex] = False
              
          self.BFS(s, d)
          t = dict()
          l = list()
          count = 0
          for path in self.pathAll:
            for v in path:
              l.append(v)
              if v._destination == d:
                t[count] = l.copy()
                l.clear()
                count += 1
          list_ordered = []
          for k in sorted(t,key = lambda k: len(t[k])):
            list_ordered.append(k)
          return list_ordered, t

  def minAllPath(self, order,paths):
    list_depth = []
    flow = 0
    l = []
    for x in order:
      for ele in paths[x]:
        l.append(ele._element)
      mini = min(l)
      flow +=mini
      l.clear()
      if (mini > 0):
        for ele in paths[x]:
          ele._element -= mini
          if (ele._element == 0):
            list_depth.append(ele)
    return list_depth

  def maxFlow(self, order, paths, s, d, dem = [], repu = []) :
    list_depth = self.minAllPath(order,paths)
    dem.append(s)
    repu.append(d)
    check = False
    node_for_insert = []
    for x in sorted(paths,key = lambda x: len(paths[x]), reverse=True):
      for ele in paths[x]:
        if(list_depth.__contains__(ele) and check == False):
          list_depth.remove(ele)
          if(not dem.__contains__(ele._origin._element) and not repu.__contains__(ele._origin._element)):
            dem.append(ele._origin._element)
          if(ele._destination._element != d):
            if (not repu.__contains__(ele._destination._element) and not dem.__contains__(ele._destination._element)):
              repu.append(ele._destination._element)
          check = True
        else:
          if (check == True):
            if (not repu.__contains__(ele._origin._element) and not dem.__contains__(ele._origin._element)):
              repu.append(ele._origin._element)
            if (not repu.__contains__(ele._destination._element) and not  dem.__contains__(ele._destination._element)):
              repu.append(ele._destination._element)
          else:
            node_for_insert.append(ele)
      for i in node_for_insert:
        if (not dem.__contains__(i._origin._element) and not repu.__contains__(i._origin._element)):
          dem.append(i._origin._element)
        if (not dem.__contains__(i._destination._element) and not repu.__contains__(i._destination._element)):
          dem.append(i._destination._element)
      check = False
    return dem, repu

  def minCut(self,order, paths, s, d, dem = [], repu = []) :
    list_depth = self.minAllPath(order,paths)
    dem.append(s)
    repu.append(d)
    node_for_insert = []
    for k in sorted(paths,key = lambda k: len(paths[k]), reverse=True):
      for ele in paths[k]:
        if(list_depth.__contains__(ele)):
          if (iter == len(paths[k])):
            if(ele._destination._element == d):
              if(not dem.__contains__(ele._origin._element)):
                dem.append(ele._origin._element)
            else:
              if(not repu.__contains__(ele._origin._element)):
                repu.append(ele._origin._element)
          else:
            node_for_insert.append(ele)
        else:
          if (ele._destination._element == d):
            if(not repu.__contains__(ele._origin._element)):
              repu.append(ele._origin._element)
          else:
            node_for_insert.append(ele)
    for i in node_for_insert:
      if (not dem.__contains__(i._origin._element) and not repu.__contains__(i._origin._element)):
        dem.append(i._origin._element)
      if (not dem.__contains__(i._destination._element) and not repu.__contains__(i._destination._element)):
        dem.append(i._destination._element)
    return dem,repu

  def modify(self,y,V):
    for arc in self.edges():
      self.insert_edge(arc._destination,arc._origin,arc._element)
    y['s'] = self.insert_vertex('s')
    y['t'] = self.insert_vertex('t')
    for key in V:
      if(y[key] is not y['s'] and y[key] is not y['t']):
        self.insert_edge(y['s'],y[key],V[key][0])
        self.insert_edge(y[key],y['t'],V[key][1])







