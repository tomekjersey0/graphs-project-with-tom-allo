from typing import Any
from collections import deque

# This  implementation represents a directed, unweighted graph 
class GraphList:
    """
    Adjacency list representation of a directed graph.

    - Vertices are stored as keys in a dictionary
    - Edges are stored as nested dictionaries (neighbour → value)
    - Edge values are unused (set to None), but allow extension to weighted graphs

    This structure is efficient for sparse graphs and supports traversal algorithms
    such as BFS and DFS.
    """

    def __init__(self):
        self.graph: dict[str, dict[str, Any]] = {}

    # Adds vertex V to the graph
    # If V already exists, adds nothing
    # Time complexity: O(1)
    def add_vertex(self, v: str) -> None:
        self.graph.setdefault(v, dict())

    # Creates the vertex A if A does not exist
    # Also creates the vertex B if B does not exist
    # Time complexity: O(1)
    def add_edge(self, a: str, b: str) -> None:
        self.graph.setdefault(a, dict())[b] = None
        self.add_vertex(b)

    # Removes the Edge A -> B if the edge exists
    # Time complexity: O(1)
    def remove_edge(self, a: str, b: str) -> None:
        if a in self.graph and b in self.graph[a]:
            del self.graph[a][b]

    # Removes the vertex V and any edges pointing to it
    # Time complexity: O(V + E)
    def remove_vertex(self, v: str) -> None:
        if v in self.graph:
            del self.graph[v]
        self.clean_graph()

    # Removes any stale edges
    # If there are edges pointing to vertices that don't exist,
    # removes them from the graph
    # Time complexity: O(V + E)
    def clean_graph(self) -> None:
        exist: set[str] = set(self.graph.keys())

        for v in self.graph:
            to_del = set()

            for e in self.graph[v]:
                if e not in exist:
                    to_del.add(e)

            for d in to_del:
                self.graph[v].pop(d)

    # Checks if a vertex exists in the graph
    # Time complexity: O(1)
    def find_vertex(self, v: str) -> bool:
        return v in self.graph
    
    # Checks if an edge exists in the graph
    # Time complexity: O(1)
    def find_edge(self, a: str, b: str) -> bool:
        return b in self.graph.get(a, {})

    # Checks if there exists a path between two vertices
    # Time complexity: O(V + E)
    def path_exists_between(self, a: str, b: str) -> bool:
        if a not in self.graph or b not in self.graph:
            return False
        
        if a == b:
            return True
        
        visited = set([a])
        q = deque([a])

        while q:
            cur = q.popleft()
            if cur == b:
                return True
            for e in self.graph[cur]:
                if e == b:
                    return True
                if e not in visited:
                    q.append(e)
                    visited.add(e)
        return False