from typing import Any

# Graph

# Adjacency list implementation
class GRAPH_LIST:
    def __init__(self):
        self.graph: dict[str, dict[str, Any]] = {}


    # Adds vertex V to the graph
    # If V already exists, adds nothing
    def add_vertex(self, v: str) -> None:
        self.graph.setdefault(v, dict())

    # Creates the vertex A if A does not exist
    # Also creates the vertex B if B does not exist
    def add_edge(self, a: str, b: str) -> None:
        self.graph.setdefault(a, dict())[b] = None
        self.add_vertex(b)

    # Removes the Edge A -> B if the edge exists
    def remove_edge(self, a: str, b: str) -> None:
        if a in self.graph:
            del self.graph[a][b]

    # Removes the vertex A if it exists
    # Any edges pointing to A remain in the graph
    def remove_vertex(self, v: str) -> None:
        if v in self.graph:
            del self.graph[v]

    # Removes any stale edges
    # If there are edges pointing to vertices that don't exist,
    # removes them from the graph
    def clean_graph(self) -> None:
        exist: set[str] = set(self.graph.keys())

        for v in self.graph:
            to_del = set()

            for e in self.graph[v]:
                if e not in exist:
                    to_del.add(e)

            for d in to_del:
                self.graph[v].pop(d)

    def find_vertex(self, v: str) -> bool:
        return True if v in self.graph else False
    
    def find_edge(self, a: str, b: str) -> bool:
        return b in self.graph.get(a, {})

    def path_exists_between(self, a: str, b: str) -> bool:
        return True