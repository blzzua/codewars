# https://www.codewars.com/kata/5a6b24d4e626c59d5b000066

class Graph(object):
    """ class Graph with path-generators implementations from internet :\ """
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        return set(self._graph_dict.keys())

    def all_edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self._graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths
    
def square_sums_row(N):
    print("start:", N)
    squares = [a**2 for a in range(2,int((2*N)**0.5)+1)]
    def possible_complement(root):
        return {sq - root for sq in squares if  0 < sq - root  <= N}
    possible_complements = { root: possible_complement(root) for root in range(1,N+1)}
    graph = Graph(possible_complements)
    # in case timeouts implement optimizations via false-on-more-then-two single_adjacent and start-end-paths:
    # single_adjacent = [v for v in possible_complement if len(possible_complement[v]) == 1]
    for i in range(1,N+1):
        for j in range(1,i):
            for path in graph.find_all_paths(i,j):
                if len(path) == N:
                    return path
    
    return False
