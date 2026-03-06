# Graph
# Adjacency list implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.edges: list[Nodes] = []

    def set_value(self, value):
        self.value = value
        
    def add_edge(self, edge: Node):
        self.edges

class Graph:
    def __init__(self):
        pass