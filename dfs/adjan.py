class Graph:

    def __init__(self, vertices, is_undirected=True):
        self.__v = vertices  # number of vertices
        self.__edge_list = []  # store the edges and their weight
        self.__is_undirected = is_undirected # True for undirected graphs
        self.__adj_matrix = None # stores the adjacency matrix
        self.__adj_list = None # stores the adjacency list

    # method for adding an edge to the graph
    def add_edge(self, u, v, w=None):
        self.__edge_list.append([u, v, w if w else 1])
        # in case it is an undirected graph, 
        # replicate edge in opposite way
        if self.__is_undirected:
            self.__edge_list.append([v, u, w if w else 1])
            
    def make_adjacency_list(self):
        adj_list = {key: [] for key in range(self.__v)}
        for edge in self.__edge_list:
            # where edge[1] is the destiny and edge[2] the weight
            edge_val = {edge[1]: edge[2]} 
            adj_list[edge[0]].append(edge_val)
        self.__adj_list = adj_list