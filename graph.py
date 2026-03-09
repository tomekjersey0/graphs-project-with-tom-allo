# Graph
# Adjacency list implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.edges: list[int] = []

    def set_value(self, value):
        self.value = value
        
    def add_edge(self, edge: int):
        self.edges.append(edge)

class Graph:
    def __init__(self):
        self.vertices: list[Node]
        self.edges: list[list[int]]

    def add_vertex(self, value):
        self.vertices.append(Node(value))

    def remove_vertex(self, index: int):
        
    
    def add_edge(self, node_from: int, node_to: int):

    def remove_edge(self, node_from: int, node_to: int):
        
    def find_vertex_by_index(self, index: int) -> list[Node] | list[None]:

    def find_vertex_by_value(self, value: int) -> list[Node] | list[None]:

    def find_edge(self, index_from: int, index_to: int) -> bool:

    def path_exists_between(self, index_from: int, index_to: int) -> bool:

    